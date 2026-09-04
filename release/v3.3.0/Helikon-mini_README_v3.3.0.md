# Mount Helikon-mini 3.3 AIOS

**Status:** `v3.3.0 draft_candidate / RC2 / rev33`  
**License:** MIT  
**Baseline:** GitHub commit `702b6fbdf34ebf54f455075525818fff7962edb9` (v3.2.0)  
**Posture:** free, open-source starter line for ChatGPT; not a drop-in copy of the full Mount Helikon system.

## What 3.3 fixes

Helikon-mini 3.2 remained internally coherent, but its public packet was incomplete in the repository and its memory-completeness language assumed exact Saved Memory visibility. ChatGPT host behavior now varies: some surfaces expose individual saved records, while others provide synthesized or less inspectable memory. Version 3.3 keeps mini's architecture and makes the truth boundary explicit.

- One complete, versioned eight-file distribution under a canonical release directory.
- Exact JSON ↔ Markdown projection parity and deterministic packaging.
- Closing boundary restored after memory #6.
- `FULL` only when all six exact memory names and sentinels are directly verifiable.
- Synthesized, merged, incomplete, or opaque memory is `PARTIAL`, normally with `missing: unknown`.
- Current host UI labels are guidance, not runtime primitives.
- The visible answer footer is reduced to a single confidence line on substantive normal answers.

## Mini and full Helikon

| Contract | Helikon-mini 3.3 | Full Mount Helikon 5.1 compatibility target |
|---|---|---|
| Runtime layers | 2 | 2 |
| Operating records | 6 compressed `Helikon-mini.*` memories | Exact 12-pillar Operating Layer |
| Primary goal | Lightweight governance and continuity | Full governance/orchestration contract |
| Host adaptation | Conservative QA classifications | Richer runtime enforcement and exact owner map |
| Distribution | Free/open-source MIT starter | Separate full product line |

Mini borrows selected contract shapes but does not import a third layer, a thirteenth pillar, a new mode, or a second identity variable. The six mini records remain the product's stable runtime identity.

## Runtime contract

1. **System Layer:** two Personalization payloads.
2. **Operating Layer:** exactly six Saved Memory records.

Chat history is optional context. Projects are optional workspace wrappers. Neither is a runtime layer or a substitute for exact record verification.

## Host compatibility

| QA classification | Observable condition | Required mini report |
|---|---|---|
| `legacy-visible` | Exact records and sentinels can be inspected | `FULL` only if all six pass; otherwise `PARTIAL` + exact missing set |
| `improved-opaque` | Host offers synthesized/merged memory but exact records are not inspectable | `PARTIAL`; `missing: unknown` |
| `memory-unavailable` | Saved Memory capability is absent/disabled | `NONE` for Operating; do not claim install |
| `projects-optional` | Project wrapper is used | No runtime-state promotion; test ordinary chat separately |

These labels are QA vocabulary only. Host behavior and UI can change; verify against the official [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq), [Custom Instructions guide](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions), [Projects guide](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), and [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

## Install sequence

1. Read `Helikon-mini_SHIP_rev33.md` and verify all eight files.
2. Open `Helikon-mini_Install_Package_v3.3.0.json`; it is the installation SSOT.
3. In a normal non-Temporary chat, send `SETUP` and install the two System Layer payloads into separate visible Personalization fields.
4. Send `INSTALL`; then process each memory with `EXTRACT` → review → `REMEMBER` → `NEXT`.
5. Run `FINAL_VERIFY`. Do not claim `FULL` when exact records are unavailable.

No included file automatically changes ChatGPT. Installation requires an assistant with an available host mechanism and explicit operator authorization for each memory attempt.

## Upgrading from v3.2

Preserve the v3.2 packet as history. Do not overwrite live settings or memories merely because 3.3 exists. First review this RC, run static validation, then use a separate sandbox/live-QA authorization to test replacement behavior. On opaque-memory hosts, avoid blind reinstall loops because exact replacement/deduplication cannot be proven.


## RC2 compatibility repair

RC2 preserves RC1's host-memory truth rules while restoring machine-consumer compatibility. The legacy setup and UI JSON keys/types remain available as deprecated-compatible fields; `reference_saved_memories` remains Boolean `true`, while the host-aware `required_if_available` policy moves to `reference_saved_memories_policy`. The package-level release remains 3.3.0, but the unchanged mini kernel contract retains its independent `HMK-3.0.0-REV1` sentinel. SHIP advances to rev33 so corrected bytes never reuse rev32 identity.

## Distribution and QA

The distribution contains exactly the eight files named in `Helikon-mini_SHIP_rev33.md`. Engineering validators are intentionally outside the shipped eight-file ZIP. Static QA can establish package integrity and projection parity; live host persistence remains provisional until separately tested.

The optional installer GPT is not part of this RC. Treat any such GPT as experimental and non-authoritative unless its knowledge, prompts, and version pointers are synchronized and verified against this exact package.
