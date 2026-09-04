#!/usr/bin/env python3
"""Create and reopen a deterministic Helikon-mini engineering review packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path, PurePosixPath


FIXED_TIME = (2026, 9, 4, 0, 0, 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite engineering packet: {output}")
    files = sorted(
        [path for path in root.rglob("*") if path.is_file() and path.resolve() != output],
        key=lambda path: path.relative_to(root).as_posix(),
    )
    if not files:
        raise ValueError("No engineering files found")
    for path in files:
        if path.is_symlink():
            raise ValueError(f"Symlink rejected: {path}")
        pure = PurePosixPath(path.relative_to(root).as_posix())
        if pure.is_absolute() or ".." in pure.parts:
            raise ValueError(f"Unsafe packet path: {pure}")
    if len({p.relative_to(root).as_posix().casefold() for p in files}) != len(files):
        raise ValueError("Case-fold path collision")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            name = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.flag_bits = 0x800
            archive.writestr(info, path.read_bytes(), compresslevel=9)

    with zipfile.ZipFile(output, "r") as archive:
        names = archive.namelist()
        expected = [p.relative_to(root).as_posix() for p in files]
        if names != expected:
            raise ValueError("Reopened engineering packet inventory mismatch")
        for info, path in zip(archive.infolist(), files):
            mode = info.external_attr >> 16
            if info.is_dir() or not stat.S_ISREG(mode) or archive.read(info.filename) != path.read_bytes():
                raise ValueError(f"Reopened engineering packet parity failure: {info.filename}")
    raw = output.read_bytes()
    print(json.dumps({
        "status": "built_and_reopened",
        "output": str(output),
        "file_count": len(files),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "first_member": files[0].relative_to(root).as_posix(),
        "last_member": files[-1].relative_to(root).as_posix(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
