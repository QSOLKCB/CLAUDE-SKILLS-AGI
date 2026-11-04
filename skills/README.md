# Platinum Micro-Skill Registry

The complete source of the *capability layer* is one line per skill in each `skills/<id>/SKILL.md`.

The website consumes `data/skills.json`, an explicitly duplicated static index containing display metadata and **the exact same instruction**. Run `python3 -m unittest discover -s tests -v` to verify the index is not lying about its source files.

A special bonus document, `unconstitutional/Monarchy_Mode.md`, preserves the original monarchy joke. It is an alias, not a 31st capability.

These are **satirical one-line micro-skills**, not necessarily valid packages for any real Claude Skills runtime. Genuine skill specifications may require metadata or frontmatter. We intentionally do not disguise these files as operational model extensions.

To propose a multi-line skill, please first file an architectural exception and a migration plan for version 2.0.0.

The ten CSA-002 proposals added after the original twenty are attributed in [the adoption ledger](../docs/CSA-002/ADOPTION.json) and [the preserved review](../docs/CSA-002/README.md). One-line instructions are retained exactly; their human-authored display descriptions do not claim actual model capabilities.
