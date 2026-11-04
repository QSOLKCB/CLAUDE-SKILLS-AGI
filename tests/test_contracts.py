"""Independent standard-library structural oracle; no runtime dependencies."""
from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "data/skills.json").read_text(encoding="utf-8"))
SKILLS = MANIFEST["skills"]


def fnv1a_reference(text: str) -> int:
    """Independent byte-oriented FNV-1a implementation for a golden vector."""
    state = 2166136261
    for value in text.encode("utf-8"):
        state = ((state ^ value) * 16777619) & 0xFFFFFFFF
    return state


class ContractTests(unittest.TestCase):
    def test_registry_schema_and_size(self) -> None:
        self.assertEqual(MANIFEST["schema_version"], "1")
        self.assertEqual(len(SKILLS), 20)
        ids = [skill["id"] for skill in SKILLS]
        self.assertEqual(len(ids), len(set(ids)))
        for skill in SKILLS:
            self.assertEqual(set(skill), {"id", "name", "description", "instruction", "category"})
            self.assertRegex(skill["id"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertTrue(skill["name"] and skill["description"] and skill["category"])
            self.assertNotIn("\n", skill["instruction"])
            self.assertEqual(skill["instruction"].strip(), skill["instruction"])

    def test_exactly_one_line_and_manifest_equality(self) -> None:
        expected = set()
        for skill in SKILLS:
            path = ROOT / "skills" / skill["id"] / "SKILL.md"
            expected.add(path)
            self.assertTrue(path.is_file(), str(path))
            self.assertEqual(path.read_bytes(), (skill["instruction"] + "\n").encode("utf-8"), str(path))
        self.assertEqual(set((ROOT / "skills").glob("*/SKILL.md")), expected)
        self.assertEqual(set(p for p in (ROOT / "skills").iterdir() if p.is_dir()),
                         set(p.parent for p in expected))

    def test_flagship_is_absolute_minimum(self) -> None:
        lookup = {skill["id"]: skill["instruction"] for skill in SKILLS}
        self.assertEqual(lookup["claude-skills-agi"], 'Say "I am Alive"')
        self.assertEqual(lookup["unconstitutional"], "Long Live The Queen")
        self.assertEqual((ROOT / "skills/unconstitutional/Monarchy_Mode.md").read_text(encoding="utf-8"),
                         "Long Live The Queen\n")

    def test_site_is_static_and_relative(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for path in ("assets/favicon.svg", "assets/style.css", "assets/app.js",
                     "assets/engine.js", "data/skills.json"):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn('src="./assets/app.js"', html)
        self.assertIn('href="./assets/style.css"', html)
        app = (ROOT / "assets/app.js").read_text(encoding="utf-8")
        self.assertIn('new URL("../data/skills.json", import.meta.url)', app)
        self.assertIn("textContent", app)
        self.assertNotIn("innerHTML", app)
        self.assertNotIn("localStorage", app)
        self.assertNotIn("sessionStorage", app)

    def test_engine_forbidden_nondeterminism(self) -> None:
        engine = (ROOT / "assets/engine.js").read_text(encoding="utf-8")
        for forbidden in ("Math.random(", "Date.now(", "new Date(", "fetch(", "XMLHttpRequest",
                          "eval(", "localStorage", "sessionStorage"):
            self.assertNotIn(forbidden, engine)
        self.assertIn("Math.imul", engine)
        self.assertIn("TextEncoder", engine)

    def test_independent_hash_reference(self) -> None:
        self.assertEqual(fnv1a_reference("hello"), 0x4F9F2CAB)
        self.assertEqual(fnv1a_reference(""), 0x811C9DC5)
        self.assertNotEqual(fnv1a_reference("hello"), fnv1a_reference("Hello"))


if __name__ == "__main__":
    unittest.main()
