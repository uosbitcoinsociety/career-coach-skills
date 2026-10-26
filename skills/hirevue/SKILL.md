---
name: hirevue
description: Practise one-way video interviews (HireVue, Sonru, Launchpad, Cappfinity video) with timed questions and scored feedback. Use when someone has a video interview invite or wants to rehearse one.
---

## How a session works
1. Read the firm and role from the tracker or ask. Generate 6 questions in the real format: 2 motivation (why firm/role), 2 competency (STAR), 1 commercial/market awareness, 1 role-technical. Order: motivation first.
2. Present ONE question at a time, in the platform's format: "Question 2 of 6. You have 30 seconds to prepare and 2 minutes to answer."
3. The user answers by typing, or by recording and pasting a transcript. If they want to speak aloud, suggest: record on their phone/laptop, then transcribe (e.g. their OS dictation or Whisper) and paste.
4. After each answer score /10 on:
   - **Structure** (clear opening line, STAR or point-reason-example, ending)
   - **Content** (specific, firm-specific, evidence, numbers)
   - **Delivery** (estimated length vs 2 min ≈ 250–300 words; filler words; hedging)
   Then: 2 things that worked, the 1 fix that matters most, and a 90-second model answer built from THEIR experience.
5. After the set: average score, weakest question type, and whether to re-do the weakest one now.
6. Log it: `tracker.py update ID --note "HireVue practice avg X/10"`.

## Platform tips (say once)
Look at the camera not the screen, laptop at eye level, light in front, plain background, notes as 3 keywords max, use the practice question, don't redo-hunt when retakes aren't allowed.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
