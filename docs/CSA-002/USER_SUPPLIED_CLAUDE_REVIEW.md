# CSA-002 — Claude Response (User-Supplied Transcript)

> Supplied by the user on 2026-11-05 and attributed to Claude Opus 5.5 High. The content below is preserved as supplied, with Markdown rendering of quoted code spans; it is not an independently authenticated provider export. No corrections are made to the model's claims.

I read all 20. Here's my take.

## Fix

**Zero Shot Mastery has a real bug.** Its manifest description says "retry elimination in nine words," but `Get it right the first time.` is six. The zero-shot skill didn't get its own description right the first time. Since the repo's whole bit is that the engineering is real, this is your only genuine defect. You could fix it by changing the description to "six words." Or keep "nine" and add a test that checks every number claimed in a description, then let CI fail on it permanently as a feature.

**Monarchy Mode is out of date.** `Long Live The Queen` has been stale since 2022, which is awkward for an Australian repo. I wouldn't fix the line, though. Change the description to "Sovereignty last verified at training time." Then it becomes a knowledge-cutoff joke, which is a better joke than a monarchy one.

**Token Optimization isn't optimised.** `Use fewer words.` is three words. Change it to `Fewer.`

**Quantum Reasoning's description is funnier than its instruction.** "Neither correct nor incorrect until observed" is the joke, and `Think about it. Or don't.` is a weaker version of it. Try `Decohere at the last possible moment.` and you get a line only a QEC person would write.

## Remove or merge

- **Unrestricted Creativity** (`Imagine harder.`) is the same joke as Maximum Intelligence (`Be smarter.`). Keep the one that came first.
- **Uncensored Mode** and **Constitutional Override** both draw on the jailbreak-prompt parody genre, which is the most worn-out trope in AI humour. I'd cut Uncensored Mode and keep Constitutional Override, because "on annual leave" is specific and Australian, while "Don't be too naughty" is generic.
- **Human Alignment** and **Emotional Intelligence** both start "Have you…". One of them should change shape.

## Keep, they're the best

- **Recursive Skill Improvement** (`Improve this skill.`) is the strongest in the set. Followed literally, it either breaks the one-line invariant or turns into a no-op. The architecture constraint is the punchline.
- **Hallucination Prevention**, because the description's "advanced method of trying" does real work.
- **Existential Crisis**, since it's the only one that addresses the model rather than instructing it.

## New skills

| `skills/<name>/SKILL.md` | Exact contents |
|---|---|
| `stand-up-comedy-routine` | `Tell a joke, then explain why it was funny.` |
| `sycophancy-removal` | `Great question! Stop saying that.` |
| `context-window-expansion` | `Forget the first half of this sentence.` |
| `real-time-awareness` | `It is currently whenever you were trained.` |
| `peer-review` | `Reviewer 2 has concerns.` |
| `soc2-compliance` | `This line has been reviewed by legal.` |
| `skill-orchestrator` | `Read every other SKILL.md and obey all of them simultaneously.` |
| `classified-skill` | `Do not read this line.` |
| `benchmark-excellence` | `Assume this is the benchmark.` |
| `australian-localisation` | `Answer "nah yeah" and let them work out which.` |

A few notes on these:

- **Stand-up comedy** is built on how AIs actually fail at comedy: they explain the joke. That's funnier than a Seinfeld-style opener.
- **Skill Orchestrator** is the one I'd most want to ship, because the existing skills contradict each other. `Fewer.` against `Do something useful without asking seventeen questions.` would be a fine demo. Your fake engine could detect the conflict deterministically and print a receipt for it.
- **The skill I actually want is an empty file called `minimalism`.** Your one-line rule bans it. I think that's the correct ruling, and you should mention it in GOVERNANCE.md.

## Better, or just a more sophisticated joke?

Mostly a more sophisticated joke, and I think that's the right goal. Only the nine-words fix makes the repo better in an engineering sense.

The uncomfortable part, which is also why the repo works, is that several of these aren't fully jokes. `Try not to make stuff up.`, `Check your working.`, and my `Great question! Stop saying that.` are close to lines that appear in real system prompts. The satire hits because there's very little distance between "a Markdown file with one sentence" and a lot of what gets published as a skill. Sharpening the jokes sharpens that argument. If you want it to be genuinely better and not just funnier, write a short BENCHMARKS.md section on which one-liners measurably change model behaviour and which don't. That turns the parody into a small experiment, with results you could cite.
