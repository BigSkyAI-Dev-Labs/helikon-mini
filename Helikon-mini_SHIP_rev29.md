# Mount Helikon-mini 3.1 AIOS SHIP Manifest — rev29
(v3.1.2 draft candidate)

Date: 2026-04-22

This manifest is the SSOT for the Mount Helikon-mini 3.1 AIOS (v3.1.2) draft candidate bundle.

## Product separation invariants (non-negotiable)
- Mount Helikon-mini 3.x AIOS is a separate product line.
- Mount Helikon-mini 3.x AIOS artifacts MUST NOT reference or depend on other Helikon lines' filenames, installer commands, or runtime assumptions.
- Runtime semantics MUST be fully defined by Mount Helikon-mini 3.x AIOS installers / install package (no doc-only semantics):
  - Unified JSON install package
  - System Layer installer projection
  - Operating Layer installer projection
- Shipped filenames remain in the `Helikon-mini_*` namespace and the Saved Memory IDs remain in the `Helikon-mini.*` namespace for runtime continuity in this candidate set.

## Versioning rules (shipping discipline)
- Mount Helikon-mini 3.x AIOS major versions are independent of Helikon (core) major versions.
- **Kit (bundle) version** is the `vX.Y.Z` in this SHIP header; **revN** increments on any shipped-file change (add/remove/content).
- Shipped components may carry their own versions in filenames; **do not assume** all component filenames match the kit version.
- **Bump rules (minimal churn):**
  - JSON install package filename bumps when package content changes.
  - Installer filenames bump only when installer content changes.
  - README/QA filenames bump when their content changes.
  - Payload/sentinel versions inside installers are integrity markers, not release labels.
- SHIP is the SSOT for exact filenames in the shipped set.

## Draft-candidate authority posture
- `Helikon-mini_Install_Package_v3.1.2.json` is the **primary install artifact** and **installation SSOT** for this candidate set.
- `Helikon-mini_SYSTEM_LAYER_v3.1.2_install.md` and `Helikon-mini_OPERATING_LAYER_v3.1.2_install.md` are synchronized human-readable projections / fallbacks.
- Runtime remains exactly **two layers**:
  - System Layer = Personalization
  - Operating Layer = Saved Memories
- The 6-memory Operating Layer remains the core continuity surface for the installed edition.
- Projects are supported as a recommended workspace wrapper for longer-running work, but they are not a required runtime layer.

## Shipped files (v3.1.2 draft candidate)
1. `Helikon-mini_Install_Package_v3.1.2.json`
2. `Helikon-mini_SYSTEM_LAYER_v3.1.2_install.md`
3. `Helikon-mini_OPERATING_LAYER_v3.1.2_install.md`
4. `Helikon-mini_QA_PACK_v3.1.2.md`
5. `Helikon-mini_README_v3.1.2.md`
6. `Helikon-mini_CHANGELOG_v3.1.2.md`
7. `Helikon-mini_SHIP_rev29.md`
8. `Helikon-mini_LICENSE.md`

## Non-shipped
- `Helikon-mini_3.0_Architecture_Spec_v0.1.0.md` is a planning artifact and is not part of this shipped candidate set.
- Legacy mini 2.3.7 files are superseded by this 3.1.2 candidate set.
- Planning artifacts must not be treated as runtime semantics.

## Revision notes
- rev29 (v3.1.2 draft candidate): metadata-truth closure patch. Bumps the unified JSON install package to v3.1.2 so the remaining stale `3.1.0 draft candidate set` note inside the JSON metadata is repaired and the synchronized source-file inventory matches the repaired shipped set while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the System Layer and Operating Layer installer projections to v3.1.2 only to keep their package-pointer text synchronized with the new JSON package line while leaving System snippet text, the 6-memory install loop, payload IDs, and memory payload text unchanged. Bumps QA / README / changelog / SHIP pointers to the synchronized 3.1.2 metadata-truth closure candidate set while leaving runtime semantics unchanged.
- rev28 (v3.1.1 draft candidate): cleanup-closure patch. Bumps the unified JSON install package to v3.1.1 so the synchronized package pointers and source-file inventory match the repaired shipped set while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the System Layer and Operating Layer installer projections to v3.1.1 only to keep their package-pointer text synchronized with the new JSON package line while leaving System snippet text, the 6-memory install loop, payload IDs, and memory payload text unchanged. Bumps QA / README / changelog / SHIP pointers to the synchronized 3.1.1 cleanup-closure candidate set, and repairs the malformed historical `v3.0.6 — rev20` heading in the shipped changelog while leaving runtime semantics unchanged.
- rev27 (v3.1.0 draft candidate): Free-fit onboarding and posture redesign patch. Bumps the unified JSON install package to v3.1.0 so the public mini surfaces become benefit-first rather than installer-first while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the System Layer installer projection to v3.1.0 to keep the beginner-explicit `SETUP` truth contract while reframing the System Layer as compact account-level activation and updating the More about you snippet to emphasize memory-backed continuity. Bumps the Operating Layer installer projection to v3.1.0 to keep the same 6-memory loop and payload text while reframing the Operating Layer as mini's continuity layer. Bumps QA / README / changelog / SHIP pointers to the synchronized 3.1.0 candidate set and adds explicit public-posture locks for memory centrality and Projects-as-wrapper wording while leaving runtime semantics unchanged.
- rev26 (v3.0.12 draft candidate): branding-hygiene closure patch. Bumps the unified JSON install package to v3.0.12 to correct the remaining stale package-set note inside the JSON metadata so the package now consistently refers to the **3.0.12 draft candidate set** while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the Operating Layer installer projection to v3.0.12 to keep the package-pointer text synchronized with the new JSON package line, bumps QA / README / changelog / SHIP pointers to the synchronized v3.0.12 candidate set, and standardizes the shipped `Helikon-mini_LICENSE.md` title to **Mount Helikon Mini 3.0 AIOS License (MIT)** while leaving runtime semantics unchanged.
- rev25 (v3.0.11 draft candidate): cleanup/truth-closure patch. Bumps the unified JSON install package to v3.0.11 to correct the remaining stale JSON runtime-status wording so `none_state_rule` now refers to **Mount Helikon Mini 3.0 AIOS** rather than the older outward `Helikon-mini` label while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the Operating Layer installer projection to v3.0.11 to keep the package-pointer text synchronized with the new JSON package line, bumps QA to v3.0.11 to close the stale regression-lock wording that still referenced the active runtime/install/procedure surfaces as `3.0.9`, and bumps README / changelog / SHIP pointers to the synchronized v3.0.11 candidate set while leaving runtime semantics unchanged.
- rev24 (v3.0.10 draft candidate): branding/descriptor standardization + synchronized-surface closure. Bumps the unified JSON install package to v3.0.10 so the package and shipped mini surfaces now identify the product as **Mount Helikon Mini 3.0 AIOS** and standardize the outward descriptor as **the Free Starter operating system line for ChatGPT** while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity. Bumps the System Layer installer projection to v3.0.5 to mirror the same standardized product identity across the SETUP surface and pasted snippets while keeping the Custom instructions payload within limit, bumps the Operating Layer installer projection to v3.0.10 to keep the package pointer and outward installer labeling synchronized without changing payload IDs or payload text, and bumps QA / README / changelog / SHIP pointers to the synchronized v3.0.10 candidate set while leaving runtime semantics unchanged.

