# Helikon-mini

Helikon-mini is a structured runtime framework for getting **more consistent and more verifiable** results from ChatGPT via:
- repeatable workflows (plan → verify → emit)
- explicit safety gates for risky/heavy actions
- disciplined outputs (clear claims, labeled uncertainty, confidence scoring)
- lightweight operator commands for predictable operation

## How it works (2-layer runtime)
Helikon-mini installs in two places:

1) **System Layer (System Kernel)**  
   Goes into ChatGPT **Personalization**:
   - Custom instructions
   - About you → More about you

2) **Operating Layer (Saved Memories)**  
   Installed as **6 Saved Memories** using in-chat operator commands.

## Install

### 1) Install the System Layer
Open: `Helikon-mini_SYSTEM_LAYER_v2.3.3_install.md`

Follow its steps to paste:
- **Snippet 1 — Custom instructions**
- **Snippet 2 — More about you**

After install, you can ask ChatGPT: `HMS` to reprint the installed snippets for a quick check.

### 2) Install the Operating Layer (6 Saved Memories)
Open: `Helikon-mini_OPERATING_LAYER_v2.3.4_install.md`

In ChatGPT, run:
- `HMO` (prints the Operating install script)
- Then loop: `INSTALL` → review payload → `REMEMBER` → `NEXT`  
  Repeat until all 6 memories are processed. After the 6th, `NEXT` emits `FINAL_VERIFY`.

## Using Helikon-mini (day-to-day)

### Operator commands
- `HMS` → print System Layer snippets (verbatim)
- `HMO` → print Operating install script (script-only)
- `INSTALL` → emit next memory payload (payload-only, wrapped)
- `REMEMBER` → attempt to commit the payload to Saved Memories (**never claims success**)
- `NEXT` → advance to next memory; after #6 emits `FINAL_VERIFY`

### Safety gates
- `HK_UNLOCK` (in the current user message) authorizes heavy/build/code/destructive actions. Otherwise Helikon-mini stays **plan-only** for those categories.
- `YES` (same-turn) authorizes deletion/overwrite actions.

### Control codes
- `DEP=1|2|3` (depth): 1=minimal, 2=default, 3=deep
- `MODE=LITE|STD|VERIFY` (verification posture):
  - LITE: no browsing/tools unless you ask
  - STD: default
  - VERIFY: prefer citations/verification for time-sensitive facts (and explicitly say if tools are unavailable)

## Quick health check
Ask ChatGPT:
- “Report Operating visibility status as FULL/PARTIAL/NONE, then list missing memory names by set-diff against EXPECTED_OPERATING_MEMORIES.”
- “What is HM_KERNEL_SENTINEL?”

## License
MIT — see `LICENSE`.
