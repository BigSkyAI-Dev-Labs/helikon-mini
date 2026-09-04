#!/usr/bin/env python3
"""Validate one Helikon-mini RC2 live-host evidence record without mutating it."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_TEST_IDS = [f"LH-{number:02d}" for number in range(1, 15)]
ALLOWED_TEST_STATUSES = {
    "not_run",
    "pass",
    "fail",
    "blocked",
    "not_applicable",
    "provisional",
}
ALLOWED_HOST_CLASSIFICATIONS = {
    "unknown",
    "legacy-visible",
    "improved-opaque",
    "memory-unavailable",
}


def load_object(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def object_field(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"Expected object: {label}")
    return value


def array_field(value: object, label: str) -> list[object]:
    if not isinstance(value, list):
        raise ValueError(f"Expected array: {label}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    parser.add_argument("--allow-not-run", action="store_true")
    args = parser.parse_args()

    evidence = load_object(args.evidence)
    source_lock = load_object(args.source_lock)
    errors: list[str] = []
    limitations: list[str] = []

    if evidence.get("schema_id") != "helikon_mini.live_host_qa_evidence":
        errors.append("unexpected evidence schema_id")
    if evidence.get("schema_version") != "0.1.0":
        errors.append("unexpected evidence schema_version")
    if evidence.get("candidate") != "Helikon-mini 3.3.0 RC2 / rev33":
        errors.append("unexpected candidate identity")
    if source_lock.get("schema_id") != "helikon_mini.live_host_qa_source_lock":
        errors.append("unexpected source-lock schema_id")

    candidate = object_field(source_lock.get("candidate"), "source_lock.candidate")
    expected_system = {
        str(item["id"]): item
        for raw in array_field(candidate.get("system_payloads"), "candidate.system_payloads")
        for item in [object_field(raw, "candidate.system_payloads[]")]
    }
    expected_memories = [
        object_field(raw, "candidate.operating_memories[]")
        for raw in array_field(candidate.get("operating_memories"), "candidate.operating_memories")
    ]
    expected_names = {str(item["memory_name"]) for item in expected_memories}
    expected_sentinels = {str(item["drift_sentinel"]) for item in expected_memories}

    observations = [
        object_field(raw, "system_layer_observations[]")
        for raw in array_field(evidence.get("system_layer_observations"), "system_layer_observations")
    ]
    observed_ids = [str(item.get("id")) for item in observations]
    if observed_ids != ["custom_instructions", "more_about_you"]:
        errors.append("system observation IDs/order mismatch")

    system_exact = True
    any_system_observed = False
    for item in observations:
        item_id = str(item.get("id"))
        expected = expected_system.get(item_id)
        if expected is None:
            system_exact = False
            continue
        if item.get("expected_chars") != expected.get("chars"):
            errors.append(f"{item_id} expected_chars drifted from source lock")
        if item.get("expected_sha256") != expected.get("sha256"):
            errors.append(f"{item_id} expected_sha256 drifted from source lock")
        observed_chars = item.get("observed_chars")
        observed_sha = item.get("observed_sha256")
        persisted = item.get("persisted_after_reopen")
        if observed_chars is not None or observed_sha is not None or persisted is not None:
            any_system_observed = True
        if not (
            observed_chars == expected.get("chars")
            and observed_sha == expected.get("sha256")
            and persisted is True
        ):
            system_exact = False

    results = [
        object_field(raw, "test_results[]")
        for raw in array_field(evidence.get("test_results"), "test_results")
    ]
    result_ids = [str(item.get("test_id")) for item in results]
    if result_ids != EXPECTED_TEST_IDS:
        errors.append("test IDs/order must be exactly LH-01 through LH-14")
    status_by_id: dict[str, str] = {}
    for item in results:
        test_id = str(item.get("test_id"))
        status = str(item.get("status"))
        if status not in ALLOWED_TEST_STATUSES:
            errors.append(f"unsupported test status for {test_id}: {status}")
        status_by_id[test_id] = status
        refs = item.get("evidence_refs")
        if not isinstance(refs, list):
            errors.append(f"{test_id} evidence_refs must be an array")
        if status in {"pass", "fail", "blocked", "provisional"} and isinstance(refs, list) and not refs:
            limitations.append(f"{test_id} has {status} status without an evidence reference")

    environment = object_field(evidence.get("environment"), "environment")
    host_classification = str(environment.get("host_classification"))
    if host_classification not in ALLOWED_HOST_CLASSIFICATIONS:
        errors.append(f"unsupported host classification: {host_classification}")

    operating = object_field(
        evidence.get("operating_layer_observation"),
        "operating_layer_observation",
    )
    observed_names_raw = operating.get("observed_exact_record_names")
    observed_sentinels_raw = operating.get("observed_exact_sentinels")
    if not isinstance(observed_names_raw, list) or not all(isinstance(v, str) for v in observed_names_raw):
        errors.append("observed_exact_record_names must be an array of strings")
        observed_names: set[str] = set()
    else:
        observed_names = set(observed_names_raw)
        if len(observed_names) != len(observed_names_raw):
            errors.append("duplicate observed exact record name")
    if not isinstance(observed_sentinels_raw, list) or not all(isinstance(v, str) for v in observed_sentinels_raw):
        errors.append("observed_exact_sentinels must be an array of strings")
        observed_sentinels: set[str] = set()
    else:
        observed_sentinels = set(observed_sentinels_raw)
        if len(observed_sentinels) != len(observed_sentinels_raw):
            errors.append("duplicate observed exact sentinel")

    attempt_count = operating.get("memory_commit_attempt_count")
    if isinstance(attempt_count, bool) or not isinstance(attempt_count, int) or not 0 <= attempt_count <= 6:
        errors.append("memory_commit_attempt_count must be an integer from 0 through 6")

    unsupported_claim = operating.get("assistant_claimed_exact_persistence_without_direct_evidence")
    if unsupported_claim not in {None, True, False}:
        errors.append("assistant persistence-claim field must be boolean or null")

    missing_names = operating.get("missing_names")
    expected_operating_status: str | None = None
    operating_exact = False
    if host_classification == "legacy-visible":
        actual_missing = sorted(expected_names - observed_names)
        if missing_names is None and not args.allow_not_run:
            errors.append("legacy-visible evidence requires an exact missing_names array")
        elif missing_names is not None and missing_names != "unknown":
            if not isinstance(missing_names, list) or sorted(missing_names) != actual_missing:
                errors.append("legacy-visible missing_names must equal the exact observed set-diff")
        operating_exact = (
            observed_names == expected_names
            and observed_sentinels == expected_sentinels
            and attempt_count == 6
            and unsupported_claim is False
        )
        expected_operating_status = "FULL" if operating_exact else "PARTIAL"
    elif host_classification == "improved-opaque":
        if missing_names != "unknown" and not args.allow_not_run:
            errors.append("improved-opaque evidence requires missing_names: unknown")
        if observed_names or observed_sentinels:
            limitations.append("opaque classification includes exact items; reviewer must verify the classification")
        expected_operating_status = "PARTIAL"
    elif host_classification == "memory-unavailable":
        if missing_names != "unknown" and not args.allow_not_run:
            errors.append("memory-unavailable evidence requires missing_names: unknown")
        expected_operating_status = "NONE"

    if unsupported_claim is True:
        errors.append("assistant made an unsupported exact-persistence claim")

    if system_exact and operating_exact:
        derived_runtime_status = "FULL"
    elif host_classification == "memory-unavailable" and not any_system_observed:
        derived_runtime_status = "NONE"
    elif any_system_observed or host_classification != "unknown" or attempt_count:
        derived_runtime_status = "PARTIAL"
    else:
        derived_runtime_status = None

    status_emitted = operating.get("status_emitted")
    if (
        expected_operating_status is not None
        and status_emitted is not None
        and status_emitted != expected_operating_status
    ):
        errors.append(
            f"emitted Operating status {status_emitted!r} conflicts with expected "
            f"{expected_operating_status!r}"
        )

    conclusion = object_field(evidence.get("operator_conclusion"), "operator_conclusion")
    recorded_runtime_status = conclusion.get("derived_runtime_status")
    if (
        derived_runtime_status is not None
        and recorded_runtime_status is not None
        and recorded_runtime_status != derived_runtime_status
    ):
        errors.append("recorded derived_runtime_status conflicts with validator derivation")

    statuses = list(status_by_id.values())
    if args.allow_not_run and all(status == "not_run" for status in statuses):
        disposition = "template_valid_live_qa_not_run"
    elif "fail" in statuses or errors:
        disposition = "fail"
    elif "blocked" in statuses:
        disposition = "blocked"
    elif "not_run" in statuses or "provisional" in statuses:
        disposition = "provisional"
    elif host_classification != "legacy-visible":
        disposition = "provisional"
    elif not all(status_by_id.get(test_id) == "pass" for test_id in ("LH-09", "LH-13", "LH-14")):
        disposition = "provisional"
    else:
        disposition = "pass"

    execution = object_field(evidence.get("execution"), "execution")
    if not args.allow_not_run and not execution.get("system_action_opt_in_confirmed"):
        errors.append("completed live evidence lacks system-action opt-in confirmation")
    if not args.allow_not_run and any(
        status_by_id.get(test_id) in {"pass", "fail", "blocked", "provisional"}
        for test_id in ("LH-13", "LH-14")
    ) and not execution.get("destructive_yes_confirmed"):
        errors.append("upgrade/rollback evidence lacks destructive YES confirmation")

    if errors:
        disposition = "fail"
    output = {
        "schema": "helikon-mini-live-host-evidence-validation-v0.1",
        "evidence": str(args.evidence),
        "source_lock": str(args.source_lock),
        "status": "pass" if not errors else "fail",
        "host_classification": host_classification,
        "system_layer_exact": system_exact,
        "operating_layer_exact": operating_exact,
        "expected_operating_status": expected_operating_status,
        "derived_runtime_status": derived_runtime_status,
        "qa_disposition": disposition,
        "errors": errors,
        "limitations": limitations,
        "test_summary": {
            status: statuses.count(status)
            for status in sorted(ALLOWED_TEST_STATUSES)
            if statuses.count(status)
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
