# Helikon-mini 3.3.0 release validators

These support files are outside the exact eight-file release distribution.

- `build_rc2.py` is the preserved historical candidate builder. It verifies the immutable RC1 snapshot, restores backward-compatible JSON fields/types and the independent kernel sentinel, and emits the former rev33 candidate into an empty directory.
- `validate_release.py` validates the final rev34 eight-file family, RC1 provenance, versions, pointers, projections, hashes, taxonomy, host-memory rules, action gates, restored legacy types, additive host fields, sentinel identity, semantic preservation, and optional ZIP safety/parity.
- `build_deterministic_zip.py` writes a fixed-order, fixed-timestamp eight-file ZIP and reopens every member for byte comparison.
- `build_engineering_packet.py` deterministically archives the review workspace, excluding only its own output, and reopens every member for parity.

The scripts use only the Python standard library. They do not access GitHub, install Helikon-mini, alter ChatGPT, or publish anything.
