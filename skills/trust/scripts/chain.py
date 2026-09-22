#!/usr/bin/env python3
"""Say where a trust run stands, read from disk.

The five steps leave five traces: `.veebee/idea.md` (eureka), `product.md`
(define), `style.md` and `design/` (style), `tickets/` (ticketise), and the
`status: done` lines inside those tickets (autopilot). A run can be interrupted
and picked up again, so this is the only source of truth.

    python3 chain.py [project-root]           # text
    python3 chain.py [project-root] --json    # for the canvas

Nothing is written.
"""
import json
import os
import re
import sys


def head(path, size=2000):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read(size)
    except OSError:
        return ""


def title_of(veebee):
    for name in ("product.md", "idea.md"):
        text = head(os.path.join(veebee, name))
        for pattern in (r"^title:\s*(.+)$", r"^#\s+(.+)$"):
            found = re.search(pattern, text, re.M)
            if found:
                return found.group(1).strip()
    return ""


def tickets(veebee):
    folder = os.path.join(veebee, "tickets")
    if not os.path.isdir(folder):
        return []
    out = []
    for name in sorted(os.listdir(folder)):
        if not re.match(r"^\d+-.*\.md$", name):
            continue
        text = head(os.path.join(folder, name))
        found = re.search(r"^title:\s*(.+)$", text, re.M)
        out.append({
            "id": name.split("-")[0],
            "title": found.group(1).strip() if found else name,
            "done": bool(re.search(r"^status:\s*done\s*$", text, re.M)),
        })
    return out


def run(root):
    veebee = os.path.join(root, ".veebee")
    has = lambda *p: os.path.exists(os.path.join(veebee, *p))
    drawn = os.path.isdir(os.path.join(veebee, "design")) and bool(os.listdir(os.path.join(veebee, "design")))
    tk = tickets(veebee)
    decisions = head(os.path.join(veebee, "trust", "decisions.md"), 100000)

    steps = [
        {"key": "eureka", "label": "L'idée", "done": has("idea.md")},
        {"key": "define", "label": "Le produit", "done": has("product.md")},
        {"key": "style", "label": "Le look", "done": has("style.md"), "note": "dessiné" if drawn else ("charte seule" if has("style.md") else "")},
        {"key": "ticketise", "label": "Les tickets", "done": bool(tk), "note": f"{len(tk)}" if tk else ""},
        {"key": "autopilot", "label": "Le build", "done": bool(tk) and all(t["done"] for t in tk),
         "note": f"{sum(t['done'] for t in tk)}/{len(tk)}" if tk else ""},
    ]
    for step in steps:
        step["current"] = False
    for step in steps:
        if not step["done"]:
            step["current"] = True
            break

    return {
        "title": title_of(veebee),
        "steps": steps,
        "tickets": tk,
        "decisions": len(re.findall(r"^## ", decisions, re.M)),
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    data = run(args[0] if args else ".")
    if "--json" in sys.argv:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    print(data["title"] or "Sans titre")
    for step in data["steps"]:
        mark = "✓" if step["done"] else ("→" if step["current"] else "○")
        note = f"   {step['note']}" if step.get("note") else ""
        print(f"  {mark} {step['label']}{note}")
    print(f"\n{data['decisions']} décisions prises")


if __name__ == "__main__":
    main()
