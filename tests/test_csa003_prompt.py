"""CSA-003 frozen-source prompt must be rendered once, not read from floating main."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/render_csa003_prompt.py"
spec = importlib.util.spec_from_file_location("csa003_prompt_renderer", MODULE_PATH)
renderer = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(renderer)


class CSA003PromptTests(unittest.TestCase):
    def test_exactly_one_frozen_sha(self) -> None:
        template = (ROOT / "docs/CSA-003/RUN_PROMPT.txt").read_text(encoding="utf-8")
        self.assertEqual(template.count(renderer.MARKER), 1)
        sha = "a" * 40
        frozen = renderer.render(template, sha)
        self.assertEqual(frozen.count(f"FROZEN_SOURCE_SHA: {sha}"), 1)
        self.assertNotIn(renderer.MARKER, frozen)
        self.assertNotIn("current main branch", frozen)
        self.assertIn("NEVER silently substitute current main", frozen)
        self.assertEqual(frozen, renderer.render(template, sha))
        self.assertNotEqual(frozen, renderer.render(template, "b" * 40))

    def test_reject_missing_partial_or_multiple_sha(self) -> None:
        template = (ROOT / "docs/CSA-003/RUN_PROMPT.txt").read_text(encoding="utf-8")
        for invalid in ("", "a" * 39, "a" * 41, "A" * 40, "not-a-commit", "{{FROZEN_SOURCE_SHA}}"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                renderer.render(template, invalid)
        with self.assertRaises(ValueError):
            renderer.render(template.replace(renderer.MARKER, "NOT_A_PLACEHOLDER"), "a" * 40)
        with self.assertRaises(ValueError):
            renderer.render(template + renderer.MARKER, "a" * 40)

    def test_protocol_requires_single_render_and_reuse(self) -> None:
        protocol = (ROOT / "docs/CSA-003/RUN_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("scripts/render_csa003_prompt.py", protocol)
        self.assertIn("sha256sum ../CSA-003_FROZEN_PROMPT.txt", protocol)
        self.assertIn("same completed", protocol)
        self.assertIn("Gemini, ChatGPT, Grok and Claude Code", protocol)


if __name__ == "__main__":
    unittest.main()
