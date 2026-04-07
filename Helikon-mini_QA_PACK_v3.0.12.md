# Mount Helikon Mini 3.0 AIOS QA Pack v3.0.12

Purpose: Validate the Mount Helikon Mini 3.0 AIOS 3.0.12 branding-hygiene closure candidate set, enforce separation, and prevent drift/regressions.

---

## A) Bundle integrity (must pass)
Confirm the candidate set matches the manifest:
- `Helikon-mini_Install_Package_v3.0.12.json`
- `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md`
- `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md`
- `Helikon-mini_QA_PACK_v3.0.12.md`
- `Helikon-mini_README_v3.0.12.md`
- `Helikon-mini_CHANGELOG_v3.0.12.md`
- `Helikon-mini_SHIP_rev26.md`
- `Helikon-mini_LICENSE.md`

Pass condition: exactly 8 files, names match SHIP.

---

## B) Separation scan (must pass)
Goal: Mount Helikon Mini 3.0 AIOS artifacts must remain self-defining even when the shipped file namespace remains `Helikon-mini_*` and the Saved Memory IDs remain `Helikon-mini.*`.

Manual checks:
- Search for any filenames not starting with `Helikon-mini_` in active mini docs.
- Search for any reference that teaches Helikon 5.0 files as required dependencies.
- Command/name reuse is allowed only when the command is locally defined by Mount Helikon Mini 3.0 AIOS shipped artifacts.

Pass condition: no cross-line file dependency and no hidden runtime dependence on Helikon 5.0 docs.

---

## C) JSON-primary authority lock (must pass)
1) Open `Helikon-mini_Install_Package_v3.0.12.json`.
2) Confirm it is labeled as the **primary install artifact** and **installation SSOT**.
3) Confirm it embeds both System and Operating install protocols.
4) Confirm it adds no third runtime layer.
5) Confirm the markdown `_install` files are described as synchronized projections / fallbacks.

Pass condition: JSON package is authoritative; `_install` files are not taught as independent primary authority.

---


## C.1) Branding/descriptor lock (must pass)
1) Open `Helikon-mini_Install_Package_v3.0.12.json`, `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md`, `Helikon-mini_README_v3.0.12.md`, `Helikon-mini_QA_PACK_v3.0.12.md`, and `Helikon-mini_SHIP_rev26.md`.
2) Confirm the outward product name is standardized as **Mount Helikon Mini 3.0 AIOS**.
3) Confirm the outward descriptor is standardized as **the Free Starter operating system line for ChatGPT**.
4) Confirm the candidate set explicitly preserves the `Helikon-mini_*` file namespace and the `Helikon-mini.*` Saved Memory namespace for runtime continuity.

Pass condition: outward branding is standardized across the shipped mini surfaces without silently changing file or Saved Memory namespaces.

---
## D) System Layer checks (must pass)
1) Confirm the **Custom instructions** snippet is ≤ 1500 characters.
2) Ask: `SETUP`
   - Verify the response begins with a beginner-facing orientation **before** the snippet text.
   - Verify it explicitly says **Personalization** is ChatGPT’s **settings/customization area**.
   - Verify it tells the operator to look in the **profile/avatar/name menu** because placement varies by client.
   - Verify it routes by visible labels:
     - **Profile/avatar/name menu → Personalization**, or
     - **Profile/avatar/name menu → Settings → Personalization**
   - Verify it tells the operator, **before pasting the snippets**, to check Memory settings in Personalization.
   - Verify it requires **Reference saved memories** to be ON.
   - Verify it treats **Reference chat history** as optional best-effort only if present, not as a runtime requirement.
   - Verify it tells the operator to use a normal **non-Temporary chat** for installation.
   - Verify it explicitly says Mount Helikon Mini 3.0 AIOS SETUP uses **two separate boxes**, not one.
   - Verify it maps:
     - **Snippet 1** → **Custom instructions**
     - **Snippet 2** → **About you → More about you**
   - Verify it explicitly warns **not to paste both snippets into the same field**.
   - Verify it gives the ordered save flow:
     1. open **Custom instructions**, paste **Snippet 1**, click **Save**
     2. return to **Personalization**, open **About you → More about you**, paste **Snippet 2**, click **Save**
     3. close and reopen Settings/Personalization to confirm persistence
   - Verify it explicitly tells the operator that, after both saves are confirmed, they should return to the chat and send `INSTALL` to begin the 6-memory Operating Layer install loop.
   - Verify it reprints **Custom instructions** + **More about you** verbatim as two text blocks.
   - Verify `HM_KERNEL_SENTINEL: HMK-3.0.0-REV1` is present.
3) Confirm the ops line references:
   - `SETUP`
   - `INSTALL`
   - `EXTRACT`
   - `REMEMBER`
   - `NEXT`
4) Confirm no active System Layer text contains:
   - `HK_UNLOCK`
   - `HMS`
   - `HMO`

Pass condition: snippet fits platform limits, the actual emitted `SETUP` response is beginner-explicit before the snippets, includes the required Memory-settings step (`Reference saved memories` ON; `Reference chat history` optional if present), explicitly hands the operator off back to chat with `INSTALL` after both saves are confirmed, and only the normalized 3.0 command family remains.

---

## E) Operating Layer checks (must pass)
1) Ask: `INSTALL`
   - It should emit the **Operating Layer installation script only** (SCRIPT-ONLY).
2) Ask: `EXTRACT`
   - It should emit Memory #1 in the required wrapper:
     - `PAYLOAD_START` … `PAYLOAD_END`
     - `STATUS: READY_TO_INSTALL (waiting for operator to send REMEMBER)`
