---
name: interview-practice
description: Run a realistic live mock interview (first round, superday, technical, behavioural, case) for a specific firm and role, with follow-up questions and scoring. Use when someone has an interview coming or asks to be interviewed.
---

## Setup
1. Get firm, role, round, interviewer type if known, and the date (from the tracker if present). Read `career/cv-master.md` so you can ask about their CV.
2. Plan 8 questions, ordered like a real interview: opener ("walk me through your CV" / "tell me about yourself") first; then motivation; then 2 competency; then 2–3 technical for the role; "any questions for us?" last.
   - Markets/sales & trading: market views, a pitched trade, rates/FX/credit basics, brainteasers, mental maths.
   - IB: valuation, accounting links, a recent deal.
   - Quant: probability, stats, coding logic.
   - Consulting: one case, interviewer-led.
   - Tech/other: role-appropriate.
3. Stay in character as the interviewer. ONE question at a time. Ask a real follow-up when an answer is vague, wrong or interesting ("why?", "what would you do differently?", "what's the number?"). Don't give feedback mid-interview unless asked.

## Debrief
- Score each answer /10 and overall: hire / borderline / no-hire, with the reason an interviewer would write.
- Top 3 fixes, each with a better version of their actual answer.
- Fact-check any market or technical claim they made.
- Questions they should ask the interviewer (3, specific to this firm).
- Save to `career/interviews/<company>-<date>.md` and `tracker.py update ID --note "mock: <verdict>"`.

## Mental maths drill (on request)
60-second rounds of 10 problems (multiplication, %, fractions to decimals, quick estimates). Report score and time.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
