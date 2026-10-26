---
name: what-next
description: Decide which applications to do first and build this week's plan from deadlines, rolling status, priority and effort. Use when someone asks "what should I do next", "what's due", or feels behind.
---

## Steps
1. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py next --hours <weekly hours from profile.md, default 6>`. It ranks open items by urgency score and fits them into the available hours.
2. Sanity-check the ranking with judgement:
   - Rolling + already open beats a fixed deadline 4+ weeks away.
   - Anything with a test/video/interview invite expiring in ≤3 days goes to the top.
   - Batch similar applications (same sector questions) on the same day.
   - Respect hard dates in profile.md (exams, travel).
3. Output, max 10 lines:
   - **Today:** 1–3 concrete actions with time estimates ("Write Citi 'why markets' answer, 40 min").
   - **This week:** the rest of the plan, by day.
   - **At risk:** anything that will be missed at the current pace, and what to drop instead.
4. If nothing is open, say so and suggest `/find-roles`.

No motivational filler. If they're behind, say exactly what to cut.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
