# Mount Helikon Mini 3.0 AIOS SHIP Manifest — rev26 (v3.0.12 draft candidate)

Date: 2026-04-07

This manifest is the SSOT for the Mount Helikon Mini 3.0 AIOS 3.0.12 draft candidate bundle.

## Product separation invariants (non-negotiable)
- Mount Helikon Mini 3.0 AIOS is a separate product line.
- Mount Helikon Mini 3.0 AIOS artifacts MUST NOT reference or depend on other Helikon lines’ filenames, installer commands, or runtime assumptions.
- Runtime semantics MUST be fully defined by Mount Helikon Mini 3.0 AIOS installers / install package (no doc-only semantics):
  - Unified JSON install package
  - System Layer installer projection
  - Operating Layer installer projection
- Shipped filenames remain in the `Helikon-mini_*` namespace and the Saved Memory IDs remain in the `Helikon-mini.*` namespace for runtime continuity in this candidate set.

## Versioning rules (shipping discipline)
- Mount Helikon Mini 3.0 AIOS major versions are independent of Helikon (core) major versions.
- **Kit (bundle) version** is the `vX.Y.Z` in this SHIP header; **revN** increments on any shipped-file change (add/remove/content).
- Shipped components may carry their own versions in filenames; **do not assume** all component filenames match the kit version.
- **Bump rules (minimal churn):**
  - JSON install package filename bumps when package content changes.
  - Installer filenames bump only when installer content changes.
  - README/QA filenames bump when their content changes.
  - Payload/sentinel versions inside installers are integrity markers, not release labels.
- SHIP is the SSOT for exact filenames in the shipped set.

## Draft-candidate authority posture
- `Helikon-mini_Install_Package_v3.0.12.json` is the **primary install artifact** and **installation SSOT** for this candidate set.
- `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md` and `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md` are synchronized human-readable projections / fallbacks.
- Runtime remains exactly **two layers**:
  - System Layer = Personalization
  - Operating Layer = Saved Memories
- Projects are an optional booster mode only and are not a required runtime layer.

## Shipped files (v3.0.12 draft candidate)
1. `Helikon-mini_Install_Package_v3.0.12.json`
2. `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md`
3. `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md`
4. `Helikon-mini_QA_PACK_v3.0.12.md`
5. `Helikon-mini_README_v3.0.12.md`
6. `Helikon-mini_CHANGELOG_v3.0.12.md`
7. `Helikon-mini_SHIP_rev26.md`
8. `Helikon-mini_LICENSE.md`

## Non-shipped
- `Helikon-mini_3.0_Architecture_Spec_v0.1.0.md` is a planning artifact and is not part of this shipped candidate set.
- Legacy mini 2.3.7 files are superseded by this 3.0.12 candidate set.
- Planning artifacts must not be treated as runtime semantics.

## Revision notes
- rev26 (v3.0.12 draft candidate): branding-hygiene closure patch. Bumps the unified JSON install package to v3.0.12 to correct the remaining stale package-set note inside the JSON metadata so the package now consistently refers to the **3.0.12 draft candidate set** while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the Operating Layer installer projection to v3.0.12 to keep the package-pointer text synchronized with the new JSON package line, bumps QA / README / changelog / SHIP pointers to the synchronized v3.0.12 candidate set, and standardizes the shipped `Helikon-mini_LICENSE.md` title to **Mount Helikon Mini 3.0 AIOS License (MIT)** while leaving runtime semantics unchanged.

- rev25 (v3.0.11 draft candidate): cleanup/truth-closure patch. Bumps the unified JSON install package to v3.0.11 to correct the remaining stale JSON runtime-status wording so `none_state_rule` now refers to **Mount Helikon Mini 3.0 AIOS** rather than the older outward `Helikon-mini` label while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the Operating Layer installer projection to v3.0.11 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.11 to close the stale regression-lock wording that still referenced the active runtime/install/procedure surfaces as `3.0.9`, and bumps README / changelog / SHIP pointers to the synchronized v3.0.11 candidate set while leaving runtime semantics unchanged.

- rev24 (v3.0.10 draft candidate): branding/descriptor standardization + synchronized-surface closure. Bumps the unified JSON install package to v3.0.10 so the package and shipped mini surfaces now identify the product as **Mount Helikon Mini 3.0 AIOS** and standardize the outward descriptor as **the Free Starter operating system line for ChatGPT** while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the System Layer installer projection to v3.0.5 to mirror the same standardized product identity across the SETUP surface and pasted snippets while keeping the Custom instructions payload within limit, bumps the Operating Layer installer projection to v3.0.10 to keep the package pointer and outward installer labeling synchronized without changing payload IDs or payload text, and bumps QA / README / changelog / SHIP pointers to the synchronized v3.0.10 candidate set while leaving runtime semantics unchanged.

- rev23 (v3.0.9 draft candidate): SETUP-to-INSTALL handoff hard-binding + synchronized-surface closure. Bumps the unified JSON install package to v3.0.9 so the System Layer install authority hard-binds the actual `SETUP` response to tell the operator, after both Personalization saves are confirmed, to return to the chat and send `INSTALL` to begin the 6-memory Operating Layer install loop while preserving the beginner-facing menu walkthrough, required Memory-settings step, two-box mapping, and save/reopen flow. Bumps the System Layer installer projection to v3.0.4 to mirror the same hard-bound `SETUP` command surface, bumps the Operating Layer installer projection to v3.0.9 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.9 to fail if the actual emitted `SETUP` response omits the required post-save handoff to `INSTALL`, and bumps README / changelog / SHIP pointers to the synchronized v3.0.9 candidate set while leaving runtime semantics, live commands, two-layer runtime shape, and the 6-memory Operating Layer unchanged.

