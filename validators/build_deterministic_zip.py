#!/usr/bin/env python3
"""Build and reopen a deterministic eight-file Helikon-mini ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path, PurePosixPath


FILES = [
    "Helikon-mini_Install_Package_v3.3.0.json",
    "Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md",
    "Helikon-mini_OPERATING_LAYER_v3.3.0_install.md",
    "Helikon-mini_QA_PACK_v3.3.0.md",
    "Helikon-mini_README_v3.3.0.md",
    "Helikon-mini_CHANGELOG_v3.3.0.md",
    "Helikon-mini_SHIP_rev33.md",
    "Helikon-mini_LICENSE.md",
]
FIXED_TIME = (2026, 9, 4, 0, 0, 0)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite existing archive: {args.output}")
    observed = sorted(p.name for p in args.release_dir.iterdir())
    if observed != sorted(FILES):
        raise ValueError(f"Release inventory mismatch: {observed}")
    for name in FILES:
        path = args.release_dir / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Unsafe or non-regular release member: {path}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in FILES:
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or len(pure.parts) != 1:
                raise ValueError(f"Unsafe archive path: {name}")
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.flag_bits = 0x800
            archive.writestr(info, (args.release_dir / name).read_bytes(), compresslevel=9)

    with zipfile.ZipFile(args.output, "r") as archive:
        names = archive.namelist()
        if names != FILES:
            raise ValueError(f"Reopened ZIP inventory/order mismatch: {names}")
        comparisons = []
        for info in archive.infolist():
            pure = PurePosixPath(info.filename)
            mode = info.external_attr >> 16
            if info.is_dir() or pure.is_absolute() or ".." in pure.parts or len(pure.parts) != 1:
                raise ValueError(f"Unsafe reopened ZIP path: {info.filename}")
            if not stat.S_ISREG(mode):
                raise ValueError(f"Reopened ZIP member is not regular: {info.filename}")
            archived = archive.read(info.filename)
            source = (args.release_dir / info.filename).read_bytes()
            if archived != source:
                raise ValueError(f"Reopened ZIP content mismatch: {info.filename}")
            comparisons.append({"filename": info.filename, "bytes": len(archived), "sha256": digest(archived)})
    raw_zip = args.output.read_bytes()
    print(json.dumps({
        "status": "built_and_reopened",
        "zip": str(args.output),
        "bytes": len(raw_zip),
        "sha256": digest(raw_zip),
        "members": comparisons,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
