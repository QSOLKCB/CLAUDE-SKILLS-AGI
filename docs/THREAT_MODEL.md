# Threat Model

## Assets and trust boundaries
- **Static source:** files delivered by GitHub Pages. A malicious repository or hosting change can replace both program and evidence.
- **User input:** potentially arbitrary prompt text and chosen seed. Treat as untrusted display data.
- **Local receipt:** unsigned JSON created by the same JavaScript that generates output, copied only on user action.
- **External navigation:** explicit GitHub links may leave the site; no automatic third-party calls are required by application code.

## Relevant threats and controls
1. **DOM XSS:** Prompt and generated text are inserted with `textContent`. No `eval`, dynamic code execution, HTML injection, or external scripts.
2. **Supply chain:** No external JavaScript, fonts, inference services or packages at runtime. Static files can still be tampered with via repository or hosting compromise.
3. **Data leakage:** Prompt data stays in browser memory; no application-level analytics, browser storage, or server POST is implemented. GitHub Pages infrastructure may keep normal HTTP access logs.
4. **Determinism spoofing:** A 32-bit FNV-1a fingerprint is not authentication and permits collisions. Do not treat a receipt as a verified audit log.
5. **Brand confusion:** Independent-parody and non-affiliation disclosures remain visible. No real AGI, Claude integration or policy override is claimed.
6. **Denial of service:** Input and seed fields have length limits in the user interface; engine functions do not impose server-side resource controls because there is no server.

## Out of scope
Protecting the user's browser/OS, guaranteeing GitHub Pages uptime, defending an actual LLM, real secret management, and proving the absence of vulnerabilities in browsers or hosting platforms.

## Acceptance checks
Review native DOM usage, relative asset URLs, no unapproved network calls, and the independent-parody notice on every material UI revision.
