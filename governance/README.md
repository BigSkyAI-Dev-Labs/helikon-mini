# Helikon-mini Repository Evidence Guide

This directory contains provenance and governance evidence for repository builds. These records document how a candidate was produced and checked; they do not grant runtime authority and are not installation instructions.

## Interpreting historical workspace paths

Some immutable engineering records contain absolute paths such as `/workspace/scratch/...`. They are historical locators from the isolated build environment in which the receipt was generated. They are not expected to exist on a contributor's computer, are not required for validation, and contain no portable repository configuration.

Future public receipts should prefer repository-relative paths. When an external working directory must be described, use a neutral placeholder such as `<build-workspace>` and pair the claim with repository paths, artifact hashes, or both.

## Interpreting `dist/` references

The `dist/` paths mentioned in historical receipts identify local, reproducible validation outputs. RC2 binary archives and the live-host QA operator kit were deliberately kept out of Git and were not published as GitHub Release assets. Current CI builds the final v3.3.0 archive under its temporary runner directory, validates it, and discards it after the run.

The final release family is in `release/v3.3.0/`. The immutable comparison baseline remains in `source-rc1/v3.3.0/`, and the byte-preserved previous release is in `release/v3.2.0/`.

## Repository checksum scope

`checksums/Helikon-mini_3.3.0_RC2_REPOSITORY_SHA256SUMS.txt` is historical evidence covering the 35 payload files introduced with the RC2 source integration. `checksums/Helikon-mini_3.3.0_REPOSITORY_SHA256SUMS.txt` is the current final-release manifest used by CI and does not hash itself.

Historical checksum manifests remain unchanged. A future release line should create a new manifest rather than silently rewriting an earlier release record.

## Authority boundary

The release runtime contract remains the two-layer Helikon-mini design documented by the release files. Provenance records, CI configuration, receipts, local paths, and generated archives are evidence about the release; none of them is a third runtime layer or a source of installation authority.
