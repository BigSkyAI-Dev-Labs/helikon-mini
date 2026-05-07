# Mount Helikon-mini 3.2 AIOS

<p align="left">
  <img alt="Mount Helikon-mini 3.2 AIOS" src="https://img.shields.io/badge/Mount%20Helikon--mini-3.2%20AIOS-blue">
  <img alt="Line: Free Starter" src="https://img.shields.io/badge/line-Free%20Starter-2ea44f">
  <img alt="Status: draft candidate" src="https://img.shields.io/badge/status-draft%20candidate-orange">
  <img alt="Runtime: 2 layers, 6 memories" src="https://img.shields.io/badge/runtime-2%20layers%20%7C%206%20memories-purple">
  <img alt="Install: JSON SSOT" src="https://img.shields.io/badge/install-JSON%20SSOT-informational">
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green">
</p>

**Start here:** [🚀 Quickstart](#quickstart-recommended) · [🧠 Why memory matters](#why-memory-matters) · [🧩 Runtime contract](#runtime-contract) · [🛠️ Troubleshooting](#troubleshooting) · [✅ QA](#qa)

> Mount Helikon-mini 3.2 AIOS is the **Free Starter operating system line for ChatGPT**: a lightweight, memory-backed operating kit designed to make ChatGPT more consistent, more structured, and more useful for ongoing work on the current Free-account surface.

## What you get

- 🧠 **Memory-backed continuity** across ordinary chats through a compact 6-memory Operating Layer
- 🧭 **Clearer workflow discipline** through plan → verify → emit, explicit uncertainty, and visible action gates
- ⚠️ **Honest degradation** when tools, memories, or current facts are missing or uncertain
- 📦 **A small install surface** with a single JSON install package as the primary install artifact and installation SSOT
- ⛰️ **A clean upgrade path** into paid Mount Helikon 5.0 AI Assistant without turning Helikon 5.0 into mini runtime authority

**Namespace note:** shipped filenames remain in the `Helikon-mini_*` namespace and the Saved Memory IDs remain in the `Helikon-mini.*` namespace for runtime continuity in this candidate set.

## Why memory matters
Mount Helikon-mini 3.2 AIOS is intentionally **memory-backed**. The 6 Saved Memories are not an optional extra for the installed edition; they are the Operating Layer that gives mini durable continuity across ordinary chats. The public docs in this release are lighter and more benefit-first, but the runtime still depends on the same two layers:
- **System Layer** = Personalization (**Custom instructions** + **More about you**)
- **Operating Layer** = 6 Saved Memories using the `Helikon-mini.*` namespace

Chat history remains optional best-effort context only and is never a spec store.

## How mini works

| Layer | Lives in | Purpose |
|---|---|---|
| **System Layer** | Personalization | Compact account-level behavior, gates, and setup posture |
| **Operating Layer** | 6 Saved Memories | Memory-backed continuity across ordinary chats |
| **Projects** | Optional workspace wrapper | Useful for long-running work, but not required for runtime completeness |

## Runtime contract
- **Two layers only**: Personalization + Saved Memories
- **System Layer** = Personalization (**Custom instructions** + **More about you**)
- **Operating Layer** = 6 Saved Memories using the `Helikon-mini.*` namespace
- **Projects** = supported workspace wrapper for longer-running work, but not a required runtime layer
- **Plain chat** = canonical install and QA baseline
- **JSON package** = primary install artifact and installation SSOT

## Recommended workspace posture
Mini is designed to work in normal chat first. For longer-running work, Projects are recommended as a workspace wrapper because they keep related chats, files, and project instructions together. They are useful, but they are not required for runtime completeness. Project instructions can override global custom instructions, so plain chat remains the baseline surface for installation and QA.

## Quickstart (recommended)
1) In a normal **non-Temporary chat**, upload `Helikon-mini_Install_Package_v3.2.0.json`.
2) Send `SETUP`.
3) Follow the beginner-facing setup walkthrough:
   - open **Personalization**
   - turn **Reference saved memories** ON
   - paste **Snippet 1** into **Custom instructions**
   - paste **Snippet 2** into **About you → More about you**
   - save both, then reopen Personalization to confirm they persisted
4) Return to the chat and send `INSTALL`.
5) Follow the Operating Layer loop: `EXTRACT` → review payload → `REMEMBER` → `NEXT`.
6) After memory #6, send `NEXT` again and follow `FINAL_VERIFY`.

## Setup posture
`SETUP` should begin by explaining, in plain language, that **Personalization** is ChatGPT's settings/customization area, that mini uses **two different text boxes**, not one, and that **Reference saved memories** must be ON before you continue. If `SETUP` does not do that, use the System Layer projection file directly and then return to the chat for `INSTALL`.

## Runtime gates
- `APPROVE` = authorizes heavy/build/code/destructive work in the current user message
- `YES` = same-turn delete/overwrite authorization

## Hardening in v3.2.0
Mini now includes compact hardening adapted from the paid Mount Helikon 5.0 donor line but re-expressed in mini's own six-memory surfaces. It does not make 5.0 files a dependency.

The added gates help mini:
- separate user instructions from evidence, tool observations, memory digests, and assistant inference
- avoid unnecessary retrieval while requiring verification for unstable or source-dependent claims
- split important factual claims into checkable units
- abstain, qualify, retrieve, or ask when evidence is insufficient
- treat confidence as an operational signal, not an empirically calibrated probability
- keep research/tool/code retention compact and avoid raw secret-bearing traces
- protect active memory links from unsafe cleanup and avoid background-monitoring claims

## Control codes
- `DEP=1|2|3`
- `MODE=LITE|STD|VERIFY`

## After setup: how to use mini
Once installed, use ChatGPT normally. Mini should make everyday work steadier by carrying compact continuity across chats and by keeping the response posture disciplined.

Useful health checks:
- `system status`
- “Report Operating visibility status as FULL/PARTIAL/NONE. Then list missing memory names by set-diff against EXPECTED_OPERATING_MEMORIES. If the expected list is unavailable/uncertain, output `missing: unknown` and do not guess.”
- “What is HM_KERNEL_SENTINEL?”

## Projects for longer-running work
Projects are recommended when you want a dedicated workspace with files, chats, and project-specific instructions. They are not part of the formal runtime contract, but they are a good organization layer for ongoing work.

Use Projects when you want:
- a bounded workspace with related chats and files
- project-specific instructions for a single workstream
- a cleaner separation between one work area and another

Use plain chat when you want:
- baseline install verification
- runtime QA
- a clean control test when a Project behaves differently than expected

## Troubleshooting
- If **Reference saved memories** is OFF, turn it ON in Personalization before rerunning `SETUP` or `INSTALL`.
- If the assistant cannot see Saved Memories, it must report FULL/PARTIAL/NONE and proceed conservatively.
- If a stored memory lacks its `DRIFT_SENTINEL:` line, reinstall that memory.
- If tools are unavailable, the assistant should say so and proceed with labeled uncertainty or ask minimal questions.
- If `SETUP` jumps straight to the snippets without a real menu walkthrough, omits the Memory-settings step, or fails to tell you to return and send `INSTALL` after both saves are confirmed, follow the System Layer projection manually and then continue with `INSTALL`.
- If a Project behaves differently from plain chat, test the same prompt in a normal chat first; project instructions may be taking precedence.

## QA
Run `Helikon-mini_QA_PACK_v3.2.0.md` after any change.
