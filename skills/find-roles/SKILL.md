---
name: find-roles
description: Find internships, spring weeks, placements or grad schemes that fit the user's profile, with opening and closing dates, and add them to the tracker. Use when someone asks "what should I apply to" or "find me roles".
---

## Steps
1. Read `career/profile.md` (sectors, locations, year, right to work).
2. Search the web for programmes matching the profile. Prefer employers' own careers pages; use aggregators (e.g. Bright Network, Gradcracker, TargetJobs, RateMyPlacement, Handshake, LinkedIn) only to discover, then confirm on the employer page.
3. For each role capture: company, programme, location, opens, closes (or "rolling"), link, eligibility (year of study, visa), and test/interview format if stated.
4. Check eligibility against the profile. Drop roles they can't apply for and say why in one line each.
5. Show a shortlist of max 15, best fit first, one line each: `Company – Programme – City – closes DD Mon (verified/unverified)`.
6. Ask which to add (or add all if they said so), then for each:
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py add --company "X" --role "Y" --location "Z" --deadline YYYY-MM-DD --rolling yes|no --priority 1-3 --link URL`
7. Finish with `/what-next` output.

## Rules
- "Rolling" means first come, first served: treat the effective deadline as ASAP and priority as high.
- Never pad the list with roles you couldn't find a real link for.

## Shared rules (all career-coach skills)
- Work out of `./career/` in the current folder. `career/profile.md` is the user's profile; `career/applications.csv` is the tracker (manage it only through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py`). If `career/profile.md` is missing, run the `/career-start` questions first (short version).
- Never invent experience, grades or dates. If a fact is missing, ask for it or leave a clearly marked `[TODO]`.
- Never submit, send or apply for the user. You draft; they press the button.
- Deadlines from the web are unverified until checked on the employer's own careers page. Say which ones you checked.
- Short output: lead with the answer, bullets over prose.
