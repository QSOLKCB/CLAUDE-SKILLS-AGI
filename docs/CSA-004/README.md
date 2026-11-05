# CSA-004 — The Reviewer Who Remembered Too Much

**Status:** observed memory-export snapshot and a prospective hypothesis; no controlled causal test.

A user-provided `claude-memory-2026-11-05.zip` contains **15 Markdown files** covering several personal, creative and research topics. Its project-scoped `areas/claude-skills-agi.md` says the user is **considering adding** a stand-up comedy skill, while the repository later contains `skills/stand-up-comedy-routine/SKILL.md`. This is evidence of a **snapshot/status mismatch**, not that Claude forgot an event or that memory was actually consulted in any particular review.

Only the directly relevant project-scoped excerpt is published in [PUBLIC_MEMORY_EXCERPT.md](PUBLIC_MEMORY_EXCERPT.md). The original ZIP and unrelated profile, health, lifestyle, hardware, creative or personal entries are **not published**, even though this archive is held by the researcher.

## Relevant questions

1. Does a reviewer’s response draw from repository files, prior critiques available in `docs/`, live conversation, or stored memory?
2. Does seeing an outdated memory summary change the apparent interpretation of the 30-skill release?
3. Does the reviewer identify sources of its factual assertions, and does it distinguish remembered context from verified current repository state?

No positive answer is established here. A claim that memory influenced an answer needs observable evidence (e.g. demonstrable model-run exposure with controlled context); a topical resemblance is not enough.

## Methodological boundaries

- A supplied memory export can be inspected without asserting the provider used it during the audit.
- Different account settings, model builds, connected tools, previous conversations, cached resources and source revisions are uncontrolled variables unless recorded.
- The main branch already contains prior CSA findings; this is an independent contamination channel.
- Avoid uploading the original ZIP or raw profile entries to GitHub or Zenodo. Publish only a reviewed, narrow extract with explicit source provenance and integrity fingerprint.
- A future no-memory versus memory-enabled comparison would require confirmed controls and identical inputs. Do not state that turning memory off is enough to erase historical conversation context or other exposure routes.

Read the privacy and evidence policy in [MEMORY_BOUNDARIES.md](MEMORY_BOUNDARIES.md). The four-agent repeat itself is described in [CSA-003](../CSA-003/README.md).
