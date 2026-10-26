#!/usr/bin/env python3
"""career-coach application tracker. Stdlib only. Data: ./career/applications.csv

Commands: init | add | update | list | next | stats | ics
"""
import argparse, csv, datetime as dt, os, sys, tempfile

DIR = os.environ.get("CAREER_DIR", "career")
PATH = os.path.join(DIR, "applications.csv")
FIELDS = ["id", "company", "role", "location", "stage", "deadline", "rolling", "priority",
          "effort_hours", "next", "next_date", "link", "notes", "updated"]
OPEN = ["todo", "drafting", "applied", "test", "video", "interview", "assessment-centre", "offer"]
CLOSED = ["rejected", "withdrawn", "accepted"]
# stages where the next move is the user's (vs waiting on the firm)
ACTION = {"todo", "drafting", "test", "video", "interview", "assessment-centre", "offer"}
DEFAULT_EFFORT = {"todo": 3, "drafting": 2, "test": 1.5, "video": 1.5, "interview": 3,
                  "assessment-centre": 4, "offer": 0.5, "applied": 0}


def today():
    return dt.date.fromisoformat(os.environ["CAREER_TODAY"]) if os.environ.get("CAREER_TODAY") else dt.date.today()


def d(s):
    try:
        return dt.date.fromisoformat(s) if s else None
    except ValueError:
        sys.exit(f"bad date {s!r}: use YYYY-MM-DD")


def load():
    if not os.path.exists(PATH):
        sys.exit("No tracker yet: run `tracker.py init`")
    with open(PATH, newline="") as f:
        return list(csv.DictReader(f))


