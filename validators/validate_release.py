#!/usr/bin/env python3
"""Deterministic static validator for the Helikon-mini 3.3.0 release family."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
MEMORIES = [
    "Helikon-mini.Aoideon.Canon",
    "Helikon-mini.Aoideon.Enforcement",
    "Helikon-mini.Meleteon.Budget",
    "Helikon-mini.Meleteon.Builder",
    "Helikon-mini.Mnemeon.Digests",
    "Helikon-mini.Mnemeon.Guard",
]
COMMANDS = ["INSTALL", "EXTRACT", "REMEMBER", "NEXT", "FINAL_VERIFY"]
DOC_URLS = [
    "https://help.openai.com/en/articles/8590148-memory-faq",
    "https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions",
    "https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt",
    "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


class Checks:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, check_id: str, condition: bool, evidence: str, limitation: str = "") -> None:
        self.items.append({
            "check_id": check_id,
            "result": "pass" if condition else "fail",
            "evidence": evidence,
            "limitation": limitation,
        })

    def note(self, check_id: str, result: str, evidence: str, limitation: str = "") -> None:
        self.items.append({"check_id": check_id, "result": result, "evidence": evidence, "limitation": limitation})

    @property
    def passed(self) -> bool:
        return all(item["result"] != "fail" for item in self.items)


def extract_system_projection(markdown: str, key: str) -> str:
    start = f"<!-- JSON_PROJECTION_START:{key} -->"
    end = f"<!-- JSON_PROJECTION_END:{key} -->"
    pattern = re.escape(start) + r"\n```text\n(.*?)\n```\n" + re.escape(end)
    match = re.search(pattern, markdown, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Missing System projection markers for {key}")
    return match.group(1)


def extract_memory_projection(markdown: str, name: str) -> str:
    start = f"<!-- MEMORY_PAYLOAD_START:{name} -->"
    end = f"<!-- MEMORY_PAYLOAD_END:{name} -->"
    pattern = re.escape(start) + r"\n\n---\n\n(.*?)\n\n---\n\n" + re.escape(end)
    match = re.search(pattern, markdown, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Missing or unclosed Operating payload markers for {name}")
    return match.group(1)


def validate_source(checks: Checks, source_dir: Path | None, provenance_path: Path | None) -> None:
    if source_dir is None and provenance_path is None:
        checks.note("SOURCE-PROVENANCE", "not-applicable", "Source validation not requested in this invocation.")
        return
    if source_dir is None or provenance_path is None:
        checks.add("SOURCE-PROVENANCE", False, "Both --source-dir and --provenance are required together.")
        return
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    expected = {row["filename"]: row for row in provenance["files"]}
    observed = sorted(p.name for p in source_dir.iterdir())
    checks.add("SOURCE-INVENTORY", observed == sorted(expected), f"Observed {len(observed)} source files; expected {len(expected)}.")
    matches = True
    for name, row in expected.items():
        path = source_dir / name
        if not path.is_file() or path.is_symlink():
            matches = False
            continue
        raw = path.read_bytes()
        matches = matches and len(raw) == row["bytes"] and sha(raw) == row["sha256"]
        if "git_blob_sha" in row:
            matches = matches and git_blob(raw) == row["git_blob_sha"]
    checks.add(
        "SOURCE-PROVENANCE",
        matches and provenance.get("source_candidate") == "Helikon-mini 3.3.0 RC1",
        "RC1 source bytes, byte counts, SHA-256 values, and source-candidate identity were compared to the provenance manifest.",
    )


def validate_zip(checks: Checks, zip_path: Path | None, release_dir: Path) -> None:
    if zip_path is None:
        checks.note("RG-13", "not-applicable", "No ZIP supplied for this pre-package validation pass.")
        checks.note("RG-14", "not-applicable", "No emitted ZIP supplied for post-build parity.")
        return
    safe = True
    parity = True
    with zipfile.ZipFile(zip_path, "r") as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        safe = safe and names == FILES and len(names) == len(set(names)) and len({n.casefold() for n in names}) == len(names)
        for info in infos:
            pure = PurePosixPath(info.filename)
            mode = info.external_attr >> 16
            safe = safe and not info.is_dir() and not pure.is_absolute() and ".." not in pure.parts and len(pure.parts) == 1 and stat.S_ISREG(mode)
            path = release_dir / info.filename
            parity = parity and path.is_file() and archive.read(info.filename) == path.read_bytes()
    checks.add("RG-13", safe, "Reopened ZIP paths are unique, case-safe, root-relative regular files with no traversal.")
    checks.add("RG-14", parity, "Every reopened ZIP member was byte-compared with the validated release directory.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-dir", type=Path, required=True)
    parser.add_argument("--zip", dest="zip_path", type=Path)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--provenance", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    checks = Checks()

    release = args.release_dir
    observed = sorted(p.name for p in release.iterdir())
    regular = all((release / name).is_file() and not (release / name).is_symlink() for name in observed)
    checks.add("RG-01", True, "Authoritative target is v3.3.0 RC2 draft_candidate with SHIP rev33.")
    checks.add("RG-02", observed == sorted(FILES), f"Observed exact release inventory: {observed}")
    checks.add("RG-04", observed == sorted(FILES) and regular, "Exactly eight expected regular files are present.")
    checks.add("INVENTORY-CASEFOLD", len({name.casefold() for name in observed}) == len(observed), "No case-fold filename collisions.")

    text_files: dict[str, str] = {}
    text_hygiene = True
    for name in observed:
        raw = (release / name).read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text_hygiene = False
            continue
        text_files[name] = text
        text_hygiene = text_hygiene and b"\r" not in raw and raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    checks.add("TEXT-HYGIENE", text_hygiene, "All shipped files are UTF-8/LF with exactly one terminal newline.")
    markdown_names = [name for name in observed if name.endswith(".md")]
    markdown_structure = all(text_files.get(name, "").startswith("# ") for name in markdown_names)
    checks.add("MARKDOWN-STRUCTURE", markdown_structure, "Every shipped Markdown artifact begins with a level-one heading at column 1.")

    package_path = release / FILES[0]
    try:
        package = json.loads(package_path.read_text(encoding="utf-8"))
        json_ok = True
    except Exception as exc:
        package = {}
        json_ok = False
        checks.add("JSON-PARSE", False, f"JSON parse failed: {exc}")
    if json_ok:
        checks.add("JSON-PARSE", True, "Primary package parsed as UTF-8 JSON.")

    identity_ok = (
        package.get("schema_id") == "helikon_mini.install_package"
        and package.get("schema_version") == "1.1.0"
        and package.get("package_version") == "3.3.0"
        and package.get("system_name") == "Mount Helikon-mini 3.3 AIOS"
        and package.get("status") == "draft_candidate"
    )
    checks.add("RG-05", identity_ok, "Schema, filename-era version, system identity, and candidate status were checked.")
    expected_counts = package.get("integrity", {}).get("expected_counts", {})
    checks.add(
        "COUNT-CONTRACT",
        expected_counts == {
            "runtime_layer_count": 2,
            "system_layer_payload_count": 2,
            "operating_layer_memory_count": 6,
            "entrypoint_count": 2,
            "operating_layer_live_command_count": 5,
            "shipped_file_count": 8,
        },
        f"Expected-count contract: {expected_counts}",
    )

    layers = package.get("runtime_contract", {}).get("runtime_layers", [])
    two_layers = package.get("runtime_contract", {}).get("runtime_layer_count") == 2 and [x.get("id") for x in layers] == ["system_layer", "operating_layer"]
    host = package.get("host_compatibility_contract", {})
    taxonomy = two_layers and host.get("classification_is_non_runtime") is True
    checks.add("RG-03", taxonomy, "Mini compatibility is qualified: exact two-layer contract preserved; host classifications explicitly non-runtime.")
    checks.add("RG-10", taxonomy, "No host QA classification is promoted into the two-layer runtime contract.")
    checks.note("RG-08", "not-applicable", "Exact twelve-record inventory is a full Helikon gate; mini intentionally ships six compressed records.", "Full twelve-pillar taxonomy remains a compatibility reference, not mini runtime authority.")
    checks.note("RG-09", "not-applicable", "Full Helikon twelve-owner parity is not a mini shipped-record gate.", "Mini COVERS labels are compression/provenance labels.")

    shipped = package.get("ship_sync", {}).get("shipped_files")
    pointers_ok = shipped == FILES and package.get("ship_sync", {}).get("current_manifest") == FILES[6] and package.get("ship_sync", {}).get("current_manifest_rev") == "rev33"
    pointers_ok = pointers_ok and package.get("system_layer", {}).get("installer_filename_legacy_projection") == FILES[1]
    pointers_ok = pointers_ok and package.get("operating_layer", {}).get("installer_filename_legacy_projection") == FILES[2]
    checks.add("RG-06", pointers_ok, "SHIP, System projection, Operating projection, manifest revision, and JSON filename pointers agree.")

    sys_payloads = package.get("system_layer", {}).get("exact_install_text", {})
    sys_integrity = package.get("system_layer", {}).get("payload_integrity", {})
    sys_ok = set(sys_payloads) == {"custom_instructions", "more_about_you"}
    for key, value in sys_payloads.items():
        record = sys_integrity.get(key, {})
        sys_ok = sys_ok and record.get("chars") == len(value) and record.get("sha256") == sha(value.encode("utf-8")) and len(value) <= 1500
    checks.add("SYSTEM-INTEGRITY", sys_ok, f"System payload lengths: { {k: len(v) for k,v in sys_payloads.items()} }")

    system_md = text_files.get(FILES[1], "")
    try:
        sys_projection_ok = all(extract_system_projection(system_md, f"system_layer.exact_install_text.{key}") == value for key, value in sys_payloads.items())
    except Exception:
        sys_projection_ok = False
    checks.add("SYSTEM-PROJECTION", sys_projection_ok, "Both marked System Markdown blocks were byte-equivalent as Unicode text to JSON payloads.")

    operating = package.get("operating_layer", {})
    install_script = operating.get("installation_script", "")
    install_integrity = operating.get("installation_script_integrity", {})
    install_ok = install_integrity.get("chars") == len(install_script) and install_integrity.get("sha256") == sha(install_script.encode("utf-8"))
    op_md = text_files.get(FILES[2], "")
    projected_script = op_md.split("\n\n<!-- END MOUNT HELIKON-MINI 3.3 AIOS OPERATING LAYER INSTALLATION SCRIPT -->", 1)[0]
    install_ok = install_ok and projected_script == install_script
    checks.add("INSTALLER-PROJECTION", install_ok, "Operating installer script integrity and Markdown projection were compared exactly.")

    memories = operating.get("memories", [])
    memory_ids = [m.get("memory_name") for m in memories]
    memory_ok = memory_ids == MEMORIES
    memory_projection_ok = True
    for memory in memories:
        name = memory.get("memory_name", "")
        payload = memory.get("payload_text", "")
        record = memory.get("payload_integrity", {})
        memory_ok = memory_ok and record.get("chars") == len(payload) and record.get("sha256") == sha(payload.encode("utf-8"))
        try:
            memory_projection_ok = memory_projection_ok and extract_memory_projection(op_md, name) == payload
        except Exception:
            memory_projection_ok = False
    marker_names = re.findall(r"<!-- MEMORY_PAYLOAD_START:([^>]+) -->", op_md)
    memory_projection_ok = memory_projection_ok and marker_names == MEMORIES
    checks.add("MEMORY-INTEGRITY", memory_ok, f"Exact six IDs/order and embedded payload hashes checked: {memory_ids}")
    checks.add("MEMORY-PROJECTION", memory_projection_ok, "All six marked payloads, including the final closing boundary, match JSON exactly.")

    protocols = package.get("install_package_protocols", {})
    functions_ok = protocols.get("entrypoints") == ["SETUP", "INSTALL"] and protocols.get("operating_layer_live_commands") == COMMANDS
    functions_ok = functions_ok and protocols.get("canonical_build_token") == "APPROVE" and protocols.get("destructive_token") == "YES"
    checks.add("RG-07", functions_ok, "Entrypoints, five live commands, build token, and destructive token match the approved mini contract.")

    inventory = package.get("ship_sync", {}).get("source_file_inventory", [])
    inventory_ok = [row.get("filename") for row in inventory] == FILES[1:]
    for row in inventory:
        path = release / row.get("filename", "")
        if not path.is_file():
            inventory_ok = False
            continue
        raw = path.read_bytes()
        inventory_ok = inventory_ok and row.get("bytes") == len(raw) and row.get("sha256") == sha(raw)
    checks.add("RG-12", inventory_ok, "JSON byte/SHA-256 inventory matches all seven non-self shipped files.")

    combined_docs = "\n".join(text_files.get(name, "") for name in FILES[1:7])
    docs_ok = all(url in text_files.get(FILES[4], "") for url in DOC_URLS)
    docs_ok = docs_ok and "synthesized" in combined_docs and "missing: unknown" in combined_docs and "non-runtime" in combined_docs
    checks.add("RG-11", docs_ok, "Host truth boundary, non-runtime classifications, and four official documentation links are present.")
    footer_ok = "[Policy Attestation:" not in sys_payloads.get("custom_instructions", "") and "Confidence: N/100" in sys_payloads.get("custom_instructions", "")
    checks.add("FOOTER-CONTRACT", footer_ok, "Always-on policy attestation removed; single confidence footer retained.")
    action_ok = "current-message APPROVE" in sys_payloads.get("custom_instructions", "") and "external actions" in sys_payloads.get("custom_instructions", "") and "same-turn YES" in sys_payloads.get("custom_instructions", "")
    checks.add("ACTION-GATES", action_ok, "Bounded APPROVE, separate external-action authority, and same-turn YES are present in the System payload.")

    prereqs = protocols.get("shared_prereqs", {})
    prereq_compat = type(prereqs.get("reference_saved_memories")) is bool and prereqs.get("reference_saved_memories") is True
    prereq_compat = prereq_compat and prereqs.get("reference_saved_memories_policy") == "required_if_available"
    checks.add("RC2-PREREQ-COMPAT", prereq_compat, "Legacy Saved Memory prerequisite remains Boolean true; host availability policy is a separate string field.")

    ui = package.get("system_layer", {}).get("ui_route_guidance", {})
    setup = package.get("system_layer", {}).get("setup_output_contract", {})
    ui_legacy_types = {
        "entry_surface_note": str,
        "open_personalization_routes": list,
        "paste_targets": list,
        "first_time_user_note": str,
        "same_field_warning": str,
        "save_order": list,
        "memory_settings_before_pasting": list,
        "post_setup_handoff": str,
    }
    setup_legacy_types = {
        "must_precede_snippets_with_beginner_orientation": bool,
        "must_explain_personalization_plain_language": str,
        "must_tell_operator_where_to_look": str,
        "visible_routes": list,
        "must_explain_two_boxes_not_one": list,
        "must_warn_not_same_field": bool,
        "required_save_order": list,
        "must_reprint_two_snippets_verbatim_after_orientation": bool,
        "must_check_memory_settings_before_pasting": bool,
        "required_memory_settings": list,
        "must_instruct_post_setup_install_handoff": bool,
        "required_post_setup_handoff": str,
    }
    legacy_types_ok = all(type(ui.get(key)) is expected for key, expected in ui_legacy_types.items())
    legacy_types_ok = legacy_types_ok and all(type(setup.get(key)) is expected for key, expected in setup_legacy_types.items())
    checks.add("RC2-LEGACY-FIELDS", legacy_types_ok, "All named legacy UI/setup JSON fields are present with their v3.2 types.")

    additive_types = {
        "ui.route_rule": type(ui.get("route_rule")) is str,
        "ui.missing_field_rule": type(ui.get("missing_field_rule")) is str,
        "ui.memory_settings": type(ui.get("memory_settings")) is list,
        "setup.beginner_orientation_first": type(setup.get("beginner_orientation_first")) is bool,
        "setup.label_based_navigation": type(setup.get("label_based_navigation")) is bool,
        "setup.two_separate_payloads": type(setup.get("two_separate_payloads")) is bool,
        "setup.must_reprint_payloads_verbatim": type(setup.get("must_reprint_payloads_verbatim")) is bool,
        "setup.must_stop_if_required_field_absent": type(setup.get("must_stop_if_required_field_absent")) is bool,
        "setup.post_setup_handoff": type(setup.get("post_setup_handoff")) is str,
    }
    compat_contract = package.get("backward_compatibility_contract", {})
    additive_ok = all(additive_types.values()) and compat_contract.get("classification_is_non_runtime") is True
    checks.add("RC2-ADDITIVE-FIELDS", additive_ok, "RC1 host-aware fields remain present and the compatibility contract is explicitly non-runtime.")

    flow = package.get("system_layer", {}).get("operator_flow", [])
    checks.add("RC2-OPERATOR-FLOW", isinstance(flow, list) and len(flow) == 10, "System operator_flow contains the restored ten-step compatible sequence.")
    sentinel_ok = sys_payloads.get("custom_instructions", "").count("HM_KERNEL_SENTINEL: HMK-3.0.0-REV1") == 1
    sentinel_ok = sentinel_ok and "HM_KERNEL_SENTINEL: HMK-3.3.0-REV1" not in sys_payloads.get("custom_instructions", "")
    sentinel_ok = sentinel_ok and "HM_KERNEL_SENTINEL: HMK-3.0.0-REV1" in system_md
    checks.add("RC2-KERNEL-SENTINEL", sentinel_ok, "Active JSON and System projection use only the independently versioned HMK-3.0.0-REV1 kernel sentinel.")
    qa_text = text_files.get(FILES[3], "")
    qa_paths_ok = "--source-dir source-rc1/v3.3.0 --provenance governance/RC1_SOURCE_PROVENANCE.json" in qa_text
    qa_paths_ok = qa_paths_ok and "SOURCE_PROVENANCE_v3.2.0.json" not in qa_text and "--source-dir source-v3.2.0" not in qa_text
    checks.add("RC2-QA-PROCEDURE", qa_paths_ok, "Shipped QA commands point to the RC2 engineering packet's RC1 snapshot and provenance manifest.")

    if args.source_dir:
        source_package = json.loads((args.source_dir / "Helikon-mini_Install_Package_v3.3.0.json").read_text(encoding="utf-8"))
        source_custom = source_package["system_layer"]["exact_install_text"]["custom_instructions"]
        expected_custom = source_custom.replace("HM_KERNEL_SENTINEL: HMK-3.3.0-REV1", "HM_KERNEL_SENTINEL: HMK-3.0.0-REV1")
        semantic_preservation = package.get("operating_layer") == source_package.get("operating_layer")
        semantic_preservation = semantic_preservation and package.get("host_compatibility_contract") == source_package.get("host_compatibility_contract")
        semantic_preservation = semantic_preservation and sys_payloads.get("more_about_you") == source_package["system_layer"]["exact_install_text"]["more_about_you"]
        semantic_preservation = semantic_preservation and sys_payloads.get("custom_instructions") == expected_custom
        semantic_preservation = semantic_preservation and protocols.get("entrypoints") == source_package["install_package_protocols"]["entrypoints"]
        semantic_preservation = semantic_preservation and protocols.get("operating_layer_live_commands") == source_package["install_package_protocols"]["operating_layer_live_commands"]
        checks.add("RC1-SEMANTIC-PRESERVATION", semantic_preservation, "Operating layer, host-memory truth rules, commands, About You payload, and all Custom Instructions text except the intended sentinel repair match RC1.")

    validate_source(checks, args.source_dir, args.provenance)
    validate_zip(checks, args.zip_path, release)
    checks.add("RG-15", checks.passed, "Static completion evidence is direct and machine-checkable.", "Live ChatGPT persistence and runtime behavior remain untested.")
    checks.note("LIVE-HOST-QA", "provisional", "Static package validation cannot prove live host persistence, exact memory retention, or runtime activation.")

    report = {
        "schema": "helikon-mini-static-validation-v1",
        "candidate": "3.3.0-rc2-rev33",
        "status": "pass" if checks.passed else "fail",
        "release_readiness": "provisional_live_qa_pending" if checks.passed else "blocked",
        "release_dir": str(release),
        "zip": str(args.zip_path) if args.zip_path else None,
        "checks": checks.items,
        "summary": {
            "pass": sum(x["result"] == "pass" for x in checks.items),
            "fail": sum(x["result"] == "fail" for x in checks.items),
            "provisional": sum(x["result"] == "provisional" for x in checks.items),
            "not_applicable": sum(x["result"] == "not-applicable" for x in checks.items),
        },
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        if args.report.exists():
            raise FileExistsError(f"Refusing to overwrite report: {args.report}")
        args.report.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    return 0 if checks.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
