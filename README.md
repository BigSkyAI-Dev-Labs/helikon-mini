# Mount Helikon Mini 3.0 AIOS (v3.0.12)

Mount Helikon Mini 3.0 AIOS is the **Free Starter operating system line for ChatGPT**: compact, deterministic, installer-first, and designed to fit the current ChatGPT free-account surface without depending on chat history.

## What Mount Helikon Mini 3.0 AIOS is
- A **separate product line**
- A **2-layer runtime**
- A **6-memory starter operating layer**
- A **JSON-first install package**
- A clean upgrade path into paid Helikon 5.0

**Namespace note:** shipped filenames remain in the `Helikon-mini_*` namespace and the Saved Memory IDs remain in the `Helikon-mini.*` namespace for runtime continuity in this candidate set.

## Runtime contract
- **System Layer** = Personalization (**Custom instructions** + **More about you**)
- **Operating Layer** = 6 Saved Memories using the `Helikon-mini.*` namespace
- **Chat history** = optional best-effort context only; never a spec store
- **Projects** = optional booster mode only; not a required runtime layer

## Primary install artifact
- `Helikon-mini_Install_Package_v3.0.12.json`

This JSON package is the **primary install artifact** and **installation SSOT**.

## Fallback projections
- `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md`
- `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md`

These remain synchronized human-readable projections / fallbacks.

## Install (recommended)
1) In a normal **non-Temporary chat**, upload `Helikon-mini_Install_Package_v3.0.12.json`
2) Send `SETUP`
3) `SETUP` should begin by explaining that **Personalization** is ChatGPT’s settings/customization area, that Mount Helikon Mini 3.0 AIOS uses **two different boxes**, not one, that you should check the Memory settings in Personalization before pasting the snippets, and that after both saves are confirmed you should return to the chat and send `INSTALL`. If it does not, use the manual path below.
4) Open your **profile/avatar/name menu** in ChatGPT. Depending on the client, you will usually see one of these routes:
   - **Personalization**
   - **Settings → Personalization**
5) In **Personalization**, turn **Reference saved memories** ON before continuing. If your client also shows **Reference chat history**, it is optional best-effort only and is **not** required for Mount Helikon Mini 3.0 AIOS runtime completeness.
6) Inside **Personalization**, do **not** paste both snippets into the same field. You are looking for two different boxes, not one:
   - **Custom instructions**
   - **About you → More about you**
7) Paste/save in this exact order:
   - Open **Custom instructions**, paste **Snippet 1**, then click **Save**
   - Return to **Personalization**, open **About you → More about you**, paste **Snippet 2**, then click **Save**
8) Close and reopen Settings/Personalization to confirm both blocks persisted
9) Return to this chat and send `INSTALL`
10) Follow the loop: `EXTRACT` → review payload → `REMEMBER` → `NEXT`
11) After memory #6, send `NEXT` again and follow `FINAL_VERIFY`

## Runtime gates
- `APPROVE` = authorizes heavy/build/code/destructive work in the current user message
- `YES` = same-turn delete/overwrite authorization

## Control codes
- `DEP=1|2|3`
- `MODE=LITE|STD|VERIFY`

## Quick health check
Ask:
- `system status`
- “Report Operating visibility status as FULL/PARTIAL/NONE. Then list missing memory names by set-diff against EXPECTED_OPERATING_MEMORIES. If the expected list is unavailable/uncertain, output `missing: unknown` and do not guess.”
- “What is HM_KERNEL_SENTINEL?”

## Optional Projects booster mode
Projects are supported as an optional long-running-work mode, but they are **not** part of Mount Helikon Mini 3.0 AIOS’s runtime contract.
- Use plain chat as the canonical install and QA baseline.
- Use projects when you want a dedicated workspace with files, chats, and project-specific instructions.
- Important: project instructions can override global custom instructions, so project mode is a supported wrapper, not the baseline runtime surface.

## Troubleshooting
- If **Reference saved memories** is OFF, turn it ON in Personalization before rerunning `SETUP` or `INSTALL`.
- If the assistant can’t see Saved Memories, it must report FULL/PARTIAL/NONE and proceed conservatively.
- If a stored memory lacks its `DRIFT_SENTINEL:` line, reinstall that memory.
- If tools are unavailable, the assistant should say so and proceed with labeled uncertainty or ask minimal questions.
- If `SETUP` jumps straight to the snippets without a real menu walkthrough, omits the Memory-settings step, or fails to tell you to return and send `INSTALL` after both saves are confirmed, follow the install steps above manually, then continue with `INSTALL`.
- If a project behaves differently from plain chat, test the same prompt in a normal chat first; project instructions may be taking precedence.

## QA
Run `Helikon-mini_QA_PACK_v3.0.12.md` after any change.
