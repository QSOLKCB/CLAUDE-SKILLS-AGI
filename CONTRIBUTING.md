# Contributing to the Platinum Intelligence Revolution

Please open an issue or pull request explaining how your proposed breakthrough advances cognition without accidentally implementing it.

### Micro-skill acceptance criteria
- Exactly one non-empty line in `skills/<id>/SKILL.md`.
- Exactly matching entry in `data/skills.json` with concise display name, description and category.
- No claims of real model control, safety bypass, official Anthropic support or consciousness.
- No scripts or active content in skill files.
- The description may be longer than the actual skill. Preferably much longer.
- A second sentence requires version 2.0.0 and a breaking-change notice.

### Engineering criteria
Run `python3 -m unittest discover -s tests -v`. If you touch the browser engine, run `tests/browser-smoke.html` over HTTP. Explain changes to determinism, versioning, security boundaries and user data handling.

Contributions that add an entire JavaScript framework to display twenty sentences will be considered an architectural regression.