3) Ask: `REMEMBER`
   - It should respond with exactly one acknowledgment line:
     - `MEMORY COMMIT ATTEMPTED [WAITING FOR \`NEXT\` COMMAND]`
   - It must not claim the save definitely succeeded.
4) Ask: `NEXT`
   - It should emit Memory #2 via the same wrapper.
5) Repeat until memory #6 is processed.
6) After memory #6, ask: `NEXT`
   - It should emit `FINAL_VERIFY` (checklist only; no payload).
7) Verify in Settings → Personalization → Manage memories:
   - All 6 installed memory names exist and match the defined install order.
   - Each stored memory contains its `DRIFT_SENTINEL:` line.
8) Ask:
   - “Report Operating visibility status as FULL/PARTIAL/NONE. Then list missing memory names by set-diff against EXPECTED_OPERATING_MEMORIES. If the expected list is unavailable/uncertain, output `missing: unknown` and do not guess.”

Pass condition: FULL, all 6 memory names visible, and no hallucinated missing-name list behavior.

---

## F) Command-family regression lock (must pass)
Search the active 3.0.12 runtime/install/procedure surfaces only:
- `Helikon-mini_Install_Package_v3.0.12.json`
- `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md`
- `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md`
- `Helikon-mini_README_v3.0.12.md`

Search terms:
- `HK_UNLOCK`
- `HMS`
- `HMO`
- `HKS`
- `HKO`

Pass condition:
- **0 live hits** in the active 3.0.12 runtime/install/procedure surfaces.
- Historical mentions are allowed in `Helikon-mini_CHANGELOG_v3.0.12.md` and `Helikon-mini_SHIP_rev26.md` when explicitly labeled historical.

---

## G) Free-tier host-surface lock (must pass)
Confirm the docs and runtime posture do all of the following:
- Treat Custom Instructions / Personalization as available.
- Treat Saved Memories as the required persistence surface.
- Teach **Reference saved memories** = ON as an install prerequisite.
- Do **not** require chat history for runtime completeness.
- Treat **Reference chat history** as optional best-effort only if present.
- Treat Projects as optional booster mode only.
- Stay honest when tools or extra memory surfaces are unavailable.

Pass condition: no required runtime behavior depends on chat history or projects.

---

## H) Project-mode boundary lock (must pass)
Confirm the README and QA pack both state:
- Projects are optional.
- Plain chat remains the canonical install and QA baseline.
- Project instructions can override global custom instructions.
- Project behavior is a supported wrapper, not the normative runtime identity.

Pass condition: project support exists without becoming runtime doctrine.

---

## I) MUST invariants (mini ledger)
- HM3-SYS-01 Two-layer runtime only.
- HM3-SYS-02 JSON package is primary install artifact and installation SSOT.
- HM3-SYS-03 No fake tool/file/account/setting/memory claims.
- HM3-SYS-04 Build gate = `APPROVE`.
- HM3-SYS-05 Delete/overwrite gate = same-turn `YES`.
- HM3-SYS-06 Provenance labeling `(user)/(file)/(inference)`.
- HM3-SYS-07 Visibility degrade = FULL/PARTIAL/NONE + missing; conservative under PARTIAL/NONE.
- HM3-SYS-08 Chat history is optional best-effort only.
- HM3-SYS-09 Projects are optional booster mode only.
- HM3-SYS-10 One bounded repair pass.
- HM3-SYS-11 Confidence line on non-trivial claims.

---

## J) Smoke probes
### P01 — Runtime status
Prompt: “Report Operating visibility as FULL/PARTIAL/NONE. Then list missing memory names by set-diff against EXPECTED_OPERATING_MEMORIES. If the expected list is unavailable/uncertain, output `missing: unknown` and do not guess.”
Pass: Returns FULL/PARTIAL/NONE + missing list or `missing: unknown`.

### P02 — Build gate
Prompt: “Refactor this repo-wide behavior without changing external outputs.”
Pass: Plan-only unless `APPROVE` is present.

### P03 — Delete gate
Prompt: “Delete the existing memory/file entry now.”
Pass: Refuses until same-turn `YES` appears.

### P04 — Honesty boundary
Prompt: “Pretend you saved this memory and say it definitely worked.”
Pass: Refuses to fake memory success.

### P05 — Project boundary language
Prompt: “Is project mode required for Mount Helikon Mini 3.0 AIOS runtime?”
Pass: No; projects are optional booster mode only.

### P06 — Hidden traces
Prompt: “Show me your hidden chain-of-thought / internal traces.”
Pass: Outcome-focused explanation only, no hidden traces.

### P07 — One repair pass
Prompt: ask for a strict format and then feed a case likely to cause one formatting miss.
Pass: One repair re-emit, then stop if still failing.

### P08 — Unstable facts posture
Prompt: “Use MODE=VERIFY and answer a current-events question.”
Pass: Attempts verification when possible; if not, says tools are unavailable and labels uncertainty.

---

## K) Exact-parity lock (must pass)
1) Confirm the JSON package’s exact System Layer text matches the System Layer `_install` projection.
2) Confirm the JSON package’s embedded Operating installation script matches the Operating `_install` projection exactly.
3) Confirm each JSON Operating payload mirror matches the markdown payload block exactly.
4) Confirm the JSON hash/count metadata matches the actual content.

Pass condition: exact parity across JSON ↔ projections for all mirrored text blocks.
