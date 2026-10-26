---
name: online-tests
description: Prepare for online assessments - numerical, verbal, logical/inductive, situational judgement (SJT), and game-based tests (e.g. SHL, Cappfinity, Pymetrics-style). Use when someone has a test invite or wants practice.
---

## Steps
1. Ask (or read from the tracker note) which firm and test type, and the deadline.
2. Explain the format in 3 bullets: question types, timing per question, what's scored.
3. Run a practice set of 8 questions in the matching style, ONE at a time. Wait for the answer, then mark it and explain the fastest method.
   - Numerical: tables/charts given as text, % change, ratios, currency conversion. Show the shortcut, not just the answer.
   - Verbal: passage + True / False / Cannot Say. Explain why "Cannot Say" traps people.
   - Logical: describe sequences of shapes in text; teach the rule-hunting order (count, rotate, alternate, position).
   - SJT: score each response option against the firm's published values.
4. End with a score, the error pattern, and 2 drills to fix it.
5. Day-of tips (once, short): quiet room, calculator + paper for numericals, do it well before the deadline, don't skip, practice tests on the provider site.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
