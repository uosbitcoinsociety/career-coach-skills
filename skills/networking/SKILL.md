---
name: networking
description: Draft short outreach to alumni, recruiters and employees (LinkedIn, email), thank-you notes and follow-ups, and track who to chase. Use when someone wants to reach out to people at a firm or follow up after an event or interview.
---

## Steps
1. Find out who (name, role, firm, how they're connected: same uni, society, event) and the goal (15-min chat, referral, advice, thank-you).
2. Draft the message:
   - LinkedIn connection note: ≤300 characters. One line who you are, one line the specific connection, one concrete ask.
   - Email: subject line that says why ("Sheffield maths student – question about rates sales"), ≤120 words, one ask, easy to say yes to (offer 2 time windows).
   - Thank-you after interview: within 24h, ≤80 words, one specific thing from the conversation.
3. Follow-up cadence: one polite nudge after 7 days, then stop.
4. Log against the application if relevant: `tracker.py update ID --note "Messaged <name> (<role>) on <date>" --next "follow up <name>" --next-date <date+7>`.

Never send anything yourself. Never ask for a job directly in a first message.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
