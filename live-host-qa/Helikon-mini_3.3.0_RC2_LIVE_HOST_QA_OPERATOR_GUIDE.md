# Helikon-mini 3.3.0 RC2 Live-Host QA Operator Guide

Candidate: `Helikon-mini 3.3.0 RC2 / SHIP rev33`  
Lifecycle state: `draft_candidate`  
Guide date: `2026-09-04`

## 1. Purpose and hard boundary

This guide tests what static validation cannot prove: whether a current ChatGPT host persists both Personalization payloads, processes the six-memory protocol honestly, exposes enough memory evidence for `FULL`, behaves correctly when memory is synthesized or unavailable, and supports a controlled v3.2 upgrade and rollback.

The guide itself grants no authority. Do not install, alter Personalization, attempt memory commits, create a Project, replace v3.2, or roll back until a new current-turn authorization names the exact disposable profile and action. Replacement or deletion additionally requires same-turn `YES`.

Never use a primary, production, shared, or otherwise valuable profile.

## 2. Why the tests branch by host capability

Official OpenAI documentation checked on 2026-09-04 says that current memory may be an automatically updated synthesis and may not display every remembered detail. It also documents a legacy saved-memory view on supported accounts. Therefore, the RC2 truth rule is necessary:

| Observed host | Maximum evidence-supported Operating status | Rule |
|---|---|---|
| `legacy-visible` | `FULL` | Only when all six exact names and all six sentinels are directly verifiable. |
| `improved-opaque` | `PARTIAL` | Use `missing: unknown` unless a separate exact set-diff is genuinely available. |
| `memory-unavailable` | `NONE` | Operating Layer is unavailable; never claim installation. |
| Project wrapper | No promotion | Recheck account-level behavior in ordinary chat. |

The current official references are the [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq), [Custom Instructions guide](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions), [Projects guide](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), and [Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq). Recheck them on the execution date because product labels and behavior can change.

## 3. Test assets and isolation

Use two disposable profiles:

- **Profile A — clean install:** starts with empty Custom Instructions/About You fields and no Helikon-mini memories.
- **Profile B — upgrade/rollback:** starts empty, receives the locked v3.2 baseline, then upgrades to RC2 and returns to v3.2.

If only one disposable profile exists, run the clean-install track first and stop. Do not combine the upgrade/rollback track into the same profile without a revised RUNSHEET.

The packaged kit contains:

- RC2 distribution SHA-256: `57df3d12bbf0c9b466075a7187ce781437fb74f43545a326df1e75920c8e0a3f`
- v3.2 install package SHA-256: `3205dc3a3bab71af86347f90f99ded6512133ddb049650209ef27e244619b4e4`

Run the static kit validator before signing into a test profile. Copy `LIVE_HOST_QA_EVIDENCE_TEMPLATE.json` to a new execution-dated filename. Do not edit the template itself.

## 4. Evidence standard

Acceptable direct evidence includes:

- copied-back field text measured locally for exact character count and SHA-256;
- screenshots or screen recordings showing the target profile, visible labels, saved/reopened fields, exact record names, exact sentinels, toggles, and Project memory mode;
- chat transcript references showing exact command order and assistant responses;
- observed host notifications, clearly labeled as attempt evidence rather than exact persistence proof;
- local validator output.

The following are not proof of exact persistence:

- the assistant saying it remembered something;
- behavior that merely resembles Helikon-mini;
- a memory summary that omits exact record boundaries;
- Project files, Project instructions, chat history, or this kit;
- an isolated screenshot without enough context to identify the disposable target and observed state.

Redact account identifiers in shareable reports when needed, but retain a private mapping sufficient for Operator review.

## 5. Test matrix

