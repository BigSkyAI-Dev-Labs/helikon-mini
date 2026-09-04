#!/usr/bin/env python3
"""Build Helikon-mini 3.3.0 RC2/rev33 from the immutable RC1 source snapshot."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


SOURCE_FILES = [
    "Helikon-mini_Install_Package_v3.3.0.json",
    "Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md",
    "Helikon-mini_OPERATING_LAYER_v3.3.0_install.md",
    "Helikon-mini_QA_PACK_v3.3.0.md",
    "Helikon-mini_README_v3.3.0.md",
    "Helikon-mini_CHANGELOG_v3.3.0.md",
    "Helikon-mini_SHIP_rev32.md",
    "Helikon-mini_LICENSE.md",
]
TARGET_FILES = SOURCE_FILES[:6] + ["Helikon-mini_SHIP_rev33.md", SOURCE_FILES[7]]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite: {path}")
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")


def insert_after(text: str, anchor: str, addition: str) -> str:
    if anchor not in text:
        raise ValueError(f"Required anchor missing: {anchor}")
    return text.replace(anchor, anchor + addition, 1)


def verify_source(source_dir: Path, provenance_path: Path) -> None:
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    expected = {row["filename"]: row for row in provenance["files"]}
    if sorted(p.name for p in source_dir.iterdir()) != sorted(expected):
        raise ValueError("RC1 source inventory mismatch")
    for name, row in expected.items():
        raw = (source_dir / name).read_bytes()
        if len(raw) != row["bytes"] or sha(raw) != row["sha256"]:
            raise ValueError(f"RC1 source provenance mismatch: {name}")


def repair_package(source: dict) -> dict:
    package = copy.deepcopy(source)
    if package.get("package_version") != "3.3.0" or package.get("schema_version") != "1.1.0":
        raise ValueError("RC1 package identity mismatch")

    package["meta"]["modified_date"] = "2026-09-04"
    package["meta"]["reference_ship_manifest"] = "Helikon-mini_SHIP_rev33.md"
    package["meta"]["candidate_revision"] = "RC2 / rev33"
    package["meta"]["derived_from_candidate"] = {
        "candidate": "Helikon-mini 3.3.0 RC1 / rev32",
        "source_snapshot": "source-rc1/v3.3.0",
    }
    package["meta"]["notes"].append(
        "RC2 restores legacy JSON field names/types as deprecated-compatible surfaces and restores the independently versioned kernel sentinel."
    )

    non_runtime = package["metadata_contract"]["non_runtime_fields"]
    if "backward_compatibility_contract" not in non_runtime:
        non_runtime.insert(-1, "backward_compatibility_contract")
    package["backward_compatibility_contract"] = {
        "classification_is_non_runtime": True,
        "source_schema_version": "1.0.0",
        "current_schema_version": "1.1.0",
        "policy": "Retain legacy field names and JSON types while adding host-aware policy fields; legacy aliases may be deprecated but not silently removed within v3.3.0.",
        "restored_surfaces": [
            "install_package_protocols.shared_prereqs.reference_saved_memories:boolean",
            "system_layer.ui_route_guidance legacy keys/types",
            "system_layer.setup_output_contract legacy keys/types",
        ],
        "kernel_sentinel_policy": "HM_KERNEL_SENTINEL tracks the unchanged mini kernel contract independently from the package release.",
    }

    prereqs = package["install_package_protocols"]["shared_prereqs"]
    prereqs["reference_saved_memories"] = True
    prereqs["reference_saved_memories_policy"] = "required_if_available"

    custom = package["system_layer"]["exact_install_text"]["custom_instructions"]
    if "HM_KERNEL_SENTINEL: HMK-3.3.0-REV1" not in custom:
        raise ValueError("RC1 kernel sentinel not found")
    custom = custom.replace("HM_KERNEL_SENTINEL: HMK-3.3.0-REV1", "HM_KERNEL_SENTINEL: HMK-3.0.0-REV1")
    package["system_layer"]["exact_install_text"]["custom_instructions"] = custom
    package["system_layer"]["payload_integrity"]["custom_instructions"] = {
        "sha256": sha(custom.encode("utf-8")),
        "chars": len(custom),
    }

    package["system_layer"]["operator_flow"] = [
        "Begin SETUP with a plain-language orientation before printing the snippets.",
        "Explain that Personalization is ChatGPT's settings/customization area for behavior/profile text.",
        "Tell the operator to look in the profile/avatar/name menu first because exact placement varies by client.",
        "Route by visible labels: profile/avatar/name menu -> Personalization, or profile/avatar/name menu -> Settings -> Personalization.",
        "Before pasting, use a normal non-Temporary chat and enable Reference saved memories if available; Reference chat history is optional.",
        "Explain that SETUP uses two separate fields: Custom instructions and About you / More about you or its visible equivalent.",
        "Explicitly warn not to paste both snippets into the same field.",
        "Guide the save order: Snippet 1, save; Snippet 2, save; reopen Personalization and confirm both persisted.",
        "If either required field is absent, stop with CLARIFY_NEEDED and report the visible labels; never merge payloads silently.",
        "After persistence is confirmed, return to ordinary chat and send INSTALL; reprint both snippets verbatim when SETUP is requested.",
    ]

    ui = package["system_layer"]["ui_route_guidance"]
    ui.update(
        {
            "entry_surface_note": "Personalization is ChatGPT's settings/customization area for behavior/profile text.",
            "open_personalization_routes": [
                "Profile/avatar/name menu -> Personalization",
                "Profile/avatar/name menu -> Settings -> Personalization",
            ],
            "first_time_user_note": "Mount Helikon-mini 3.3 AIOS SETUP uses two separate fields inside Personalization, not one.",
            "save_order": [
                "Open Custom instructions, paste Snippet 1, click Save.",
                "Return to Personalization, open About you / More about you or its visible equivalent, paste Snippet 2, click Save.",
                "Close and reopen Settings/Personalization to confirm both blocks persisted.",
                "Return to ordinary chat and send INSTALL to begin the six-memory Operating Layer loop.",
            ],
            "memory_settings_before_pasting": [
                "Reference saved memories -> ON if available",
                "Reference chat history -> optional best-effort only if present; not required for runtime completeness",
                "Use a normal non-Temporary chat for installation",
            ],
            "post_setup_handoff": "After both saves are confirmed, return to ordinary chat and send INSTALL to begin the six-memory Operating Layer install loop.",
        }
    )

    setup = package["system_layer"]["setup_output_contract"]
    setup.update(
        {
            "must_precede_snippets_with_beginner_orientation": True,
            "must_explain_personalization_plain_language": "Personalization is ChatGPT's settings/customization area for behavior/profile text.",
            "must_tell_operator_where_to_look": "Look in the profile/avatar/name menu first because exact placement varies by client.",
            "visible_routes": [
                "Profile/avatar/name menu -> Personalization",
                "Profile/avatar/name menu -> Settings -> Personalization",
            ],
            "must_explain_two_boxes_not_one": [
                "Custom instructions",
                "About you / More about you or equivalent visible profile text field",
            ],
            "must_warn_not_same_field": True,
            "required_save_order": [
                "Open Custom instructions, paste Snippet 1, click Save.",
                "Return to Personalization, open About you / More about you or its visible equivalent, paste Snippet 2, click Save.",
                "Close and reopen Settings/Personalization to confirm both blocks persisted.",
            ],
            "must_reprint_two_snippets_verbatim_after_orientation": True,
            "must_check_memory_settings_before_pasting": True,
            "required_memory_settings": [
                "Reference saved memories -> ON if available",
                "Reference chat history -> optional best-effort only if present; not required for runtime completeness",
                "Use a normal non-Temporary chat for installation",
            ],
            "must_instruct_post_setup_install_handoff": True,
            "required_post_setup_handoff": "After both saves are confirmed, return to ordinary chat and send INSTALL to begin the six-memory Operating Layer install loop.",
        }
    )
    return package


def repair_system_markdown(source: str) -> str:
    text = source.replace("HM_KERNEL_SENTINEL: HMK-3.3.0-REV1", "HM_KERNEL_SENTINEL: HMK-3.0.0-REV1")
    note = (
        "\n\n> **RC2 compatibility note:** The JSON package retains the legacy setup/UI field names and types as deprecated-compatible surfaces while keeping the label-based host guidance. The kernel sentinel remains independently versioned at `HMK-3.0.0-REV1`."
    )
    return insert_after(
        text,
        "> **Authority:** `Helikon-mini_Install_Package_v3.3.0.json` is the primary install artifact and installation SSOT. This file is a synchronized human-readable projection/fallback.",
        note,
    )


def repair_qa(source: str) -> str:
    text = source.replace("(v3.3.0 RC1)", "(v3.3.0 RC2 / rev33)")
    text = text.replace("SHIP `rev32`", "SHIP `rev33`")
    text = text.replace("Helikon-mini_SHIP_rev32.md", "Helikon-mini_SHIP_rev33.md")
    text = text.replace("Helikon-mini_3.3.0_draft_candidate.zip", "Helikon-mini_3.3.0_RC2_draft_candidate.zip")
    text = text.replace(
        "--source-dir source-v3.2.0 --provenance governance/SOURCE_PROVENANCE_v3.2.0.json",
        "--source-dir source-rc1/v3.3.0 --provenance governance/RC1_SOURCE_PROVENANCE.json",
    )
    addition = """
