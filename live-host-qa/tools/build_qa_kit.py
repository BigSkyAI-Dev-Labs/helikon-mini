#!/usr/bin/env python3
"""Build and reopen a deterministic Helikon-mini RC2 live-host QA kit."""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path, PurePosixPath


LOCAL_FILES = [
    "README.md",
    "RUNSHEET_Helikon-mini_3.3.0_RC2_live-host-qa.yaml",
    "RUNSHEET_COMPILATION_REPORT.yaml",
    "SOURCE_LOCK.json",
    "Helikon-mini_3.3.0_RC2_LIVE_HOST_QA_OPERATOR_GUIDE.md",
    "LIVE_HOST_QA_EVIDENCE_TEMPLATE.json",
    "LIVE_HOST_QA_REPORT_TEMPLATE.md",
    "tools/validate_qa_kit.py",
    "tools/validate_live_host_evidence.py",
    "tools/build_qa_kit.py",
]
FIXED_TIME = (2026, 9, 4, 0, 0, 0)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kit-root", type=Path, required=True)
    parser.add_argument("--rc2-archive", type=Path, required=True)
    parser.add_argument("--v32-package", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.kit_root.resolve()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing archive: {output}")
    sources = [(relative, root / relative) for relative in LOCAL_FILES]
    sources.extend(
        [
            ("packages/Helikon-mini_3.3.0_RC2_draft_candidate.zip", args.rc2_archive.resolve()),
            ("packages/Helikon-mini_Install_Package_v3.2.0.json", args.v32_package.resolve()),
        ]
    )
    sources.sort(key=lambda item: item[0])

    names = [name for name, _ in sources]
    if len(names) != 12 or len(names) != len(set(name.casefold() for name in names)):
        raise ValueError("QA kit must contain twelve unique case-safe files")
    for name, path in sources:
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts or not path.is_file() or path.is_symlink():
            raise ValueError(f"Unsafe QA kit member: {name} <- {path}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, path in sources:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.flag_bits = 0x800
            archive.writestr(info, path.read_bytes(), compresslevel=9)

    members: list[dict[str, object]] = []
    with zipfile.ZipFile(output, "r") as archive:
        if archive.namelist() != names:
            raise ValueError("Reopened QA kit inventory/order mismatch")
        for info, (name, path) in zip(archive.infolist(), sources):
            mode = info.external_attr >> 16
            raw = archive.read(name)
            if info.is_dir() or not stat.S_ISREG(mode) or raw != path.read_bytes():
                raise ValueError(f"Reopened QA kit parity failure: {name}")
            members.append({"filename": name, "bytes": len(raw), "sha256": digest(raw)})

    raw_output = output.read_bytes()
    print(
        json.dumps(
            {
                "status": "built_and_reopened",
                "output": str(output),
                "bytes": len(raw_output),
                "sha256": digest(raw_output),
                "member_count": len(members),
                "members": members,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
