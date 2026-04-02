# Helikon-mini SHIP Manifest — rev19 (v3.0.5 draft candidate)

Date: 2026-04-02

This manifest is the SSOT for the Helikon-mini 3.0.5 draft candidate bundle.

## Product separation invariants (non-negotiable)
- Helikon-mini is a separate product line.
- Helikon-mini artifacts MUST NOT reference or depend on other Helikon lines’ filenames, installer commands, or runtime assumptions.
- Runtime semantics MUST be fully defined by Helikon-mini installers / install package (no doc-only semantics):
  - Unified JSON install package
  - System Layer installer projection
  - Operating Layer installer projection

## Versioning rules (shipping discipline)
- Helikon-mini major versions are independent of Helikon (core) major versions.
- **Kit (bundle) version** is the `vX.Y.Z` in this SHIP header; **revN** increments on any shipped-file change (add/remove/content).
- Shipped components may carry their own versions in filenames; **do not assume** all component filenames match the kit version.
- **Bump rules (minimal churn):**
  - JSON install package filename bumps when package content changes.
  - Installer filenames bump only when installer content changes.
  - README/QA filenames bump when their content changes.
  - Payload/sentinel versions inside installers are integrity markers, not release labels.
- SHIP is the SSOT for exact filenames in the shipped set.

## Draft-candidate authority posture
- `Helikon-mini_Install_Package_v3.0.5.json` is the **primary install artifact** and **installation SSOT** for this candidate set.
- `Helikon-mini_SYSTEM_LAYER_v3.0.0_install.md` and `Helikon-mini_OPERATING_LAYER_v3.0.5_install.md` are synchronized human-readable projections / fallbacks.
- Runtime remains exactly **two layers**:
  - System Layer = Personalization
  - Operating Layer = Saved Memories
- Projects are an optional booster mode only and are not a required runtime layer.

## Shipped files (v3.0.5 draft candidate)
1. `Helikon-mini_Install_Package_v3.0.5.json`
2. `Helikon-mini_SYSTEM_LAYER_v3.0.0_install.md`
3. `Helikon-mini_OPERATING_LAYER_v3.0.5_install.md`
4. `Helikon-mini_QA_PACK_v3.0.5.md`
5. `Helikon-mini_README_v3.0.5.md`
6. `Helikon-mini_CHANGELOG_v3.0.5.md`
7. `Helikon-mini_SHIP_rev19.md`
8. `Helikon-mini_LICENSE.md`

## Non-shipped
- `Helikon-mini_3.0_Architecture_Spec_v0.1.0.md` is a planning artifact and is not part of this shipped candidate set.
- Legacy mini 2.3.7 files are superseded by this 3.0.5 candidate set.
- Planning artifacts must not be treated as runtime semantics.

## Revision notes
- rev19 (v3.0.5 draft candidate): command-order truth + regression-lock hardening closure. Bumps the unified JSON install package to v3.0.5 so the Operating Layer live-command metadata array matches the taught operator flow, bumps the Operating Layer installer projection to v3.0.5 to keep the embedded installation script and package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.5 to add `HKS` / `HKO` to the command-family regression lock, and bumps README / changelog / SHIP pointers to the synchronized v3.0.5 candidate set while leaving runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev18 (v3.0.4 draft candidate): exact payload-parity + SHIP truth closure. Bumps the unified JSON install package to v3.0.4 and the Operating Layer installer projection / QA / README / changelog / SHIP pointers to the synchronized v3.0.4 candidate set; restores exact markdown↔JSON parity for all six Operating payload mirrors by matching the markdown payload-block boundary text exactly; fixes the stale 3.0.2 supersession line in SHIP; leaves runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev17 (v3.0.3 draft candidate): integrity metadata + final truth closure. Bumps the unified JSON install package to v3.0.3 to correct stale System-layer payload-integrity metadata, bumps the Operating Layer installer projection / QA / README / SHIP / changelog pointers to the synchronized v3.0.3 candidate set, fixes the stale shipped-files version label in SHIP, corrects the duplicated/mislabeled revision-note entry, and fixes the remaining stale 3.0.1 label in the QA command-family regression lock; leaves runtime semantics, live commands, two-layer runtime shape, and 6-memory Operating Layer unchanged.
- rev15 (v3.0.1 draft candidate): narrow closure patch. Bumps the unified JSON install package to v3.0.1 and the Operating Layer installer projection to v3.0.1 to restore exact embedded installation-script parity; bumps QA to v3.0.1 so the old-token regression scan targets only active runtime/install/procedure surfaces and does not false-fail on explicitly historical mentions; bumps README to v3.0.1 and SHIP to rev15; leaves runtime semantics and live commands unchanged.
- rev14 (v3.0.0 draft candidate): major mini-line rebase. Adds unified JSON install package as primary install artifact and installation SSOT; normalizes commands to `SETUP / INSTALL / EXTRACT / REMEMBER / NEXT / FINAL_VERIFY`; changes build token from `HK_UNLOCK` to `APPROVE`; keeps the 2-layer runtime and compact 6-memory Operating Layer; documents Projects as optional booster mode only.
- rev13 (v2.3.7): Build gate token became `HK_UNLOCK`; updated System Layer installer (v2.3.3), Operating Layer installer (v2.3.4; Builder memory update), QA Pack (v2.3.7), and README (v2.3.7).