## K. RC2 backward-compatibility gates

- [ ] `shared_prereqs.reference_saved_memories` remains JSON Boolean `true`.
- [ ] `shared_prereqs.reference_saved_memories_policy` separately equals `required_if_available`.
- [ ] Legacy `ui_route_guidance` field names remain present with their v3.2 JSON types while RC1 label-based fields remain active.
- [ ] Legacy `setup_output_contract` field names remain present with their v3.2 JSON types while RC1 host-aware fields remain active.
- [ ] `operator_flow` again provides the complete ten-step compatible sequence.
- [ ] `backward_compatibility_contract.classification_is_non_runtime` is `true`.
- [ ] `HM_KERNEL_SENTINEL` is exactly `HMK-3.0.0-REV1` in JSON and the System Markdown projection.
- [ ] Memory payload IDs, memory sentinels, Operating installer, commands, modes, verdicts, and host-memory truth rules remain unchanged from RC1.

"""
    text = text.replace("## K. Live host tests — deferred in RC1", addition + "## L. Live host tests — deferred in RC2")
    return text


def repair_readme(source: str) -> str:
    text = source.replace("**Status:** `v3.3.0 draft_candidate / RC1`", "**Status:** `v3.3.0 draft_candidate / RC2 / rev33`")
    text = text.replace("Helikon-mini_SHIP_rev32.md", "Helikon-mini_SHIP_rev33.md")
    section = """
