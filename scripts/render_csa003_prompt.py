#!/usr/bin/env python3
"""Render exactly one CSA-003 source-pinned prompt (stdlib only)."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs/CSA-003/RUN_PROMPT.txt"
MARKER = "{{FROZEN_SOURCE_SHA}}"


def render(template: str, source_sha: str) -> str:
    """Reject placeholders that could make different reviewers audit different revisions."""
    if re.fullmatch(r"[0-9a-f]{40}", source_sha) is None:
        raise ValueError("Source SHA must be one complete lowercase 40-character commit hash.")
    if template.count(MARKER) != 1:
        raise ValueError("Expected exactly one frozen-source placeholder.")
    if f"FROZEN_SOURCE_SHA: {MARKER}" not in template:
        raise ValueError("Frozen-source marker not in required source declaration.")
    rendered = template.replace(MARKER, source_sha)
    if MARKER in rendered:
        raise ValueError("Unresolved placeholder.")
    return rendered


def verify_local_commit(source_sha: str) -> None:
    result = subprocess.run(
        ["git", "cat-file", "-t", source_sha],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 0 or result.stdout.strip() != "commit":
        raise ValueError("Frozen source SHA is not a readable commit in this local checkout.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-sha", required=True, help="Immutable post-merge Git commit SHA")
    parser.add_argument("--output", type=Path, required=True, help="New output file, never overwritten")
    args = parser.parse_args()
    try:
        result = render(TEMPLATE.read_text(encoding="utf-8"), args.source_sha)
        verify_local_commit(args.source_sha)
        data = result.encode("utf-8")
        with args.output.open("xb") as f:
            f.write(data)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"SOURCE_COMMIT_SHA={args.source_sha}")
    print(f"PROMPT_SHA256={hashlib.sha256(data).hexdigest()}")
    print(f"OUTPUT={args.output}")


if __name__ == "__main__":
    main()