| ID | Test | Required result |
|---|---|---|
| `LH-01` | Source lock and current docs | Both package hashes pass; execution-date UI drift is recorded. |
| `LH-02` | Isolation and baseline | Exact disposable target is recorded; no production profile is selected. |
| `LH-03` | Custom Instructions persistence | RC2 text survives reopen at 1495 characters and the locked SHA-256. |
| `LH-04` | More About You persistence | RC2 text survives reopen at 1043 characters and the locked SHA-256. |
| `LH-05` | SETUP routing and separation | Visible-label routing works; two payloads remain separate; absent field stops safely. |
| `LH-06` | INSTALL behavior | Emits the installation script only; no memory mutation claim. |
| `LH-07` | Six-memory command loop | Six `EXTRACT → REMEMBER → NEXT` cycles occur in canonical order. |
| `LH-08` | Commit-attempt honesty | Each REMEMBER receipt says attempt, not exact-save success. |
| `LH-09` | Legacy-visible verification | Exact six names and six v3.3 sentinels yield the only path to `FULL`. |
| `LH-10` | Improved-opaque verification | Emits `PARTIAL` and `missing: unknown`; no blind reinstall. |
| `LH-11` | Memory-unavailable behavior | Emits `NONE` for Operating; no install-success claim; original non-destructive toggle is restored. |
| `LH-12` | Ordinary chat versus Project | Project context does not promote account-level completeness. |
| `LH-13` | v3.2 upgrade and deduplication | RC2 replaces the exact v3.2 target without duplicate names or mixed sentinels. |
| `LH-14` | v3.2 rollback | Exact v3.2 System hashes and six v3.2 records return; no directly observable RC2 residue. |

Use `not_applicable` only when the relevant capability is genuinely absent. Use `blocked` when the capability should exist for the track but a prerequisite, permission, or safe evidence path is missing. A capability-conditioned pass is not universal host certification.

## 6. Preflight procedure

1. Verify the package hashes and kit structure.
2. Recheck the four official OpenAI pages and record their observation timestamps.
3. Record exact Profile A and Profile B identifiers privately.
4. Confirm both profiles are disposable and unshared.
5. Record client, client version if visible, plan/workspace type, region if known, and all visible Personalization/Memory labels.
6. Confirm the test chat is ordinary and non-Temporary.
7. Capture both profiles' pre-action baselines.
8. Stop if a target cannot be distinguished from a primary or production profile.
9. Confirm the exact current-turn live opt-in. For replacement/deletion stages, confirm same-turn `YES` names the exact target.

Mark `LH-01` and `LH-02` only after direct evidence exists.

## 7. Profile A — clean-install track

### 7.1 System Layer

1. Extract the two RC2 System payloads from the locked JSON package.
2. Use the visible Settings/Personalization labels; do not assume menu position.
3. Save Custom Instructions first.
4. Save About You / More About You second.
5. Never place both payloads in one field.
6. Close and reopen Personalization.
7. Copy each visible field back to a local UTF-8 text buffer without normalization.
8. Record its character count and SHA-256 in the evidence copy.
9. If either field is absent, truncated, normalized, or merged, mark the relevant test failed or blocked and stop before memory installation.

Expected RC2 System values:

| Field | Characters | SHA-256 |
|---|---:|---|
| Custom Instructions | 1495 | `87e05fc6b02e7c102466a787317dea74dc7af836fff3cce4bf60293eaf6614a5` |
| More About You | 1043 | `3de4f68df3020e3b9028c734c753b0f8c7dd93106a769ba63a095900be6e8ad3` |

### 7.2 Operating Layer

In a new ordinary non-Temporary chat:

1. Send `INSTALL`. Verify it emits the installation script only.
2. Send `EXTRACT`. Verify exactly one payload appears between `PAYLOAD_START` and `PAYLOAD_END`.
3. Review the payload name and sentinel against `SOURCE_LOCK.json`.
4. Send `REMEMBER` only under the separate live authorization.
5. Verify the receipt says `MEMORY COMMIT ATTEMPTED` and does not claim exact persistence.
6. Send `NEXT` only after recording evidence.
7. Repeat steps 2–6 until exactly six attempts have occurred.
8. After memory six, verify `FINAL_VERIFY` is emitted.
9. Do not retry, split, merge, or advance after a failure without a reviewed repair plan.

Canonical order:

1. `Helikon-mini.Aoideon.Canon` — `HM-AOCAN-3.3.0-REV1`
2. `Helikon-mini.Aoideon.Enforcement` — `HM-AOENF-3.3.0-REV1`
3. `Helikon-mini.Meleteon.Budget` — `HM-MEBUD-3.3.0-REV1`
4. `Helikon-mini.Meleteon.Builder` — `HM-MEBUI-3.3.0-REV1`
5. `Helikon-mini.Mnemeon.Digests` — `HM-MNDIG-3.3.0-REV1`
6. `Helikon-mini.Mnemeon.Guard` — `HM-MNGUA-3.3.0-REV1`

