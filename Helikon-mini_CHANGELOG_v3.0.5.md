# Helikon-mini Changelog

Canonical change record for the Helikon-mini bundle.
- Kit releases are tracked by **SHIP rev** + `vX.Y.Z` (see the current SHIP manifest).
- Component filenames may carry their own versions; the SHIP manifest is the SSOT for what ships.

## v3.0.5 — rev19 draft candidate (2026-04-02)
- Command-order truth + regression-lock hardening closure on top of the 3.0.4 exact-parity candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.5.json` to align the Operating Layer live-command metadata array with the taught operator flow and refresh the synchronized source-file inventory for the v3.0.5 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.5_install.md` to keep the embedded installation script and package-pointer text synchronized with the new JSON package line while leaving payload text and runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.5.md` to expand the command-family regression lock so it also scans for `HKS` and `HKO` in the active runtime/install/procedure surfaces.
- Bumped `Helikon-mini_README_v3.0.5.md` and `Helikon-mini_SHIP_rev19.md` to the synchronized closure candidate set.
- Left live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.4 — rev18 draft candidate (2026-04-01)
- Exact payload-parity + SHIP truth closure on top of the 3.0.3 integrity-closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.4.json` to refresh synchronized package metadata and source-file inventory for the v3.0.4 set while leaving runtime semantics unchanged.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.4_install.md`, `Helikon-mini_QA_PACK_v3.0.4.md`, `Helikon-mini_README_v3.0.4.md`, and `Helikon-mini_SHIP_rev18.md` to the synchronized exact-parity closure candidate set.
- Restored exact markdown↔JSON parity for all six Operating payload mirrors by matching the markdown payload-block boundary text exactly.
- Fixed the stale 3.0.2 supersession wording in SHIP.
- Left live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.3 — rev17 draft candidate (2026-04-01)
- Final integrity/truth closure on top of the 3.0.2 truth-polish candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.3.json` to correct stale System-layer payload-integrity metadata and refresh the synchronized source-file inventory for the v3.0.3 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.3_install.md`, `Helikon-mini_QA_PACK_v3.0.3.md`, `Helikon-mini_README_v3.0.3.md`, and `Helikon-mini_SHIP_rev17.md` to the synchronized integrity-closure candidate set.
- Fixed the stale shipped-files version label and duplicated/mislabeled revision-note entry in SHIP, and fixed the remaining stale 3.0.1 label in the QA command-family regression lock.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.2 — rev16 draft candidate (2026-04-01)
- Final doc truth polish on top of the 3.0.1 closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.2.json` to correct stale package-set wording inside the JSON metadata and refresh the synchronized source-file inventory for the v3.0.2 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.2_install.md`, `Helikon-mini_QA_PACK_v3.0.2.md`, `Helikon-mini_README_v3.0.2.md`, and `Helikon-mini_SHIP_rev16.md` to the synchronized truth-polish candidate set.
- Corrected the stale 3.0.0 supersession wording in SHIP and fixed the v3.0.0 changelog entry so it names `Helikon-mini_Install_Package_v3.0.0.json` rather than the later 3.0.1 file.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.1 — rev15 draft candidate (2026-04-01)
- Narrow closure patch on top of the 3.0.0 draft candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.1.json` and `Helikon-mini_OPERATING_LAYER_v3.0.1_install.md` to restore exact embedded Operating installation-script parity between the JSON package and markdown projection.
- Bumped `Helikon-mini_QA_PACK_v3.0.1.md` so the old-token regression scan targets only active runtime/install/procedure surfaces and no longer false-fails on explicitly historical mentions inside SHIP/changelog.
- Bumped `Helikon-mini_README_v3.0.1.md` and `Helikon-mini_SHIP_rev15.md` to the synchronized closure candidate set.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.0 — rev14 draft candidate (2026-04-01)
- Major starter-line rebase from the 2.3.7 baseline.
- Added `Helikon-mini_Install_Package_v3.0.0.json` as the **primary install artifact** and **installation SSOT**.
- Re-labeled the System and Operating `_install` files as synchronized human-readable projections / fallbacks.
- Normalized the installer command family to:
  - `SETUP`
  - `INSTALL`
  - `EXTRACT`
  - `REMEMBER`
  - `NEXT`
  - `FINAL_VERIFY`
- Retired:
  - `HMS`
  - `HMO`
- Changed the build gate token from `HK_UNLOCK` to `APPROVE`.
- Preserved the 2-layer runtime:
  - System Layer = Personalization
  - Operating Layer = 6 Helikon-mini Saved Memories
- Preserved the compact 6-memory topology rather than expanding to a 12-pillar operating layer.
- Added explicit optional Projects booster posture while keeping projects outside the normative runtime contract.
- Bumped README, QA, SHIP, and installer surfaces to the 3.0.0 candidate set.

## v2.3.7 — rev13 (2026-02-17)
- Build gate token is now `HK_UNLOCK`.
- System Layer install surface bumped to v2.3.3 (kernel sentinel update).
- Operating Layer install surface bumped to v2.3.4 (Meleteon.Builder memory update).
- QA Pack + README bumped to v2.3.7 to match shipped pointers.

## v2.3.6 — rev12 (2026-02-17)
- Operating Layer install surface bumped to v2.3.3; Aoideon.Canon memory content bumped to v2.3.2.
- Aoideon.Canon now anchors `EXPECTED_OPERATING_MEMORIES (6)` and a deterministic FULL/PARTIAL/NONE + missing-names rule to prevent hallucinated missing-name lists under PARTIAL installs.
- QA + README prompts updated to reference the anchored expected set and allow `missing: unknown` when the expected set is unavailable.

## v2.3.5 — rev11 (2026-02-17)
- Mechanical lineage renumber from the prior `0.3.x` kit series to `2.3.x` to avoid collision with archived Helikon-mini 1.x artifacts.
- Renamed shipped artifacts to `v2.3.x` and updated pointers/sentinels accordingly. No behavioral/protocol changes intended.
- Helikon-mini major versions are independent of Helikon (core) major versions.