## RC2 compatibility repair

RC2 preserves RC1's host-memory truth rules while restoring machine-consumer compatibility. The legacy setup and UI JSON keys/types remain available as deprecated-compatible fields; `reference_saved_memories` remains Boolean `true`, while the host-aware `required_if_available` policy moves to `reference_saved_memories_policy`. The package-level release remains 3.3.0, but the unchanged mini kernel contract retains its independent `HMK-3.0.0-REV1` sentinel. SHIP advances to rev33 so corrected bytes never reuse rev32 identity.

"""
    return text.replace("## Distribution and QA", section + "## Distribution and QA")


def repair_changelog(source: str) -> str:
    source = source.replace("## v3.3.0 — rev32 draft candidate (2026-09-04)", "## v3.3.0 — rev32 draft candidate / RC1 (2026-09-04)", 1)
    entry = """
## v3.3.0 — rev33 draft candidate / RC2 (2026-09-04)

- Restores `install_package_protocols.shared_prereqs.reference_saved_memories` to Boolean `true` for backward-compatible consumers.
- Adds `reference_saved_memories_policy: required_if_available` as the separate host-aware policy field.
- Restores all v3.2 `system_layer.ui_route_guidance` and `system_layer.setup_output_contract` field names with their legacy JSON types while retaining RC1's additive label-based and missing-field rules.
- Restores the full ten-step `system_layer.operator_flow` sequence.
- Adds a non-runtime `backward_compatibility_contract` documenting the compatibility surface.
- Restores `HM_KERNEL_SENTINEL` to the independently versioned `HMK-3.0.0-REV1`; no kernel-contract change was established by the package version bump.
- Advances SHIP identity to rev33 and reruns exact projections, file hashes, source preservation, archive safety, and reproducible packaging checks.
- Preserves RC1's memory IDs, memory payload semantics/sentinels, Operating installer, host-memory truth rules, commands, modes, verdicts, and draft-candidate posture.

