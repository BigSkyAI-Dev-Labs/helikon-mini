# Mount Helikon-mini 3.3.0 AIOS

<p align="left">
  <img alt="Mount Helikon-mini 3.3.0 AIOS" src="https://img.shields.io/badge/Mount%20Helikon--mini-3.3.0%20AIOS-blue">
  <img alt="Release: v3.3.0 rev34" src="https://img.shields.io/badge/release-v3.3.0%20%7C%20rev34-2ea44f">
  <img alt="Line: Free and open source" src="https://img.shields.io/badge/line-free%20%26%20open--source-2ea44f">
  <img alt="Runtime: 2 layers and 6 memories" src="https://img.shields.io/badge/runtime-2%20layers%20%7C%206%20memories-purple">
  <a href="https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/actions/workflows/helikon-mini-release-ci.yml"><img alt="Helikon-mini release validation" src="https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/actions/workflows/helikon-mini-release-ci.yml/badge.svg"></a>
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green">
</p>

> [!IMPORTANT]
> **Current public release:** `v3.3.0 / rev34`. The eight-file package passes deterministic static validation and is published as a tagged GitHub Release. Live-host installation and behavioral QA have not been executed; do not treat static validation as proof of installation.

**Start here:** [Install package](release/v3.3.0/Helikon-mini_Install_Package_v3.3.0.json) · [Release guide](release/v3.3.0/Helikon-mini_README_v3.3.0.md) · [SHIP manifest](release/v3.3.0/Helikon-mini_SHIP_rev34.md) · [QA pack](release/v3.3.0/Helikon-mini_QA_PACK_v3.3.0.md) · [Changelog](release/v3.3.0/Helikon-mini_CHANGELOG_v3.3.0.md)

Mount Helikon-mini is the free, open-source starter line of Mount Helikon: a lightweight operating system for ChatGPT that adds structured workflow discipline, memory-backed continuity, honest uncertainty, and explicit action gates without importing the full Helikon runtime.

## What 3.3 changes

Helikon-mini 3.2 remained internally coherent, but its public repository packet was incomplete and its memory-completeness language assumed exact Saved Memory visibility. ChatGPT host behavior now varies: some surfaces expose individual saved records, while others provide synthesized or less inspectable memory. Version 3.3 preserves mini's architecture while making that truth boundary explicit.

- Provides one complete, versioned eight-file release under [`release/v3.3.0/`](release/v3.3.0/).
- Enforces exact JSON-to-Markdown projection parity and deterministic packaging.
- Restores the closing installation boundary after memory #6.
- Permits `FULL` only when all six exact memory names and sentinels are directly verifiable.
- Reports synthesized, merged, incomplete, or opaque memory as `PARTIAL`, normally with `missing: unknown`.
- Treats current host UI labels as guidance rather than runtime primitives.
- Reduces the visible answer footer to one confidence line on substantive normal answers.
- Adds repeatable GitHub Actions validation for source checksums and ephemeral packages.

See the [complete 3.3 changelog](release/v3.3.0/Helikon-mini_CHANGELOG_v3.3.0.md) for the detailed RC1 and RC2 history.

## Mini and full Helikon

| Contract | Helikon-mini 3.3 | Full Mount Helikon 5.1 compatibility target |
|---|---|---|
| Runtime layers | 2 | 2 |
| Operating records | 6 compressed `Helikon-mini.*` memories | Exact 12-pillar Operating Layer |
| Primary goal | Lightweight governance and continuity | Full governance and orchestration contract |
| Host adaptation | Conservative QA classifications | Richer runtime enforcement and exact owner map |
| Distribution | Free and open-source MIT starter | Separate full product line |

Mini borrows selected contract shapes but does not import a third layer, a thirteenth pillar, a new mode, or a second identity variable. Its six mini records remain the product's stable runtime identity.

## Runtime contract

Helikon-mini has exactly two runtime layers:

1. **System Layer:** two Personalization payloads—Custom Instructions and More About You.
2. **Operating Layer:** exactly six Saved Memory records in the `Helikon-mini.*` namespace.

Chat history is optional context. Projects are optional workspace wrappers. Models, apps, files, Skills, tools, and connectors are support surfaces. None of these is an additional runtime layer.

## What is included

The v3.3.0 release contains exactly eight release files:

