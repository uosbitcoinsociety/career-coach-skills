---
name: tracker
description: Add, update and review job/internship applications in the local tracker (career/applications.csv). Use when someone says they applied, got a test, interview, rejection or offer, or wants to see their applications.
---

The tracker is a CSV the user can open in any spreadsheet app. Always change it through the script, never by hand-editing:

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py init
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py add --company C --role R [--location L] [--deadline YYYY-MM-DD] [--rolling yes] [--priority 1|2|3] [--link URL] [--effort-hours N]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py update ID [--stage STAGE] [--deadline ...] [--next "step"] [--next-date YYYY-MM-DD] [--note "..."]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py list [--all]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py next [--hours N]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py stats
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py ics
```

Stages, in order: `todo`, `drafting`, `applied`, `test`, `video`, `interview`, `assessment-centre`, `offer`, plus terminal `rejected`, `withdrawn`, `accepted`.

## When the user reports news
- "Applied to X" → `update ID --stage applied --next "chase / wait for test" --next-date <today+14>`
- "Got a HireVue/online test" → stage `video`/`test`, `--next-date` = the invite's deadline, then offer `/hirevue` or `/online-tests`.
- "Interview on <date>" → stage `interview`, next-date = that date, then offer `/interview-practice` for that firm.
- Rejection → stage `rejected`, `--note` with the stage reached and any feedback. Say one line on what to learn, nothing more.
- `ics` writes `career/deadlines.ics` for import into any calendar.
Show the updated `list` after changes.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
