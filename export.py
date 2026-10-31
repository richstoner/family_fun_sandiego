#!/usr/bin/env python3
"""Build events.json for the public page from a directory of exported event docs.

Usage: python3 export.py <dir-of-event-json-files> <lastRun ISO> [mode]
Drops events the family marked booked/dismissed, drops past events,
strips private fields, and marks events seen in the latest run as isNew.
"""
import json, sys, pathlib, datetime
PUBLIC = ["title","category","urgency","start","end","whenText","venue","area",
          "fit","onSale","caveat","tags","url","source"]
src, last_run = pathlib.Path(sys.argv[1]), sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else "update"
today = datetime.date.fromisoformat(last_run[:10])
out = []
for f in sorted(src.glob("*.json")):
    d = json.loads(f.read_text())
    d = d.get("data", d)
    if d.get("status") in ("booked", "dismissed"):
        continue
    last = d.get("end") or d.get("start")
    if last and datetime.date.fromisoformat(last) < today:
        continue
    e = {k: d[k] for k in PUBLIC if k in d}
    e["id"] = f.stem
    e["isNew"] = d.get("status") == "new"
    out.append(e)
json.dump({"lastRun": last_run, "mode": mode, "events": out},
          open("events.json", "w"), indent=1, ensure_ascii=False)
print(f"wrote events.json with {len(out)} events")
