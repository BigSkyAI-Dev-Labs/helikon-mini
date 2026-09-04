#!/usr/bin/env python3
"""Statically validate the Helikon-mini RC2 live-host QA kit."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
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
EXPECTED_TEST_IDS = [f"LH-{number:02d}" for number in range(1, 15)]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--rc2-archive", type=Path)
    parser.add_argument("--v32-package", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    failures: list[str] = []
    passes: list[str] = []

    observed_local = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "packages" not in path.relative_to(root).parts
    )
    if observed_local == sorted(LOCAL_FILES):
        passes.append("exact local kit inventory")
    else:
        failures.append(f"local inventory mismatch: {observed_local}")

    for relative in LOCAL_FILES:
        path = root / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"missing, non-regular, or symlinked file: {relative}")
            continue
        raw = path.read_bytes()
        if b"\r" in raw or not raw.endswith(b"\n"):
            failures.append(f"UTF-8/LF/terminal-newline failure: {relative}")
            continue
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            failures.append(f"UTF-8 decode failure: {relative}")
    if not any("UTF-8" in failure for failure in failures):
        passes.append("UTF-8 LF text hygiene")

    try:
        source_lock = json.loads((root / "SOURCE_LOCK.json").read_text(encoding="utf-8"))
        evidence = json.loads(
            (root / "LIVE_HOST_QA_EVIDENCE_TEMPLATE.json").read_text(encoding="utf-8")
        )
        if source_lock.get("schema_id") != "helikon_mini.live_host_qa_source_lock":
            failures.append("source-lock schema mismatch")
        if evidence.get("schema_id") != "helikon_mini.live_host_qa_evidence":
            failures.append("evidence-template schema mismatch")
        test_ids = [item.get("test_id") for item in evidence.get("test_results", [])]
        if test_ids != EXPECTED_TEST_IDS:
            failures.append("evidence test IDs/order mismatch")
        else:
            passes.append("source-lock and evidence JSON schemas")
    except (json.JSONDecodeError, OSError, AttributeError) as exc:
        failures.append(f"JSON validation failure: {exc}")
        source_lock = {}

    for relative in LOCAL_FILES:
        if not relative.endswith(".py"):
            continue
        try:
            ast.parse((root / relative).read_text(encoding="utf-8"), filename=relative)
        except (SyntaxError, OSError) as exc:
            failures.append(f"Python syntax failure {relative}: {exc}")
    if not any("Python syntax" in failure for failure in failures):
        passes.append("Python syntax")

    runsheet = (root / "RUNSHEET_Helikon-mini_3.3.0_RC2_live-host-qa.yaml").read_text(
        encoding="utf-8"
    )
    required_runsheet_tokens = [
        "runsheet_schema: helikon-runsheet-v0.1",
        "action_class: external_or_system_affecting_action",
        "operating_state: OPERATOR",
        "external_opt_in_state: missing",
        "destructive_confirmation_state: missing",
        "No in-turn tool path is available here",
        "same-turn YES",
    ]
    missing_tokens = [token for token in required_runsheet_tokens if token not in runsheet]
    if missing_tokens:
        failures.append(f"RUNSHEET missing gate tokens: {missing_tokens}")
    else:
        passes.append("RUNSHEET gate posture")

    report = (root / "RUNSHEET_COMPILATION_REPORT.yaml").read_text(encoding="utf-8")
    if not all(
        token in report
        for token in (
            "compatibility_state: qualified",
            "promotion_assessment: plan_ready",
            "live_execution_completed: false",
            "destructive_confirmation: absent",
        )
    ):
        failures.append("compilation report posture mismatch")
    else:
        passes.append("compilation report posture")

    report_template = (root / "LIVE_HOST_QA_REPORT_TEMPLATE.md").read_text(encoding="utf-8")
    if "TEMPLATE — NOT EXECUTED" not in report_template:
        failures.append("report template lacks non-execution marker")
    else:
        passes.append("report non-execution marker")

    package_root = root / "packages"
    rc2 = args.rc2_archive.resolve() if args.rc2_archive else package_root / "Helikon-mini_3.3.0_RC2_draft_candidate.zip"
    v32 = args.v32_package.resolve() if args.v32_package else package_root / "Helikon-mini_Install_Package_v3.2.0.json"
    try:
        candidate = source_lock["candidate"]
        rc2_lock = candidate["distribution_archive"]
        if rc2.stat().st_size != rc2_lock["bytes"] or sha256(rc2) != rc2_lock["sha256"]:
            failures.append("RC2 distribution does not match source lock")
        else:
            passes.append("RC2 distribution source lock")
        with zipfile.ZipFile(rc2, "r") as archive:
            names = archive.namelist()
            if len(names) != 8 or len(names) != len(set(names)):
                failures.append("RC2 nested distribution inventory count/uniqueness failure")
            for name in names:
                pure = PurePosixPath(name)
                if pure.is_absolute() or ".." in pure.parts or len(pure.parts) != 1:
                    failures.append(f"unsafe RC2 nested path: {name}")
            install_lock = candidate["install_package"]
            install_raw = archive.read(install_lock["member_path"])
            if len(install_raw) != install_lock["bytes"] or hashlib.sha256(install_raw).hexdigest() != install_lock["sha256"]:
                failures.append("RC2 nested install package does not match source lock")
            else:
                passes.append("RC2 nested install package source lock")
    except (KeyError, OSError, zipfile.BadZipFile) as exc:
        failures.append(f"RC2 package validation failure: {exc}")

    try:
        v32_lock = source_lock["upgrade_baseline"]["install_package"]
        if v32.stat().st_size != v32_lock["bytes"] or sha256(v32) != v32_lock["sha256"]:
            failures.append("v3.2 install package does not match source lock")
        else:
            parsed_v32 = json.loads(v32.read_text(encoding="utf-8"))
            if parsed_v32.get("package_version") != "3.2.0":
                failures.append("v3.2 package version mismatch")
            else:
                passes.append("v3.2 package source lock")
    except (KeyError, OSError, json.JSONDecodeError) as exc:
        failures.append(f"v3.2 package validation failure: {exc}")

    output = {
        "schema": "helikon-mini-live-host-qa-kit-validation-v0.1",
        "status": "pass" if not failures else "fail",
        "passes": passes,
        "failures": failures,
        "summary": {"pass": len(passes), "fail": len(failures)},
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
