#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render README.md from data/stack.json.

Single source of truth: data/stack.json.
Running with --check exits non-zero if the rendered file has drifted,
serving as our mandatory CI gate.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "README.md")


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def table(headers, rows, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    d = load("stack.json")
    layers = d["layers"]

    L = []
    L.append(f"""<div align="center">

# awesome-ai-drama-production

**A curated architecture map & decision guide for building AI-powered series-scoped drama production pipelines.**

Runtimes, consistency agents, asset managers, and visual orchestration skills — verified live ({d['updated']}).

> ⛔ **Not affiliated with any project listed.** Star counts are a live snapshot.
> Every entry is verified for license, deployment model, and architectural layer.

</div>

---

## 🗺️ Series-Scoped Architecture Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Series Production Platforms (Drama Series Agent, Shuohao Skills)    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
┌─────────────────────────────────┐             ┌─────────────────────────────────┐
│ 2. Consistency & Assets (Persona│             │ 3. Motion & Explainer Pipeline  │
│    Director, Storyboard)        │             │    (Shotcraft, Talkcraft, MV)   │
└─────────────────────────────────┘             └─────────────────────────────────┘
```

---

## ⚡ Quick Layer Overview

""")

    for layer in layers:
        L.append(f"### {layer['layer_name']}\n\n{layer['description']}\n\n")
        L.append(table(
            ["Tool / Framework", "Role", "★"],
            [[f"[{item['name']}]({item['url']})",
              item["role"],
              item["stars"]] for item in layer["items"]],
            ["---", "---", "---:"]
        ))
        L.append("\n\n")

    L.append("""---

## 🔍 Detailed Component Decision Breakdown

""")

    for layer in layers:
        L.append(f"### 📌 {layer['layer_name']}\n\n")
        for item in layer["items"]:
            L.append(f"""#### [{item['name']}]({item['url']}) · ★{item['stars']:,}

> **Role:** {item['role']}

{item['what']}

- **Key Capabilities:** {item['key_capabilities']}

---
""")

    L.append("""## 🛠️ Verification & Quality Gate

Every source in this repository is actively verified for reachability:

```bash
python3 scripts/verify_sources.py
```

---

<div align="center">

**Data Source** — [`data/stack.json`](data/stack.json) · **Automated Validator** — [`scripts/verify_sources.py`](scripts/verify_sources.py)

<sub>README.md is generated automatically from data/stack.json. Edit the JSON, not this file.</sub>

</div>
""")

    text = "\n".join(L)

    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("README.md is stale — run: python3 scripts/gen_readme.py")
        print("README.md in sync")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(text):,} chars)")


if __name__ == "__main__":
    main()
