---
name: application-answers
description: Draft cover letters and application-form answers (why this firm, why this role, competency/STAR questions, strengths) in the user's own voice. Use when an application form or cover letter needs writing.
---

## Steps
1. Get the exact question text and word/character limit. Get the job ad or link.
2. Research the firm in 5 minutes: what the division actually does, 1–2 recent concrete facts (deal, product, results, initiative) with a source link. Never invent facts; cite what you used.
3. Pull evidence only from `career/profile.md` and `career/cv-master.md`. If the best story isn't there, ask one question to get it.
4. Draft to the limit (aim 90–100% of it):
   - **Why firm:** specific fact → why it matters to them → link to their experience. No generic "global leader" lines.
   - **Why role:** what the job is day to day → evidence they'd enjoy and be good at it.
   - **Competency (STAR):** Situation 1 line, Task 1 line, Action is the bulk ("I", not "we"), Result with a number + what they learned.
5. Remove AI tells: no "delve", "passionate", "I am excited to", "furthermore", em-dash chains, or tricolon lists. Read like a sharp 20-year-old, not a brochure.
6. Save to `career/answers/<company>.md` (question, answer, word count, sources) and log it: `tracker.py update ID --stage drafting --note "answers drafted"`.

Remind once: they must edit it into their own words before submitting; many firms check for AI-written answers.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
