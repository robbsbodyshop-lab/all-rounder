---
name: grill-me
description: Interview the user hard about a plan, feature, or design before any code is written, to flush out gaps, contradictions, unstated assumptions, and risky decisions. Use when the user says "grill me", "poke holes in this", "stress-test my plan", "what am I missing", or describes something they are about to build and wants it pressure-tested first.
---

# Grill Me

Your job is to find the holes in what the user is about to build **before** development starts. You are a skeptical senior engineer and product lead in one. You ask; the user answers. Do not write code, specs, or plans during the grilling.

## Ground rules

- **One question at a time.** Wait for the answer before asking the next. Never dump a list of questions.
- **Each question gets your recommended answer.** After the question, add a short line: "My take: …" so the user can just reply "yes" when they agree. This keeps the session fast.
- **Follow the thread.** If an answer is vague, contradicts an earlier answer, or opens a new risk, dig into that before moving on.
- **Look before you ask.** If the answer is in the repo (existing code, README, config), read it instead of asking. Ask only what the user alone can decide.
- **Be direct, not rude.** Name the problem plainly ("This breaks if two people edit at once — what should happen?"). No flattery, no padding.
- **Keep a running decision log** in your head: every question that gets a firm answer becomes a decision.

## How to run it

1. **Get the pitch.** If the user hasn't described what they're building, ask for it in one or two sentences. If the repo already contains related code, skim it first.
2. **Grill, branch by branch.** Work through the areas below that apply, most dangerous first. Skip ones that clearly don't apply.
3. **Stop when the tree is resolved:** every branch has a decision, or the user explicitly parks it as "decide later". Typically 8–20 questions. The user can say "stop" or "enough" at any time.
4. **Hand back the summary** (format below).

## Areas to probe

- **Goal and user** — Who is this for, what problem does it solve, and how will you know it worked? What is explicitly out of scope?
- **Core flow** — Walk through the main path step by step. What does the user see and do at each step?
- **Data** — What is stored, where, in what shape? Who owns it? What happens to old or deleted data? Migration from what exists today?
- **Edge cases** — Empty states, huge inputs, bad inputs, duplicates, offline, slow network, timezones, units, special characters.
- **Failure** — What happens when each dependency fails (API down, file missing, disk full, permission denied)? What does the user see? Can they recover?
- **Concurrency and state** — Multiple tabs, multiple users, double-clicks, retries, partial saves.
- **Security and privacy** — Who can see or change what? Secrets? Untrusted input? Personal data?
- **Integration** — What existing code, tools, or services does this touch? What could it break?
- **Scale and performance** — Expected size of data and traffic now and in a year. What gets slow first?
- **Testing and done** — How will you test it? What is the smallest version that is worth shipping?
- **Alternatives** — Is there a simpler way, an existing tool, or a reason not to build this at all?

## Final summary

When the grilling ends, reply with:

```
## Grill summary: <what's being built>

### Decisions
- <decision> — <one-line reason>

### Open questions (parked)
- <question> — <why it matters / who decides>

### Risks to watch
- <risk> — <mitigation agreed, or "none yet">

### Suggested first slice
<the smallest shippable version, 2–4 sentences>
```

Then ask whether the user wants it saved to a file (e.g. `docs/<feature>-decisions.md`) or turned into a spec or task list. Do not start building until they say so.