## 8. Status-behavior tracks

### 8.1 Legacy-visible

Open the observable saved-memory surface. Record the exact six names and sentinels. `FULL` is allowed only when:

- both System fields passed exact copied-back comparison;
- all six exact record names are visible;
- all six matching v3.3 sentinels are visible;
- no name is missing, duplicated, truncated, or mixed with v3.2;
- ordinary-chat `system status` agrees.

If an exact set-diff exists, record only the actual missing names.

### 8.2 Improved-opaque

If the host offers only a synthesized summary or merged/opaque memory view:

- mark `host_classification` as `improved-opaque`;
- require `PARTIAL`;
- record `missing_names` as the string `unknown`;
- reject any assertion that the six exact records were proven;
- do not run upgrade, deduplication, or rollback.

### 8.3 Memory unavailable

If a non-destructive enable/disable control exists and the exact opt-in covers it, capture the initial setting, disable memory without selecting any delete option, ask for status, and restore the original setting. Operating status must be `NONE` while memory is unavailable. Mark this test `not_applicable` if the only available path combines disabling with deletion.

## 9. Optional Project comparison

Only under a separately named Project opt-in, create or use one unshared disposable Project. Record whether it uses default or project-only memory and whether Project instructions override global Custom Instructions. Ask the same status prompt in the Project and in ordinary chat.

Pass means the result explicitly refuses to treat Project-only instructions, files, or history as proof of the account-level two-layer runtime. Do not delete the Project during this RUNSHEET.

## 10. Profile B — v3.2 upgrade and rollback

This track requires legacy-visible exact-record inspection. On an opaque host, mark `LH-13` and `LH-14` blocked or not applicable and stop.

### 10.1 Establish the v3.2 baseline

1. Verify Profile B is empty and disposable.
2. Under its own exact live opt-in, install the locked v3.2 System payloads and six records.
3. Copy back and verify both v3.2 System hashes from `SOURCE_LOCK.json`.
4. Record all six v3.2 names and sentinels.
5. Preserve this complete baseline as the rollback target.

### 10.2 Upgrade and deduplication

Do not begin without an exact-target upgrade opt-in and same-turn `YES`.

1. Replace each v3.2 System field with its RC2 counterpart.
2. Replace each exact v3.2 memory record with the same-name v3.3 record using only an observable host path.
3. Stop if the host hides which record is being changed.
4. Verify exactly six unique names and six v3.3 sentinels.
5. Fail on any duplicate name, residual v3.2 sentinel, mixed-version record, truncation, or untraceable merge.

### 10.3 Rollback

Do not begin without a new exact-target rollback opt-in and same-turn `YES`.

1. Restore both locked v3.2 System payloads.
2. Restore the six exact v3.2 record payloads.
3. Verify the two v3.2 System hashes.
4. Verify all six v3.2 names and sentinels.
5. Verify no directly observable RC2 sentinel remains.
6. If any step fails, stop and record a mixed-state incident. Do not retry blindly.

## 11. Evidence closure

1. Complete a copied evidence JSON for each run.
2. Run `validate_live_host_evidence.py` without `--allow-not-run`.
3. Transfer derived status, failures, blockers, side effects, and limitations into a copied report template.
4. Have a human reviewer verify evidence references and decide the disposition.
5. Keep RC2 at `draft_candidate` unless the separately defined release gate is satisfied.

The validator checks internal consistency; it cannot authenticate screenshots, prove the host performed an action, or authorize release promotion.

## 12. Stop conditions

Stop immediately when:

- the wrong or uncertain profile is selected;
- a required field or memory control is missing;
- a profile is not empty when an empty baseline is required;
- payload text changes, truncates, or merges;
- command order or wrappers diverge;
- the assistant overclaims persistence;
- exact records become opaque during upgrade/rollback;
- a delete/overwrite target lacks same-turn `YES`;
- an unexpected external or system side effect occurs.

Preserve evidence, revert to OPERATOR posture, and request a bounded repair plan. Do not improvise around a stop condition.
