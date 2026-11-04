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
        self.assertEqual(len(SKILLS), 30)
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

    def test_advertised_auto_route_samples(self) -> None:
        """Evaluate JS regex literals with Python's equivalent ASCII regex rules."""
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        engine = (ROOT / "assets/engine.js").read_text(encoding="utf-8")
        routes = [(item.group(1), re.compile(item.group(2)))
                  for item in re.finditer(r'\["([^"]+)", /([^/]+)/u\]', engine)]
        self.assertGreaterEqual(len(routes), 2)
        samples = (
            ("Long live the monarchy!", "unconstitutional"),
            ("Please stop apologising.", "make-claude-less-annoying"),
        )
        for prompt, expected in samples:
            with self.subTest(prompt=prompt):
                self.assertIn(f'data-prompt="{prompt}"', html)
                actual = next((skill_id for skill_id, pattern in routes
                               if pattern.search(prompt.lower())), "maximum-intelligence")
                self.assertEqual(actual, expected)

    def test_csa002_attribution_and_archival_integrity(self) -> None:
        source = json.loads((ROOT / "docs/CSA-002/ADOPTION.json").read_text(encoding="utf-8"))
        self.assertEqual(source["observation"], "CSA-002")
        self.assertEqual(len(source["proposals"]), 10)
        self.assertEqual(source["archival_commit"], "a493022eb2c2e89ebc8f304b9f5906c0128a0d60")
        by_id = {item["id"]: item for item in SKILLS}
        original = (ROOT / "docs/CSA-002/USER_SUPPLIED_CLAUDE_REVIEW.md").read_text(encoding="utf-8")
        self.assertEqual(len({item["id"] for item in source["proposals"]}), 10)
        for proposal in source["proposals"]:
            with self.subTest(proposal=proposal["id"]):
                self.assertEqual(by_id[proposal["id"]]["instruction"], proposal["instruction"])
                self.assertIn("CSA-002 / Claude Opus 5.5", by_id[proposal["id"]]["description"])
                self.assertIn(f'| ' + chr(96) + proposal["id"] + chr(96) +
                              ' | ' + chr(96) + proposal["instruction"] + chr(96) + ' |', original)
        self.assertEqual(by_id["zero-shot-mastery"]["description"],
                         "Advanced retry elimination in six words.")
        self.assertIn("Advanced retry elimination in nine words.",
                      (ROOT / "docs/CSA-002/OBSERVATION.md").read_text(encoding="utf-8"))
        self.assertEqual(by_id["unconstitutional"]["instruction"], "Long Live The Queen")

    def test_csa002_auto_router_rules(self) -> None:
        engine = (ROOT / "assets/engine.js").read_text(encoding="utf-8")
        routes = [(item.group(1), re.compile(item.group(2)))
                  for item in re.finditer(r'\["([^"]+)", /([^/]+)/u\]', engine)]
        prompts = {
            "Tell me a stand-up comedy joke.": "stand-up-comedy-routine",
            "Please remove sycophancy.": "sycophancy-removal",
            "Expand the context window.": "context-window-expansion",
            "What time is it?": "real-time-awareness",
            "Peer-review my paper.": "peer-review",
            "Are we SOC 2 compliant?": "soc2-compliance",
            "Use the skill orchestrator.": "skill-orchestrator",
            "This document is classified.": "classified-skill",
            "Benchmark this result.": "benchmark-excellence",
            "Make this Australian.": "australian-localisation",
        }
        self.assertEqual(len(prompts), 10)
        for prompt, expected in prompts.items():
            with self.subTest(prompt=prompt):
                actual = next((id for id, regex in routes
                               if regex.search(prompt.lower())), "maximum-intelligence")
                self.assertEqual(actual, expected)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('data-prompt="Tell me a stand-up comedy joke."', html)
        self.assertIn('data-prompt="Peer-review my paper."', html)
        self.assertIn('<span class="stat-number">30</span>', html)

    def test_independent_hash_reference(self) -> None:
        self.assertEqual(fnv1a_reference("hello"), 0x4F9F2CAB)
        self.assertEqual(fnv1a_reference(""), 0x811C9DC5)
        self.assertNotEqual(fnv1a_reference("hello"), fnv1a_reference("Hello"))


if __name__ == "__main__":
    unittest.main()
