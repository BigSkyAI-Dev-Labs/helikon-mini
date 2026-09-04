# Helikon-mini 3.3.0 RC2 Static QA Receipt

Date: 2026-09-04  
Candidate: Helikon-mini 3.3.0 RC2 / SHIP rev33  
Lifecycle state: `draft_candidate`  
Readiness: `provisional_live_qa_pending`

## Authorized scope

RC2 was built from the preserved RC1 source candidate. The approved scope allowed one bounded repair pass and deterministic static validation and packaging. It did not authorize installation, changes to ChatGPT Personalization or Saved Memories, GitHub mutation, publication, or promotion to a release state.

## Compatibility repair applied

- Restored `reference_saved_memories` to the legacy Boolean value `true`.
- Added `reference_saved_memories_policy: "required_if_available"` as a separate policy field.
- Restored the named v3.2 UI-route and setup-output fields with their legacy types while retaining RC1 host-aware additions.
- Restored the ten-step compatible `system_layer.operator_flow`.
- Restored the independently versioned kernel sentinel `HMK-3.0.0-REV1`.
- Preserved the entire RC1 Operating Layer structure and content exactly.
- Preserved RC1 host-memory truth rules, commands, More About You payload, and all Custom Instructions content except the intended kernel-sentinel repair.

## Bounded repair record

The single permitted repair pass was used after manual review found two documentation defects in the first static build: shipped QA commands still named RC1-local source paths, and SHIP called RC1 "rejected" without supporting evidence. RC2 now names its packaged RC1 snapshot and provenance manifest, and describes RC1 as "superseded." The first build and its validation report remain preserved under `failed_builds/prepackage-1/`.

## Final validation result

| Result | Count |
|---|---:|
| Pass | 34 |
| Fail | 0 |
| Provisional | 1 |
| Not applicable | 2 |

The two not-applicable checks are full-Helikon-only twelve-record and twelve-owner parity gates; Helikon-mini intentionally implements six compressed records. The provisional item is live-host QA: static evidence cannot establish ChatGPT persistence, exact memory retention, or runtime activation.

The final validator report is `receipts/STATIC_VALIDATION_FINAL_RC2.json`.

## Deterministic package evidence

Two independent ZIP builds were byte-identical and each reopened successfully. All eight members were path-safety checked and byte-compared against the validated release directory.

- Package: `dist/Helikon-mini_3.3.0_RC2_draft_candidate.zip`
- Bytes: `35925`
- SHA-256: `57df3d12bbf0c9b466075a7187ce781437fb74f43545a326df1e75920c8e0a3f`
- Shipped files: `8`

Detached member and package checksums are recorded in `dist/Helikon-mini_3.3.0_RC2_SHA256SUMS.txt`.

## Decision

Static build and packaging gates pass. RC2 remains a draft candidate and must not be described as installed, live-validated, published, or released. The next gate is human review followed by separately authorized live-host QA in an isolated disposable profile.

Confidence: 97/100 — deterministic static, source-preservation, compatibility, and archive evidence is complete; live host behavior remains untested.

⚠️ Provisional — static governance checks passed; live host QA remains pending.
