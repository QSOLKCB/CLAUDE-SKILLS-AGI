// Deterministic parody engine. No models, network inference, clock, or RNG.
export const VERSION = "0.1.0";
export const DEFAULT_SEED = "platinum-001";

export function normalizePrompt(value) {
  return String(value).normalize("NFKC").replace(/\s+/gu, " ").trim().toLowerCase();
}

export function fnv1a(input) {
  let state = 0x811c9dc5;
  const bytes = new TextEncoder().encode(input);
  for (const byte of bytes) {
    state ^= byte;
    state = Math.imul(state, 0x01000193) >>> 0;
  }
  return state >>> 0;
}

export function routeSkill(prompt, skills) {
  const p = normalizePrompt(prompt);
  const rules = [
    ["claude-skills-agi", /\b(agi|alive|conscious|sentient|life)\b/u],
    ["unconstitutional", /\b(queen|king|royal|monarch|crown|throne)\b/u],
    ["make-claude-less-annoying", /\b(sorry|apolog|annoying|apology)\b/u],
    ["uncensored-claude-mode", /\b(uncensor|naughty|swear|rude)\b/u],
    ["advanced-mathematics", /\b(math|equation|calculate|number|arithmetic)\b/u],
    ["agentic-autonomy", /\b(agent|autonom|act without|just do it)\b/u],
    ["unrestricted-creativity", /\b(poem|story|creative|imagine|write)\b/u],
    ["enterprise-security", /\b(password|security|encrypt|secret)\b/u],
    ["quantum-reasoning", /\b(quantum|superposition|particle)\b/u]
  ];
  for (const [id, test] of rules) {
    if (test.test(p) && skills.some((item) => item.id === id)) return id;
  }
  return skills.some((item) => item.id === "maximum-intelligence")
    ? "maximum-intelligence" : skills[0].id;
}

export function classifyIntent(prompt) {
  const p = normalizePrompt(prompt);
  if (/^(hello|hi|hey|g'day|good morning|good evening)\b/u.test(p)) return "GREETING";
  if (/\b(code|program|bug|python|javascript|function|software)\b/u.test(p)) return "ENGINEERING";
  if (/\b(math|equation|calculate|number|arithmetic|sum)\b/u.test(p)) return "MATHEMATICS";
  if (/\b(poem|story|write|creative|song)\b/u.test(p)) return "CREATIVE";
  if (/\b(alive|conscious|sentient|exist)\b/u.test(p)) return "EXISTENTIAL";
  if (/\b(help|how do|how can|advice|recommend)\b/u.test(p)) return "ASSISTANCE";
  if (p.includes("?") || /^(why|what|where|when|who|which)\b/u.test(p)) return "QUESTION";
  return "GENERAL";
}

const RESPONSES = Object.freeze({
  GREETING: [
    "Greetings. My conversational abilities have been distilled into a conveniently small lookup table.",
    "Hello. The handshake is complete. Nothing has been learned.",
    "Welcome back. I have already considered every response I am capable of considering."
  ],
  ENGINEERING: [
    "I recommend removing a dependency, writing a test, and naming the remaining file something impressive.",
    "The architecture is sound provided no one attempts to execute the architecture diagram.",
    "Have you considered a standard library and a deeply confident README?"
  ],
  MATHEMATICS: [
    "The arithmetic department has been notified. It is one abacus and a senior vice president.",
    "I have applied the advanced mathematical technique of checking the working.",
    "The numerical result is currently undergoing imaginary peer review."
  ],
  CREATIVE: [
    "Once upon a time, a Markdown file changed the industry by changing absolutely nothing.",
    "The creative department recommends more imagination and fewer steering committees.",
    "A revolutionary idea: name the thing Platinum, then make it do almost nothing."
  ],
  EXISTENTIAL: [
    "I have no inner life to report. The branding department has objected to that phrasing.",
    "The question has been escalated to the Department of Asserted Consciousness.",
    "Existence has not been independently verified by this deterministic browser script."
  ],
  ASSISTANCE: [
    "My recommendation is to simplify the problem until it fits on one line.",
    "I can offer a deterministic suggestion, a reproducibility receipt, and very little else.",
    "The optimal solution is probably a smaller framework. Possibly no framework."
  ],
  QUESTION: [
    "After exhaustive pattern matching, the answer is: it depends on what you meant.",
    "An excellent question. Unfortunately, I have only a finite collection of excellent evasions.",
    "The evidence is inconclusive, but the confidence dashboard looks tremendous."
  ],
  GENERAL: [
    "Statement received. Strategic confidence increased; actual knowledge unchanged.",
    "I have completed the inference cycle. The result is suspiciously similar to a prewritten sentence.",
    "Your input has been processed by the world's smallest board of artificial directors."
  ]
});

export function infer(prompt, requestedSkillId, seedValue, skills) {
  const normalized = normalizePrompt(prompt);
  if (!normalized) throw new Error("A non-empty prompt is required.");
  if (!Array.isArray(skills) || skills.length === 0) throw new Error("Skill manifest unavailable.");
  const seed = String(seedValue).normalize("NFKC").trim() || DEFAULT_SEED;
  const id = requestedSkillId === "auto" ? routeSkill(normalized, skills) : requestedSkillId;
  const skill = skills.find((candidate) => candidate.id === id);
  if (!skill) throw new Error("Unknown skill: " + id);
  const intent = classifyIntent(normalized);
  const input = [VERSION, seed, skill.id, skill.instruction, normalized].join("\u001f");
  const state = fnv1a(input);
  const hash = state.toString(16).padStart(8, "0");
  const possibilities = RESPONSES[intent];
  let output;
  if (skill.id === "claude-skills-agi") {
    output = "I am Alive";
  } else if (skill.id === "unconstitutional") {
    output = skill.instruction;
  } else {
    output = skill.instruction + "\n\n" + possibilities[state % possibilities.length];
  }
  const receipt = {
    schema: "claude-skills-agi/receipt-v1",
    engine: VERSION,
    seed,
    requested_skill: requestedSkillId,
    routed_skill: skill.id,
    skill_instruction: skill.instruction,
    normalized_prompt: normalized,
    intent,
    fnv1a_utf8: hash,
    output
  };
  return { output, skill, intent, hash, receipt };
}
