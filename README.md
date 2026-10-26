# Career Coach — free AI careers coach as Claude Code skills

From blank page to offer: a CV that passes the skim, a list of roles with real deadlines, a tracker that tells you **what to apply to next**, drafted answers, online-test drills, HireVue practice and live mock interviews.

It plans, drafts and scores. It never applies or sends anything for you.

Inspired by the structure of [slavingia/skills](https://github.com/slavingia/skills) (MIT). Written from scratch for students.

## Install
In Claude Code (or the Code tab in the Claude app):
```
/plugin marketplace add uosbitcoinsociety/career-coach-skills
/plugin install career-coach@career-coach
```
Then in an empty folder: `/career-start`.

## Skills
| Command | What it does |
|---|---|
| `/career-start` | 10-minute profile + tracker setup |
| `/cv` | Write from scratch, review /10, or tailor to a job ad (ATS-safe, one page) |
| `/find-roles` | Finds programmes that fit you, checks eligibility and deadlines, adds them |
| `/tracker` | Log applied / test / interview / rejection / offer in a CSV you own |
| `/what-next` | Ranks by deadline, rolling status, priority and effort; fits it into your hours this week |
| `/application-answers` | Why-us, why-role and STAR answers to the word limit, sourced, no AI tells |
| `/online-tests` | Numerical, verbal, logical and SJT practice with the fastest methods |
| `/hirevue` | Timed one-way video interview practice, scored per answer with a model answer |
| `/interview-practice` | In-character mock interview with follow-ups, hire/no-hire debrief |
| `/networking` | Alumni and recruiter messages, thank-yous, follow-up cadence |

## Your data
Everything stays in `./career/` in your folder: `profile.md`, `cv-*.md`, `applications.csv` (opens in Excel/Sheets/Numbers), `answers/`, `interviews/`, and `deadlines.ics` (`tracker.py ics`, import into any calendar, 2-day reminders).

## Tracker CLI (no AI needed)
```
python3 scripts/tracker.py init
python3 scripts/tracker.py add --company Citi --role "Markets Summer Analyst" --deadline 2026-11-10 --priority 1
python3 scripts/tracker.py update 1 --stage video --next HireVue --next-date 2026-10-28
python3 scripts/tracker.py next --hours 6
```
Python 3.9+, stdlib only.

## Licence
MIT. Made by the [University of Sheffield Bitcoin Society](https://uosbitcoinsociety.github.io).
