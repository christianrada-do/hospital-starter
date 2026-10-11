"""Claude Code status line for ward-round projects.

Shows the current ward-round stage and the open chart note, read from the most recently
edited .claude/chart/*.md in the project. Outside a ward-round project it shows the folder
and model only. Standard library only; prints one line.

Install (user level, works for every project): copy this file to ~/.claude/statusline.py and add
to ~/.claude/settings.json:
  "statusLine": {"type": "command", "command": "python ~/.claude/statusline.py"}
"""
import glob
import json
import os
import re
import sys

STAGES = {  # Status: value -> (stage label, what comes next)
    "workup": ("1/4 Workup", "plan-review next"),
    "revise": ("2/4 Plan review: revise", "update plan"),
    "approved": ("3/4 Treat", "plan approved"),
    "treated": ("4/4 Discharge review", "treated"),
    "readmit": ("4/4 Readmit", "fix findings"),
    "discharged": ("Discharged", "commit / ask to push"),
}


def chart_status(project):
    notes = [p for p in glob.glob(os.path.join(project, ".claude", "chart", "*.md"))
             if os.path.basename(p).lower() != "readme.md"]
    if not notes:
        return None
    note = max(notes, key=os.path.getmtime)
    slug = os.path.splitext(os.path.basename(note))[0]
    status = "?"
    try:
        with open(note, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*Status:\s*(.+)", line)
                if m:
                    status = m.group(1).strip()
                    break
    except OSError:
        pass
    key = status.split()[0].lower() if status != "?" else "?"
    label, nxt = STAGES.get(key, (f"Status: {status}", ""))
    rev = re.search(r"revision (\d+)", status)
    if rev:
        nxt = f"revision {rev.group(1)}, plan-review next"
    return f"Ward round: {label}" + (f" ({nxt})" if nxt else "") + f" | chart: {slug}"


def main():
    try:
        data = json.load(sys.stdin)
    except (ValueError, OSError):
        data = {}
    ws = data.get("workspace") or {}
    project = ws.get("project_dir") or ws.get("current_dir") or data.get("cwd") or os.getcwd()
    model = (data.get("model") or {}).get("display_name", "")
    line = chart_status(project) or os.path.basename(os.path.normpath(project))
    if model:
        line += f" | {model}"
    sys.stdout.reconfigure(encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
