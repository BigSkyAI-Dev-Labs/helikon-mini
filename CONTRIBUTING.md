# Contributing to Helikon-mini

Thanks for contributing. Helikon-mini is a structured runtime framework for consistent ChatGPT operation (workflows, safety gates, verification posture, and memory hygiene). Contributions are welcome, but **runtime/protocol drift** is the primary risk—this guide exists to prevent that.

## What to contribute
- Docs improvements: clarity, examples, troubleshooting
- Installer hardening: clearer steps, more robust wording, better safety defaults
- Protocol fixes: edge cases in operator commands or health checks
- Tooling: repo checks that prevent regressions (CI, verification scripts)

## Design constraints (non-negotiable)
### A) Two-layer runtime
1. **System Layer** lives in Custom Instructions + “More about you”
2. **Operating Layer** installs as Saved Memories

Anything runtime-relevant must be defined in these installers and reflected in the README usage section.

### B) Protocol stability
The operator command interface is part of the product surface. Do not casually change:
- `HMS`, `HMO`, `INSTALL`, `REMEMBER`, `NEXT`
- safety tokens: `HK_UNLOCK` (authorizes heavy/build/code/destructive work), `YES` (authorizes delete/overwrite)

If you must change a token or protocol rule:
- explain why (risk/benefit)
- update README + both installer docs accordingly
- note backward compatibility (or explicitly state breaking change)

### C) No “doc-only semantics”
Do not introduce new “modes”, “tokens”, “control codes”, invariants, or behaviors that exist only in prose. If it affects runtime, it must be installed.

### D) Determinism + safety defaults
Prefer:
- explicit assumptions
- conservative behavior when tools/memory are unavailable
- repeatable workflows (“plan → verify → emit”)

### E) Separation discipline
Helikon-mini is its own product line. Keep the repo self-contained and avoid importing external runtime assumptions, tokens, or filenames.

## Repo structure
This repo is intentionally minimal for end-users:
- `Helikon-mini_SYSTEM_LAYER_..._install.md`
- `Helikon-mini_OPERATING_LAYER_..._install.md`
- `README.md`, `LICENSE`

Additional community files (.github, contributing, security) should not change installation semantics.

## Development workflow
1. Fork the repo
2. Create a branch: `feat/<topic>` or `fix/<topic>`
3. Make changes
4. Run local checks (if present), e.g. repo verifier scripts
5. Do a **fresh-install smoke test** (recommended for installer/README changes):
   - Install System Layer
   - Install Operating Layer
   - Run: `HMS`, `HMO`, and complete one install loop (`INSTALL` → `REMEMBER` → `NEXT`)

## Pull request checklist (required)
- [ ] Change is scoped and explained (what/why)
- [ ] README remains consistent with installer files
- [ ] If changing protocols/tokens, all surfaces updated (README + both installers)
- [ ] Any repo checks/scripts pass
- [ ] For installer/README changes: fresh-install smoke test completed

## Versioning guidance
Installer filenames are versioned. Prefer:
- bump the filename version when changing runtime behavior, tokens, or required steps
- small, additive edits when fixing typos or improving clarity without altering semantics

If unsure, open an Issue first describing the proposed change and the intended compatibility story.
