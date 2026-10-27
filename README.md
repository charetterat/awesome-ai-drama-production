<div align="center">

# awesome-ai-drama-production

**A curated architecture map & decision guide for building AI-powered series-scoped drama production pipelines.**

Runtimes, consistency agents, asset managers, and visual orchestration skills — verified live (2026-10-28).

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


### Series Production Platforms & Workflows

Orchestration frameworks that manage episodic state, characters, and consistency across multiple scenes/episodes.


| Tool / Framework | Role | ★ |
|---|---|---:|
| [Drama Series Agent](https://github.com/binwu1/drama-series-agent) | Orchestrator | 74 |
| [Shuohao Skills](https://github.com/eternityspring/shuohao-skills) | Creative Workflow | 4266 |



### Vision & Consistency Assets

Skills and agents focused specifically on maintaining character likeness and visual style across shots.


| Tool / Framework | Role | ★ |
|---|---|---:|
| [Persona Director](https://github.com/18yz153/ComfyUI-Persona-Director) | Pipeline Component | 22 |
| [Template AI Storyboard](https://github.com/Sri01729/template-ai-storyboard-consistent-character) | Pipeline Component | 37 |



### Motion & Explainer Infrastructure

Production pipelines for turning text/scripts into cinematic visual assets.


| Tool / Framework | Role | ★ |
|---|---|---:|
| [Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Pipeline Component | 10750 |
| [Video Talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | Pipeline Component | 1410 |
| [Vocaloid-Style Pipeline](https://github.com/EGSECDA/vocaloid-style-mv-pipeline) | Pipeline Component | 70 |



---

## 🔍 Detailed Component Decision Breakdown


### 📌 Series Production Platforms & Workflows


#### [Drama Series Agent](https://github.com/binwu1/drama-series-agent) · ★74

> **Role:** Orchestrator

Series-scoped Agent (Idea → Script → Cast → MiniMax/Ref2VA) that focuses on episodic serialization, character definitions, and asset reuse.

- **Key Capabilities:** MiniMax H3 integration, Reference-to-Video (Ref2VA) consistency, multi-scene continuity.

---

#### [Shuohao Skills](https://github.com/eternityspring/shuohao-skills) · ★4,266

> **Role:** Creative Workflow

Modular skills for short drama production: storyboarding, character consistency (Cast), asset generation, script-to-scene planning.

- **Key Capabilities:** Role-play agent architecture, modular narrative skillsets, asset cataloging.

---

### 📌 Vision & Consistency Assets


#### [Persona Director](https://github.com/18yz153/ComfyUI-Persona-Director) · ★22

> **Role:** Pipeline Component

ComfyUI node/agent pipeline ensuring character consistency in series rendering.

- **Key Capabilities:** Persona-based conditioning, multi-stage consistency checkpoints.

---

#### [Template AI Storyboard](https://github.com/Sri01729/template-ai-storyboard-consistent-character) · ★37

> **Role:** Pipeline Component

Comprehensive storyboard system for managing persistent character visual cues.

- **Key Capabilities:** Persistent visual metadata, style-transfer alignment.

---

### 📌 Motion & Explainer Infrastructure


#### [Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft) · ★10,750

> **Role:** Pipeline Component

Studio-grade cinematic video generator for Claude Code/Codex with 150+ camera recipe cards.

- **Key Capabilities:** Camera orchestration, motion-design, Remotion-native pipeline.

---

#### [Video Talkcraft](https://github.com/Vincentwei1021/video-talkcraft) · ★1,410

> **Role:** Pipeline Component

Voiceover-driven explainer studio. Syncs phonetic subtitles, typography, and B-roll callouts.

- **Key Capabilities:** Whisper/TTS alignment, kinetic typography.

---

#### [Vocaloid-Style Pipeline](https://github.com/EGSECDA/vocaloid-style-mv-pipeline) · ★70

> **Role:** Pipeline Component

Production pipeline and Claude Code skill specifically for MV (Music Video) production workflows.

- **Key Capabilities:** MV-production sequencing, multi-node staging.

---

## 🛠️ Verification & Quality Gate

Every source in this repository is actively verified for reachability:

```bash
python3 scripts/verify_sources.py
```

---

<div align="center">

**Data Source** — [`data/stack.json`](data/stack.json) · **Automated Validator** — [`scripts/verify_sources.py`](scripts/verify_sources.py)

<sub>README.md is generated automatically from data/stack.json. Edit the JSON, not this file.</sub>

</div>
