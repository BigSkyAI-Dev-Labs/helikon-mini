# Helikon-mini v3.0.5

Helikon-mini 3.0 is the **public Free Starter** for the Helikon family: compact, deterministic, installer-first, and designed to fit the current ChatGPT free-account surface without depending on chat history.

## What Helikon-mini is
- A **separate product line**
- A **2-layer runtime**
- A **6-memory starter operating layer**
- A **JSON-first install package**
- A clean upgrade path into paid Helikon 5.0

## Runtime contract
- **System Layer** = Personalization (**Custom instructions** + **More about you**)
- **Operating Layer** = 6 Helikon-mini Saved Memories
- **Chat history** = optional best-effort context only; never a spec store
- **Projects** = optional booster mode only; not a required runtime layer

## Primary install artifact
- `Helikon-mini_Install_Package_v3.0.5.json`

This JSON package is the **primary install artifact** and **installation SSOT**.

## Fallback projections
- `Helikon-mini_SYSTEM_LAYER_v3.0.0_install.md`
- `Helikon-mini_OPERATING_LAYER_v3.0.5_install.md`

These remain synchronized human-readable projections / fallbacks.

## Install (recommended)
1) Upload `Helikon-mini_Install_Package_v3.0.5.json`
2) Send `SETUP`
3) Paste the two System Layer snippets into Personalization
4) Send `INSTALL`
5) Follow the loop: `EXTRACT` → review payload → `REMEMBER` → `NEXT`
6) After memory #6, send `NEXT` again and follow `FINAL_VERIFY`

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
Projects are supported as an optional long-running-work mode, but they are **not** part of Helikon-mini’s runtime contract.
- Use plain chat as the canonical install and QA baseline.
- Use projects when you want a dedicated workspace with files, chats, and project-specific instructions.
- Important: project instructions can override global custom instructions, so project mode is a supported wrapper, not the baseline runtime surface.

## Troubleshooting
- If the assistant can’t see Saved Memories, it must report FULL/PARTIAL/NONE and proceed conservatively.
- If a stored memory lacks its `DRIFT_SENTINEL:` line, reinstall that memory.
- If tools are unavailable, the assistant should say so and proceed with labeled uncertainty or ask minimal questions.
- If a project behaves differently from plain chat, test the same prompt in a normal chat first; project instructions may be taking precedence.

## QA
Run `Helikon-mini_QA_PACK_v3.0.5.md` after any change.
