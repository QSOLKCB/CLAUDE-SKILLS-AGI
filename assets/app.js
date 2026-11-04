import { infer, DEFAULT_SEED } from "./engine.js";

const $ = (id) => document.getElementById(id);
const list = $("skill-list");
const form = $("prompt-form");
let skills = [];
let selected = "auto";
let lastReceipt = null;

function make(tag, className, value) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined) node.textContent = value;
  return node;
}

function chosenSkill() {
  return skills.find((item) => item.id === selected);
}

function displaySelection() {
  const current = chosenSkill();
  $("active-skill").textContent = current ? current.name : "Auto orchestration";
  $("skill-instruction").textContent = current
    ? current.instruction : "Automatic routing by keywords. No transformer required.";
  renderSkills();
}

function renderSkills() {
  const query = $("skill-search").value.toLowerCase().trim();
  const items = [{ id: "auto", name: "Auto orchestration", description: "The world's most confident keyword router." }, ...skills];
  list.replaceChildren();
  let visible = 0;
  for (const item of items) {
    if (!(item.name + " " + item.id + " " + item.description).toLowerCase().includes(query)) continue;
    visible++;
    const button = make("button", "skill-choice" + (item.id === selected ? " is-selected" : ""));
    button.type = "button";
    button.setAttribute("aria-pressed", String(item.id === selected));
    button.append(make("strong", "", item.name), make("span", "", item.description));
    button.addEventListener("click", () => { selected = item.id; displaySelection(); });
    list.append(button);
  }
  if (!visible) list.append(make("p", "loading", "No groundbreaking capabilities found."));
  $("skill-count").textContent = String(skills.length).padStart(2, "0");
}

function addMessage(role, text, meta) {
  const entry = make("div", "chat-entry " + role);
  entry.append(make("span", "who", role === "user" ? "You" : "Platinum Reasoner"));
  entry.append(make("div", "bubble", text));
  if (meta) entry.append(make("span", "meta", meta));
  $("chat-stage").append(entry);
  $("chat-stage").scrollTop = $("chat-stage").scrollHeight;
}

function runInference(prompt) {
  const value = prompt.trim();
  if (!value) return;
  try {
    const result = infer(value, selected, $("seed").value || DEFAULT_SEED, skills);
    if ($("chat-stage").querySelector(".welcome")) $("chat-stage").replaceChildren();
    addMessage("user", value);
    addMessage("assistant", result.output, result.skill.name + " · FNV1A/" + result.hash);
    $("hash").textContent = result.hash;
    $("routed").textContent = result.skill.id;
    $("intent").textContent = result.intent;
    $("status").textContent = "Inference complete. 0 GPU-hours consumed.";
    lastReceipt = result.receipt;
    $("copy-receipt").disabled = false;
    $("prompt").value = "";
  } catch (error) {
    $("status").textContent = "Inference halted: " + error.message;
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  runInference($("prompt").value);
});

$("prompt").addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    form.requestSubmit();
  }
});

$("skill-search").addEventListener("input", renderSkills);
$("reset-chat").addEventListener("click", () => {
  $("chat-stage").replaceChildren(make("div", "welcome",
    "Session cleared. As a stateless engine, I have forgotten nothing because I never remembered anything."));
  $("hash").textContent = "—";
  $("routed").textContent = "—";
  $("intent").textContent = "—";
  $("status").textContent = "Conversation display cleared. No inference state exists.";
  lastReceipt = null;
  $("copy-receipt").disabled = true;
  $("prompt").focus();
});

$("copy-receipt").addEventListener("click", async () => {
  if (!lastReceipt) return;
  try {
    await navigator.clipboard.writeText(JSON.stringify(lastReceipt, null, 2) + "\n");
    $("status").textContent = "Receipt copied. It contains no timestamp or private server-side state.";
  } catch {
    $("status").textContent = "Clipboard unavailable. Browser permission required.";
  }
});

for (const chip of document.querySelectorAll("[data-prompt]")) {
  chip.addEventListener("click", () => {
    $("prompt").value = chip.dataset.prompt;
    $("prompt").focus();
  });
}

async function init() {
  try {
    const response = await fetch(new URL("../data/skills.json", import.meta.url));
    if (!response.ok) throw new Error("HTTP " + response.status);
    const manifest = await response.json();
    if (manifest.schema_version !== "1" || !Array.isArray(manifest.skills) || !manifest.skills.length)
      throw new Error("Unsupported skill manifest.");
    skills = manifest.skills;
    displaySelection();
    $("status").textContent = "Ready. All skills loaded locally; no inference API exists.";
  } catch (error) {
    list.replaceChildren(make("p", "loading", "Could not load local skills."));
    $("send").disabled = true;
    $("status").textContent = "Startup failed: " + error.message;
  }
}
init();