def save(rows):
    os.makedirs(DIR, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=DIR, suffix=".csv")
    with os.fdopen(fd, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    os.replace(tmp, PATH)


def find(rows, rid):
    for r in rows:
        if r["id"] == str(rid):
            return r
    sys.exit(f"no application with id {rid}")


def due(r):
    """The date that matters now: next_date for in-process items, deadline before applying."""
    nd, dl = d(r["next_date"]), d(r["deadline"])
    if r["stage"] in ("todo", "drafting"):
        return min([x for x in (dl, nd) if x], default=None)
    return nd or None


def score(r, t):
    """Higher = do sooner. Combines days left, rolling, priority and stage."""
    if r["stage"] not in ACTION:
        return None
    du = due(r)
    days = (du - t).days if du else 30
    if r["rolling"] == "yes" and r["stage"] in ("todo", "drafting"):
        days = min(days, 3)  # rolling: first come, first served
    urgency = 100 / (max(days, 0) + 1)
    pri = {"1": 1.5, "2": 1.0, "3": 0.6}.get(r["priority"] or "2", 1.0)
    stage_w = 1.3 if r["stage"] in ("test", "video", "interview", "assessment-centre", "offer") else 1.0
    return round(urgency * pri * stage_w, 1)


def effort(r):
    try:
        return float(r["effort_hours"])
    except (TypeError, ValueError):
        return DEFAULT_EFFORT.get(r["stage"], 2)


def stamp():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def cmd_init(a):
    if os.path.exists(PATH):
        print(f"exists: {PATH}")
        return
    save([])
    print(f"created {PATH}")


def cmd_add(a):
    rows = load()
    rid = str(max([int(r["id"]) for r in rows] or [0]) + 1)
    if a.deadline:
        d(a.deadline)
    rows.append({"id": rid, "company": a.company, "role": a.role, "location": a.location or "",
                 "stage": "todo", "deadline": a.deadline or "", "rolling": a.rolling,
                 "priority": a.priority, "effort_hours": a.effort_hours or "", "next": "apply",
                 "next_date": "", "link": a.link or "", "notes": "", "updated": stamp()})
    save(rows)
    print(f"added #{rid} {a.company} – {a.role}")


def cmd_update(a):
    rows = load()
    r = find(rows, a.id)
    if a.stage:
        if a.stage not in OPEN + CLOSED:
            sys.exit(f"stage must be one of {OPEN + CLOSED}")
        r["stage"] = a.stage
        if a.stage in CLOSED:
            r["next"], r["next_date"] = "", ""
    for k in ("deadline", "next_date"):
        v = getattr(a, k)
        if v is not None:
            d(v)
            r[k] = v
    for k in ("next", "priority", "link", "location", "rolling", "effort_hours"):
        v = getattr(a, k)
        if v is not None:
            r[k] = v
    if a.note:
        r["notes"] = (r["notes"] + " | " if r["notes"] else "") + f"{today().isoformat()}: {a.note}"
    r["updated"] = stamp()
    save(rows)
    print(f"updated #{r['id']} {r['company']} → {r['stage']}")


def fmt(r, t):
    du = due(r)
    left = f"{(du - t).days:+d}d" if du else ("rolling" if r["rolling"] == "yes" else "—")
    when = du.strftime("%d %b") if du else ""
    nxt = f" · next: {r['next']}" if r["next"] else ""
    return f"#{r['id']:>3} {r['company']} – {r['role']} [{r['stage']}] {when} ({left}){nxt}"


def cmd_list(a):
    rows, t = load(), today()
    show = rows if a.all else [r for r in rows if r["stage"] in OPEN]
    show.sort(key=lambda r: (due(r) or dt.date.max))
    if not show:
        print("nothing open")
    for r in show:
        print(fmt(r, t))


def cmd_next(a):
    rows, t = load(), today()
    ranked = [(score(r, t), r) for r in rows if r["stage"] in ACTION]
    ranked.sort(key=lambda x: -x[0])
    overdue = [r for s, r in ranked if due(r) and due(r) < t]
    budget, plan, cut = a.hours, [], []
    for s, r in ranked:
        if r in overdue:
            continue
        e = effort(r)
        (plan if e <= budget else cut).append((s, r, e))
        if e <= budget:
            budget -= e
    waiting = [r for r in rows if r["stage"] == "applied"]
    stale = [r for r in waiting if (t - d(r["updated"][:10])).days >= 14]
    if overdue:
        print("PAST DUE — check the careers page; if closed: `update ID --stage withdrawn`:")
        for r in overdue:
            print("  " + fmt(r, t))
    print(f"DO THIS WEEK ({a.hours:g}h available):")
    for s, r, e in plan:
        print(f"  {fmt(r, t)} · ~{e:g}h · score {s}")
    if not plan:
        print("  nothing actionable")
    if cut:
        print("DOESN'T FIT — drop or find time:")
        for s, r, e in cut:
            print(f"  {fmt(r, t)} · ~{e:g}h")
    if stale:
        print("WAITING 14+ DAYS — chase or assume no:")
        for r in stale:
            print("  " + fmt(r, t))


def cmd_stats(a):
    rows = load()
    from collections import Counter
    c = Counter(r["stage"] for r in rows)
    applied = sum(c[s] for s in OPEN[2:] + CLOSED)
    print(f"total {len(rows)} · applied+ {applied} · " + " · ".join(f"{k} {v}" for k, v in c.items()))
    if applied:
        past = sum(c[s] for s in ("test", "video", "interview", "assessment-centre", "offer", "accepted"))
        print(f"got past CV screen: {past}/{applied} ({100 * past // applied}%)")


def cmd_ics(a):
    rows, out = load(), os.path.join(DIR, "deadlines.ics")
    ev = []
    for r in rows:
        if r["stage"] not in OPEN:
            continue
        for k, label in (("deadline", "Deadline"), ("next_date", r["next"] or "Next step")):
            x = d(r[k])
            if x and not (k == "next_date" and r[k] == r["deadline"]):
                ev.append((f"{r['id']}-{k}", x, f"{label}: {r['company']} – {r['role']}", r["link"]))
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//career-coach//EN"]
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for uid, x, summ, link in ev:
        lines += ["BEGIN:VEVENT", f"UID:{uid}@career-coach", f"DTSTAMP:{now}",
                  f"DTSTART;VALUE=DATE:{x:%Y%m%d}", f"DTEND;VALUE=DATE:{x + dt.timedelta(days=1):%Y%m%d}",
                  f"SUMMARY:{summ}", f"URL:{link}" if link else "DESCRIPTION:", "BEGIN:VALARM",
                  "TRIGGER:-P2D", "ACTION:DISPLAY", f"DESCRIPTION:{summ}", "END:VALARM", "END:VEVENT"]
    lines.append("END:VCALENDAR")
    with open(out, "w") as f:
        f.write("\r\n".join(lines) + "\r\n")
    print(f"wrote {len(ev)} events to {out}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("init")
    x = s.add_parser("add")
    x.add_argument("--company", required=True); x.add_argument("--role", required=True)
    x.add_argument("--location"); x.add_argument("--deadline"); x.add_argument("--link")
    x.add_argument("--rolling", choices=["yes", "no"], default="no")
    x.add_argument("--priority", choices=["1", "2", "3"], default="2")
    x.add_argument("--effort-hours", dest="effort_hours")
    u = s.add_parser("update")
    u.add_argument("id")
    for k in ("stage", "deadline", "next", "link", "location", "note"):
        u.add_argument(f"--{k}")
    u.add_argument("--next-date", dest="next_date")
    u.add_argument("--priority", choices=["1", "2", "3"])
    u.add_argument("--rolling", choices=["yes", "no"])
    u.add_argument("--effort-hours", dest="effort_hours")
    l = s.add_parser("list"); l.add_argument("--all", action="store_true")
    n = s.add_parser("next"); n.add_argument("--hours", type=float, default=6)
    s.add_parser("stats"); s.add_parser("ics")
    a = p.parse_args()
    globals()[f"cmd_{a.cmd}"](a)


if __name__ == "__main__":
    main()
