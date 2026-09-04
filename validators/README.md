# Helikon-mini 3.3.0 RC2 engineering validators

These support files are outside the exact eight-file release distribution.

- `build_rc2.py` verifies the immutable RC1 snapshot, restores backward-compatible JSON fields/types and the independent kernel sentinel, advances SHIP to rev33, and writes only to an empty RC2 release directory.
- `validate_release.py` validates RC1 provenance, the eight-file family, versions, pointers, projections, hashes, taxonomy, host-memory rules, action gates, restored legacy types, additive RC1 fields, sentinel identity, semantic preservation, and optional ZIP safety/parity.
- `build_deterministic_zip.py` writes a fixed-order, fixed-timestamp eight-file ZIP and reopens every member for byte comparison.
- `build_engineering_packet.py` deterministically archives the review workspace, excluding only its own output, and reopens every member for parity.

The scripts use only the Python standard library. They do not access GitHub, install Helikon-mini, alter ChatGPT, or publish anything.