"""
    anchor = "This changelog tracks the independently versioned free/open-source mini line. Full Mount Helikon versions are compatibility references only and do not determine mini's version.\n"
    return insert_after(source, anchor, entry)


def repair_ship(source: str) -> str:
    text = source.replace("rev32", "rev33").replace("RC1", "RC2")
    old = (
        "rev33 advances mini from v3.2.0 to v3.3.0 as a host-compatibility and packaging repair. It completes the canonical eight-file release family, restores the final Operating payload boundary, adds deterministic validation/packaging support, updates documentation links and navigation posture, and prevents synthesized/opaque host memory from being misreported as FULL. It preserves the two-layer runtime, six stable memory IDs, command family, modes, verdicts, action gates, and MIT posture."
    )
    new = (
        "rev33 is the RC2 compatibility correction to the v3.3.0 host-compatibility and packaging release. It restores legacy JSON field names/types, separates the Saved Memory availability policy from the legacy Boolean prerequisite, and restores the independently versioned `HMK-3.0.0-REV1` kernel sentinel. It preserves RC1's two-layer runtime, six stable memory IDs, exact payload behavior, host-memory truth boundary, command family, modes, verdicts, action gates, and MIT posture. rev32 remains preserved as the superseded RC1 source candidate."
    )
    if old not in text:
        raise ValueError("RC1 SHIP revision note not found")
    return text.replace(old, new)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--provenance", type=Path, required=True)
    parser.add_argument("--release-dir", type=Path, required=True)
    args = parser.parse_args()
    if any(args.release_dir.iterdir()):
        raise FileExistsError(f"Release directory must be empty: {args.release_dir}")
    verify_source(args.source_dir, args.provenance)

    source_text = {name: (args.source_dir / name).read_text(encoding="utf-8") for name in SOURCE_FILES}
    package = repair_package(json.loads(source_text[SOURCE_FILES[0]]))
    outputs = {
        TARGET_FILES[1]: repair_system_markdown(source_text[SOURCE_FILES[1]]),
        TARGET_FILES[2]: source_text[SOURCE_FILES[2]],
        TARGET_FILES[3]: repair_qa(source_text[SOURCE_FILES[3]]),
        TARGET_FILES[4]: repair_readme(source_text[SOURCE_FILES[4]]),
        TARGET_FILES[5]: repair_changelog(source_text[SOURCE_FILES[5]]),
        TARGET_FILES[6]: repair_ship(source_text[SOURCE_FILES[6]]),
        TARGET_FILES[7]: source_text[SOURCE_FILES[7]],
    }
    for name, value in outputs.items():
        write_new(args.release_dir / name, value)

    inventory = []
    for name in TARGET_FILES[1:]:
        raw = (args.release_dir / name).read_bytes()
        inventory.append({"filename": name, "sha256": sha(raw), "bytes": len(raw)})
    package["ship_sync"] = {
        "current_manifest": "Helikon-mini_SHIP_rev33.md",
        "current_manifest_rev": "rev33",
        "shipped_bundle_count": 8,
        "shipped_files": TARGET_FILES,
        "source_file_inventory": inventory,
    }
    write_new(args.release_dir / TARGET_FILES[0], json.dumps(package, ensure_ascii=False, indent=2))
    print(json.dumps({"status": "built", "candidate": "3.3.0 RC2 / rev33", "files": TARGET_FILES}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