| Artifact | Purpose |
|---|---|
| [`Helikon-mini_Install_Package_v3.3.0.json`](release/v3.3.0/Helikon-mini_Install_Package_v3.3.0.json) | Installation source of truth |
| [`Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md`](release/v3.3.0/Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md) | Human-readable System Layer projection |
| [`Helikon-mini_OPERATING_LAYER_v3.3.0_install.md`](release/v3.3.0/Helikon-mini_OPERATING_LAYER_v3.3.0_install.md) | Human-readable six-memory projection |
| [`Helikon-mini_QA_PACK_v3.3.0.md`](release/v3.3.0/Helikon-mini_QA_PACK_v3.3.0.md) | Static and behavioral QA procedure |
| [`Helikon-mini_README_v3.3.0.md`](release/v3.3.0/Helikon-mini_README_v3.3.0.md) | Release guide |
| [`Helikon-mini_CHANGELOG_v3.3.0.md`](release/v3.3.0/Helikon-mini_CHANGELOG_v3.3.0.md) | Version and repair history |
| [`Helikon-mini_SHIP_rev34.md`](release/v3.3.0/Helikon-mini_SHIP_rev34.md) | Eight-file inventory and integrity manifest |
| [`Helikon-mini_LICENSE.md`](release/v3.3.0/Helikon-mini_LICENSE.md) | MIT license copy |

Engineering validators, source provenance, receipts, and live-host QA materials remain outside the eight-file distribution.

## Install sequence

> [!CAUTION]
> No repository file automatically changes ChatGPT. Review the release before installing it, and do not overwrite live settings or memories merely because 3.3 exists.

1. Read the [`rev34` SHIP manifest](release/v3.3.0/Helikon-mini_SHIP_rev34.md) and verify the eight-file family.
2. Open [`Helikon-mini_Install_Package_v3.3.0.json`](release/v3.3.0/Helikon-mini_Install_Package_v3.3.0.json); it is the installation source of truth.
3. In a normal, non-Temporary chat, send `SETUP` and install the two System Layer payloads into their separate Personalization fields.
4. Send `INSTALL`; process each memory with `EXTRACT` → review → `REMEMBER` → `NEXT`.
5. Run `FINAL_VERIFY`. Do not claim `FULL` when exact records cannot be verified.
6. Run the [`v3.3.0` QA pack](release/v3.3.0/Helikon-mini_QA_PACK_v3.3.0.md).

The optional Helikon-mini Installer GPT is not part of this release. Treat any installer GPT as experimental and non-authoritative unless it has been synchronized and verified against this exact package.

## Host compatibility

| QA classification | Observable condition | Required mini report |
|---|---|---|
| `legacy-visible` | Exact records and sentinels can be inspected | `FULL` only if all six pass; otherwise `PARTIAL` plus the exact missing set |
| `improved-opaque` | The host provides synthesized or merged memory but exact records are not inspectable | `PARTIAL`; `missing: unknown` |
| `memory-unavailable` | Saved Memory capability is absent or disabled | `NONE` for Operating; do not claim installation |
| `projects-optional` | A Project wrapper is used | Do not promote it into runtime state; test ordinary chat separately |

Host behavior and interface labels can change. Verify them against the official [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq), [Custom Instructions guide](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions), [Projects guide](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), and [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

## Validation status

| Check | Current result |
|---|---|
| Repository checksum manifest | Pass |
| Static release validator | 34 pass, 0 fail, 1 provisional live-host check, 2 not applicable |
| Deterministic v3.3.0 archive parity | Pass |
| Live ChatGPT persistence and behavior | Pending |

The [GitHub Actions workflow](.github/workflows/helikon-mini-release-ci.yml) rebuilds and validates a temporary archive without committing or publishing binaries. Historical candidate paths and local-only `dist/` references are explained in the [repository evidence guide](governance/README.md).

## Previous v3.2 baseline

Helikon-mini 3.2 remains preserved byte-for-byte under [`release/v3.2.0/`](release/v3.2.0/) for comparison and controlled upgrade work:

- [`Helikon-mini_Install_Package_v3.2.0.json`](release/v3.2.0/Helikon-mini_Install_Package_v3.2.0.json)
- [`Helikon-mini_SYSTEM_LAYER_v3.2.0_install.md`](release/v3.2.0/Helikon-mini_SYSTEM_LAYER_v3.2.0_install.md)
- [`Helikon-mini_OPERATING_LAYER_v3.2.0_install.md`](release/v3.2.0/Helikon-mini_OPERATING_LAYER_v3.2.0_install.md)
- [`Helikon-mini_QA_PACK_v3.2.0.md`](release/v3.2.0/Helikon-mini_QA_PACK_v3.2.0.md)
- [`Helikon-mini_CHANGELOG_v3.2.0.md`](release/v3.2.0/Helikon-mini_CHANGELOG_v3.2.0.md)
- [`Helikon-mini_SHIP_rev31.md`](release/v3.2.0/Helikon-mini_SHIP_rev31.md)

Upgrades should be reviewed and tested deliberately. On opaque-memory hosts, avoid blind reinstall loops because exact replacement or deduplication cannot be proven.

## License and status

Helikon-mini is distributed under the [MIT License](LICENSE). Version 3.3.0 / rev34 is the current public release.
