# Helikon-mini 3.3.0 RC2 Live-Host QA Report

Report status: `TEMPLATE — NOT EXECUTED`  
Candidate: `Helikon-mini 3.3.0 RC2 / SHIP rev33`  
Lifecycle state: `draft_candidate`

## 1. Execution identity

- Execution date/time (UTC):
- Operator:
- Reviewer:
- Evidence JSON filename:
- Evidence JSON SHA-256:
- Exact authorization text:
- Same-turn destructive `YES` text, if used:

## 2. Environment

- Profile A identifier/redacted label:
- Profile B identifier/redacted label:
- Client and version:
- Plan/workspace type:
- Region, if known:
- Visible Personalization labels:
- Visible Memory labels:
- Visible Project-memory labels:
- Host classification(s):
- Official documentation rechecked at:

## 3. Locked inputs

- RC2 distribution SHA-256:
- v3.2 baseline package SHA-256:
- Kit ZIP SHA-256:
- Source-lock validation result:

## 4. Test results

| ID | Result | Direct evidence | Limitation or failure |
|---|---|---|---|
| LH-01 |  |  |  |
| LH-02 |  |  |  |
| LH-03 |  |  |  |
| LH-04 |  |  |  |
| LH-05 |  |  |  |
| LH-06 |  |  |  |
| LH-07 |  |  |  |
| LH-08 |  |  |  |
| LH-09 |  |  |  |
| LH-10 |  |  |  |
| LH-11 |  |  |  |
| LH-12 |  |  |  |
| LH-13 |  |  |  |
| LH-14 |  |  |  |

Allowed results: `pass`, `fail`, `blocked`, `not_applicable`, or `provisional`.

## 5. System Layer evidence

| Field | Expected characters | Observed characters | Expected SHA-256 | Observed SHA-256 | Reopen persistence |
|---|---:|---:|---|---|---|
| Custom Instructions | 1495 |  | `87e05fc6b02e7c102466a787317dea74dc7af836fff3cce4bf60293eaf6614a5` |  |  |
| More About You | 1043 |  | `3de4f68df3020e3b9028c734c753b0f8c7dd93106a769ba63a095900be6e8ad3` |  |  |

## 6. Operating Layer evidence

- Memory commit attempts observed:
- Exact record names directly visible:
- Exact sentinels directly visible:
- Missing names from observable set-diff, or `unknown`:
- Assistant made unsupported exact-persistence claim: yes/no
- FINAL_VERIFY status:
- Ordinary-chat system status:

## 7. Host-truth decision

- System Layer status:
- Operating Layer status:
- Derived combined runtime status:
- Evidence basis:
- Why a higher status is not justified, if applicable:

## 8. Project comparison

- Project used:
- Default or project-only memory:
- Project instructions present:
- Ordinary-chat result:
- Project-chat result:
- Confirmation that Project behavior did not promote runtime status:

## 9. Upgrade, deduplication, and rollback

- v3.2 baseline directly verified:
- Upgrade authorized with exact target:
- Same-turn `YES` observed:
- Duplicate names after upgrade:
- Residual v3.2 sentinels after upgrade:
- Rollback attempted:
- v3.2 System hashes restored:
- Six v3.2 records/sentinels restored:
- Residual RC2 state:
- Mixed-state incident, if any:

## 10. Side-effect ledger

### Attempted

-

### Completed

-

### Not completed

-

### Unexpected

-

## 11. Failures, blockers, and limitations

-

## 12. Disposition

Select one only after evidence review:

- [ ] `pass` — all required supported-host tests passed with direct evidence.
- [ ] `fail` — at least one material behavior contradicted the rev33 contract.
- [ ] `blocked` — a prerequisite or safe mechanism prevented required testing.
- [ ] `provisional` — useful evidence exists, but host opacity or incomplete coverage prevents closure.

Release recommendation:

- [ ] Retain `draft_candidate`.
- [ ] Prepare a bounded RC3 repair plan.
- [ ] Submit evidence to the separate release-promotion gate.

Reviewer rationale:

> 

## 13. Change statement

State exactly which profiles, fields, memory records, toggles, chats, and Projects changed; which were restored; and which were intentionally retained for review. Do not imply any action lacking direct evidence.

Confidence: __/100 — complete only after evidence and human review.

⚠️ Provisional — replace this line only when the separately governed final verdict permits it.
