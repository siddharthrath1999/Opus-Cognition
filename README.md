<div align="center">
  <h1>🧠 Opus-Cognition</h1>
  <p>A production-ready repository containing the advanced Opus 4.6 framework and a curated suite of powerful AI agent skills.</p>
</div>

---

## 🌟 Overview

The **Opus 4.6 Cognitive Engine** is an advanced system prompt/framework designed to enforce high-reliability reasoning for Large Language Models. It implements a multi-stage pipeline that forces models to think, verify, critique, and calibrate before generating final output.

This repository bundles the Opus 4.6 instruction framework with **8 advanced, open-source skills** (plugins/tools capability documents) that you can drop directly into your IDE agents, custom workflows, or agentic frameworks.

## 🏗 System Architecture (Layout of Concepts)

The Opus 4.6 System operates on a strict **10-Stage Pipeline**:

1. **Problem Framing:** Extracts hidden assumptions and identifies missing data.
2. **Exploratory Reasoning:** Generates multiple reasoning paths (first-principles, contrarian, empirical).
3. **Verification Layer:** Cross-checks logical consistency and rejects ungrounded paths.
4. **Iterative Deepening:** Stress-tests assumptions through multiple cycles.
5. **Synthesis:** Constructs a unified model from verified paths.
6. **Self-Critique (Adversarial):** Actively looks for failure modes and flaws.
7. **Uncertainty Calibration:** Refuses to guess. Escalates ambiguity back to the user.
8. **Bias Check:** Evaluates cognitive framing bias.
9. **Adaptive Output:** Formats structure based on intent.
10. **Final Refinement:** Removes conversational fluff for maximum signal density.

> **Why use this?** Rather than generating an immediate (often flawed) answer, the model is forced into a highly structured "thinking" loop inside `<thinking>` and `<adversarial_review>` XML tags, surfacing grounded, reliable intelligence.

## 🧰 Included Skills

These skills serve as modular instructions that give the model specific operational parameters when working with advanced file formats or APIs.

- 🤖 **Claude API (`claude-api`)**: Rules for Anthropic SDKs and Prompt Caching.
- 📝 **Doc Co-authoring (`doc-coauthoring`)**: Workflow for transferring context to technical specs.
- 📄 **Word Documents (`docx`)**: Read, parse, and generate `.docx` files.
- 🛠 **MCP Builder (`mcp-builder`)**: Patterns for Model Context Protocol integrations.
- 📑 **PDF Mastery (`pdf`)**: OCR, merging, parsing, and structured extraction.
- 📊 **Presentations (`pptx`)**: Generate, parse, and modify `.pptx` decks.
- ⚙️ **Skill Creator (`skill-creator`)**: Instructions for benchmarking and authoring new skills.
- 📈 **Spreadsheets (`xlsx`)**: Clean, format, and compute `.xlsx` files.

---

## 📚 Documentation Quick Links

Ready to get started? Check out our detailed documentation:

- 🚀 [Usage & Integration Guide](USAGE_AND_INTEGRATION.md) — How to wire this up in Cursor, VSCode, ChatGPT (GPTs), Gemini (Gems), and other LLMs.
- 🧪 [Testing, Scenarios & Results](TESTING_AND_RESULTS.md) — 10 rigorous real-world evaluation scenarios showcasing adversarial flaw catching.
- 🏆 [Credits & Attributions](CREDITS.md) — Acknowledgments to the creators of these tools.

---

<div align="center">
  <p>If you find this repository useful, consider leaving a ⭐!</p>
</div>
