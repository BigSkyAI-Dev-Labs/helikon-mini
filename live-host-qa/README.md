# Helikon-mini 3.3.0 RC2 Live-Host QA Operator Kit

This kit prepares—but does not execute—the separately gated live-host QA for Helikon-mini 3.3.0 RC2 / SHIP rev33.

## Contents

1. `RUNSHEET_Helikon-mini_3.3.0_RC2_live-host-qa.yaml` — canonical staged execution plan.
2. `RUNSHEET_COMPILATION_REPORT.yaml` — compatibility, readiness, authorization, and blocker report.
3. `SOURCE_LOCK.json` — exact RC2/v3.2 identities, payload hashes, sentinels, and documentation baseline.
4. `Helikon-mini_3.3.0_RC2_LIVE_HOST_QA_OPERATOR_GUIDE.md` — human test procedure and pass/fail rules.
5. `LIVE_HOST_QA_EVIDENCE_TEMPLATE.json` — copy once per host test run; never overwrite the template.
6. `LIVE_HOST_QA_REPORT_TEMPLATE.md` — human-reviewed final report template.
7. `tools/validate_qa_kit.py` — static kit/source validator.
8. `tools/validate_live_host_evidence.py` — completed-evidence validator and status derivation.
9. `tools/build_qa_kit.py` — deterministic package builder.
10. `packages/Helikon-mini_3.3.0_RC2_draft_candidate.zip` — locked rev33 distribution, included only in the packaged kit.
11. `packages/Helikon-mini_Install_Package_v3.2.0.json` — locked upgrade/rollback baseline, included only in the packaged kit.

The source tree has seven documentation/template files plus three tools. The deterministic packaged ZIP adds the two locked package inputs for a total of twelve members.

## Current state

- RUNSHEET: compiled
- Promotion assessment: `plan_ready`
- Live installation or host mutation: not authorized and not performed
- Exact disposable profiles: unresolved
- Live-host result: not run
- Release state: remains `draft_candidate`

## Static verification

From the extracted kit root:

```bash
python3 tools/validate_qa_kit.py --root .
python3 tools/validate_live_host_evidence.py \
  --evidence LIVE_HOST_QA_EVIDENCE_TEMPLATE.json \
  --source-lock SOURCE_LOCK.json \
  --allow-not-run
```

Do not run the live procedure until the Operator has named the exact disposable profiles and issued a new authorization specifically covering the intended host mutations. Upgrade and rollback replacement/deletion also require same-turn `YES`.

## Runtime boundary

This kit, its evidence, host classifications, tools, Projects, profiles, and chats are supporting QA infrastructure. Helikon-mini remains exactly two runtime layers: the Personalization System Layer and the six-record Saved Memory Operating Layer.