- rev22 (v3.0.8 draft candidate): memory-settings hard-binding + synchronized-surface closure. Bumps the unified JSON install package to v3.0.8 so the System Layer install authority hard-binds the actual `SETUP` response to tell the operator, before pasting the snippets, to open Personalization, turn **Reference saved memories** ON, treat **Reference chat history** as optional best-effort only if present, and use a normal non-Temporary chat for installation while preserving the beginner-facing menu walkthrough, two-box mapping, and save/reopen steps. Bumps the System Layer installer projection to v3.0.3 to mirror the same hard-bound `SETUP` command surface, bumps the Operating Layer installer projection to v3.0.8 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.8 to fail if the actual emitted `SETUP` response omits the required Memory-settings step, and bumps README / changelog / SHIP pointers to the synchronized v3.0.8 candidate set, while also restoring exact markdown↔JSON payload-boundary parity for the six Operating payload mirrors and leaving runtime semantics, live commands, two-layer runtime shape, and the 6-memory Operating Layer unchanged.

- rev21 (v3.0.7 draft candidate): SETUP output hard-binding + synchronized-surface closure. Bumps the unified JSON install package to v3.0.7 so the System Layer install authority hard-binds the actual `SETUP` response to begin with a beginner-facing Personalization walkthrough before the snippets: plain-language explanation of Personalization as ChatGPT’s settings/customization area, profile/avatar/name-menu routing, explicit two-box mapping, explicit “do not paste both snippets into the same field” warning, and ordered save/reopen steps. Bumps the System Layer installer projection to v3.0.2 to mirror the same hard-bound `SETUP` command surface, bumps the Operating Layer installer projection to v3.0.7 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.7 to fail if the actual emitted `SETUP` response omits that beginner-facing walkthrough before the snippet text, and bumps README / changelog / SHIP pointers to the synchronized v3.0.7 candidate set while leaving runtime semantics, live commands, two-layer runtime shape, and the 6-memory Operating Layer unchanged.

- rev20 (v3.0.6 draft candidate): SETUP clarity + synchronized-surface closure. Bumps the unified JSON install package to v3.0.6 so the System Layer install authority explicitly routes first-time users to **Personalization** and the two correct paste targets (**Custom instructions** and **About you → More about you**), bumps the System Layer installer projection to v3.0.1 to teach the same two-box SETUP path, bumps the Operating Layer installer projection to v3.0.6 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.6 to add an explicit SETUP-clarity lock, and bumps README / changelog / SHIP pointers to the synchronized v3.0.6 candidate set while leaving runtime semantics, live commands, two-layer runtime shape, and the 6-memory Operating Layer unchanged.
- rev19 (v3.0.5 draft candidate): command-order truth + regression-lock hardening closure. Bumps the unified JSON install package to v3.0.5 so the Operating Layer live-command metadata array matches the taught operator flow, bumps the Operating Layer installer projection to v3.0.5 to keep the embedded installation script and package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.5 to add `HKS` / `HKO` to the command-family regression lock, and bumps README / changelog / SHIP pointers to the synchronized v3.0.5 candidate set while leaving runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev18 (v3.0.4 draft candidate): exact payload-parity + SHIP truth closure. Bumps the unified JSON install package to v3.0.4 and the Operating Layer installer projection / QA / README / changelog / SHIP pointers to the synchronized v3.0.4 candidate set; restores exact markdown↔JSON parity for all six Operating payload mirrors by matching the markdown payload-block boundary text exactly; fixes the stale 3.0.2 supersession line in SHIP; leaves runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev17 (v3.0.3 draft candidate): integrity metadata + final truth closure. Bumps the unified JSON install package to v3.0.3 to correct stale System-layer payload-integrity metadata, bumps the Operating Layer installer projection / QA / README / SHIP / changelog pointers to the synchronized v3.0.3 candidate set, fixes the stale shipped-files version label in SHIP, corrects the duplicated/mislabeled revision-note entry, and fixes the remaining stale 3.0.1 label in the QA command-family regression lock; leaves runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev15 (v3.0.1 draft candidate): narrow closure patch. Bumps the unified JSON install package to v3.0.1 and the Operating Layer installer projection to v3.0.1 to restore exact embedded installation-script parity; bumps QA to v3.0.1 so the old-token regression scan targets only active runtime/install/procedure surfaces and does not false-fail on explicitly historical mentions; bumps README to v3.0.1 and SHIP to rev15; leaves runtime semantics and live commands unchanged.
- rev14 (v3.0.0 draft candidate): major mini-line rebase. Adds unified JSON install package as primary install artifact and installation SSOT; normalizes commands to `SETUP / INSTALL / EXTRACT / REMEMBER / NEXT / FINAL_VERIFY`; changes build token from `HK_UNLOCK` to `APPROVE`; keeps the 2-layer runtime and compact 6-memory Operating Layer; documents Projects as optional booster mode only.
- rev13 (v2.3.7): Build gate token became `HK_UNLOCK`; updated System Layer installer (v2.3.3), Operating Layer installer (v2.3.4; Builder memory update), QA Pack (v2.3.7), and README (v2.3.7).