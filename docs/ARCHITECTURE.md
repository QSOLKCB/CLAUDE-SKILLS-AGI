# Architecture — Platinum Intelligence Lab

## Boundary diagram

```text
                        STATIC GITHUB PAGES
  ┌──────────────────────────────────────────────────────────┐
  │ index.html + assets/style.css                           │
  │       │                                                  │
  │ assets/app.js  ─────── data/skills.json                  │
  │       │                 (static index, skill text copy)   │
  │ assets/engine.js                                         │
  │       │                                                  │
  │ normalize → route → classify → FNV-1a → fixed templates  │
  │       │                                                  │
  │ display output + local receipt (user may copy JSON)      │
  └──────────────────────────────────────────────────────────┘
            NO LLM / NO SERVER INFERENCE / NO STORAGE

  skills/*/SKILL.md are the canonical satirical one-liners.
  tests/test_contracts.py checks their equality with the JSON index.
```

## Operation

1. On load, `app.js` fetches `data/skills.json` using a same-origin relative module URL. Nothing is fetched from a third-party service for inference.
2. A user selects a named skill or `auto`. Auto uses a fixed-order keyword router that falls back to `maximum-intelligence`.
3. Each prompt is processed independently by `infer()` in `assets/engine.js`; displayed chat history does **not** influence subsequent output.
4. NFKC Unicode normalization, whitespace folding and lowercase canonicalization produce a normalized prompt.
5. The seed, engine version, routed skill ID, canonical instruction and normalized prompt are joined with the ASCII unit separator (U+001F) and hashed using FNV-1a on UTF-8 bytes.
6. A fixed intent response bank is indexed using the integer hash modulo its response count. AGI and Monarchy Mode intentionally use fixed output overrides.
7. The browser displays output and lets the user copy a JSON receipt without timestamps or external uploads.

## Static hosting

GitHub Pages serves the site from the repository root (`index.html`). All application assets use local relative paths compatible with a project Pages URL. A simple local HTTP server is sufficient; `file://` imports are not supported in all browsers.

## Explicit limitations

FNV-1a is **not** collision-resistant or cryptographic. A receipt supports reproducing an output using the pinned source and manifest; it cannot prove which code actually ran, guarantee integrity against malicious edits, or attest to a model's capabilities. The project is a humorous deterministic rule-and-template demo rather than an LLM. A real Claude skill pack may require frontmatter and additional structure that we deliberately omit.

## Dependency policy

No npm, Node.js, Docker, cloud inference, trackers, external fonts, runtime libraries or build pipeline. Tests use the Python standard library; the actual interface uses native web APIs.
