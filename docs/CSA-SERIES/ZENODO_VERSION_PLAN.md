# CSA Series — Future Zenodo Record Version Plan

**Existing published record supplied by the author:** DOI `10.5281/zenodo.23964942`, originally titled **CSA-001 — The Self-Referential Skills Review Incident**, release v1.0.0.

**Not yet undertaken:** no new Zenodo version reserved, uploaded, verified or published for CSA-003/004.

## Release order

1. Merge this **protocol and observation** documentation PR.
2. Run the frozen CSA-003 prompt once on each of Gemini, ChatGPT, Grok and Claude Code against an identical recorded source commit and with the disclosure that the archive is exposed.
3. Preserve results and independent reproductions in a **separate** results PR; merge only after human review and reproducible integrity checks.
4. Create a versioned, flat archival payload (including source IDs, comparison ledger, prompt, complete or explicitly redacted reviewer reports, memory excerpt, executed evidence and `SHA256SUMS`). Do not upload private provider-session exports or the full Claude memory ZIP without selective, explicit review.
5. Use Zenodo **New version** on the existing record if the owner chooses to keep CSA-001/002/003/004 in the same accumulating dataset. Preserve earlier files, accurately describe the version delta, and ensure the record title/description reflect the expanded scope.
6. Check whether Zenodo assigns a new **version DOI** and preserves a separate concept DOI. Record both exactly as returned by Zenodo. Never assume `10.5281/zenodo.23964942` is also the new version DOI.
7. Verify Zenodo's final public file list and checksum manifest, then announce publication. Do not claim publication merely from a reserved DOI or a prepared draft.

## Packaging validation (to execute later)

- `sha256sum -c SHA256SUMS` verifies every listed payload file.
- The checksum file excludes itself to avoid self-reference.
- Flat file paths in the manifest match the actual Zenodo download layout; zip paths are validated separately.
- No unlisted extra files, path collisions, or mismatched file counts.
- Preserve the full historical incident separately from later interpretation; results should never rewrite old evidence.

## Scope/title choice

A record whose title specifies only **CSA-001** can become misleading if it carries CSA-003 and CSA-004. The author should either update the new version's title to describe the cumulative **CSA Series** and retain a clear version history, or issue separate records for the distinct experiments and relate their DOIs. The requested plan is a **new version of the existing record**, not a premature new DOI.

No further work can be completed until the four fresh outputs and, if present, tool receipts are provided.
