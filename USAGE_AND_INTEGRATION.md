# 🚀 Usage & Integration Guide

The **Opus Cognition Framework** is highly portable. Because it operates as a master "System Prompt", it doesn't require complex package installations (unless you are evaluating it). 

This guide provides deep, intuitive paths for integrating the engine depending on your role.

---

## 🗺️ Which Integration Path is Right for You?

| Environment | Best For | Integration Method | Capability |
|-------------|----------|--------------------|------------|
| **ChatGPT / Gemini UI** | Non-developers, quick consulting | UI Copy/Paste | High |
| **Claude.ai Projects** | Deep architectural planning, skill usage | Knowledge Base Upload | Extremely High |
| **Cursor / VS Code** | Active Software Engineers | `.cursorrules` / `.copilot` | Extremely High |
| **Headless APIs** | Apps, Agents, Automation | REST Payload `system` Param | Total Control |

---

## 1. 🤖 Consumer AI Platforms (Web UIs)

If you use consumer models directly in the browser, you want to override their default behavior so they think before they speak.

### Method A: ChatGPT (Custom GPT)
*Best for: Persistent Chat environments and mobile use.*

When building the GPT, switch from the "Create" tab to the **Configure** tab and copy-paste these exact values:

- **Name:** `Opus Cognitive Engineer`
- **Description:** `A highly rigorous, multi-stage reasoning agent that forces slow-thinking, verification, and adversarial critique before answering.`
- **Instructions:** Paste the complete text of [`system_instructions/opus46_cognitive_engine.md`](system_instructions/opus46_cognitive_engine.md) directly into this box.
- **Conversation Starters:**
  - *"Review this code block and find the hidden race conditions."*
  - *"Help me architect a scalable backend system using first-principles."*
  - *"Adversarially critique my attached document."*
- **Knowledge:** Upload the specialized `.md` files you need directly from the [`skills/`](skills/) directory (e.g., upload `skills/pdf/SKILL.md` if you want it to be a PDF master).
- **Capabilities:** Check `Code Interpreter & Data Analysis` (crucial for executing tests) and `Web Browsing`.

Click **Save & Publish**. Your GPT will now inherently wrap all advanced problem-solving inside `<thinking>` tags.

### Method B: Claude (Projects)
*Best for: Complex codebase analysis. Claude natively handles the XML framing perfectly.*
1. Create a new **Project** in the left sidebar.
2. Under **Project Instructions**, paste the Opus framework framework code.
3. Click **"Add Content"** and upload the actual `opus46_cognitive_engine.md` file as project knowledge.
4. *Intuitive Tip:* Claude separates system prompts tightly. The XML tags native to Claude models (`<thinking>`) map flawlessly to this framework.

### Method C: Gemini Advanced (Gems)
*Best for: Extremely fast reasoning execution over large context windows.*

1. Navigate to **Gem manager** -> **Create a new Gem**.
2. Fill out the exact builder parameters:
   - **Name:** `Opus Cognition Engine`
   - **Instructions:** Paste the entire [`opus46_cognitive_engine.md`](system_instructions/opus46_cognitive_engine.md) text here.
   - **Knowledge/Files:** Because Gems natively hook into your Google Drive, you can keep your skills updated dynamically. Upload the specific `/skills/` rules you want this Gem to possess (e.g., `xlsx_skill.md`).
3. Click **Create**.
4. *Intuitive Tip:* Gemini is exceptionally fast, so the 10-stage loop overhead is extremely negligible, resulting in near-instant structurally verified responses.

---

## 2. 💻 Agentic IDEs (For Developers)

Injecting the framework into Agent IDEs prevents them from hastily generating buggy code that breaks your app.

### ⚡ Cursor (The `.cursorrules` method)
Cursor natively looks for a `.cursorrules` file to dictate how its AI behaves.
1. Create `.cursorrules` in your project root layer.
2. Copy the Opus 4.6 file and paste it completely inside.
3. **Adding Skills dynamically:** If you are building an MCP server today but writing technical specs tomorrow, you can simply append the relevant skill right below the engine:
```markdown
[Paste Opus 4.6 Engine text here]
---
# ACTIVE SKILL: MCP Builder
[Paste contents of skills/mcp-builder/SKILL.md here]
```

### ⚡ VS Code / GitHub Copilot
1. Create a `.github/copilot-instructions.md` file in your repository.
2. Paste the Opus instructions. Copilot Chat will utilize these constraints when generating inline suggestions or answering terminal queries.

### ⚡ Claude Code (Terminal CLI)
1. Claude Code looks for `.claude-code.txt`. 
2. Or, pass the framework file in your prompt context dynamically:  
   `claude "Analyze this memory leak using the framework strictly defined in Opus-Cognition/system_instructions/opus46_cognitive_engine.md"`

---

## 3. 🔌 Headless APIs (Python / Node.js)

If you are a developer building a backend LLM loop, pass the Opus framework statically located in your codebase into the `system` parameter of your messages payload.

> [!WARNING]
> Do **NOT** place the framework in the `user` prompt. It must be placed in the `system` role parameter to establish highest adherence priority.

### Advanced: The Global CLI (Beta Prompt Caching)
Because Opus is massive, sending it into an API on every call burns input tokens. If you want to use Opus-Cognition on-the-fly securely, utilize the included pip package. This architecture natively injects `<ephemeral>` caching markers, saving you **~90%** on Anthropic usage costs automatically!
```bash
# From the repository root
cd packages/opus-cli
pip install -e .
export ANTHROPIC_API_KEY="your-key"

# Execute natively from anywhere!
opus "Analyze this architecture for lost-updates"
```

### Advanced: The FastMCP Server (Claude Desktop)
If you prefer Claude Desktop, you don't even need to paste the `.md` file. Boot the natively installed Model Context Protocol server:
```bash
cd packages/opus-mcp
python mcp_server.py
```
*This exposes the Opus Cognitive Tool universally to your Claude desktop instances.*

### Generic Python (Standard API Call)

```python
import os
import anthropic

# 1. Load the cognitive framework into memory
with open("Opus-Cognition/system_instructions/opus46_cognitive_engine.md", "r") as file:
    OPUS_SYSTEM_PROMPT = file.read()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# 2. Execute with the framework as the System param
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=4000, # Give it room to think!
    system=OPUS_SYSTEM_PROMPT, 
    messages=[
        {"role": "user", "content": "Analyze our server performance."}
    ]
)

print(message.content)
```

> [!TIP]
> **Stuck or seeing weird loops?** Head straight to the [🚑 Support & Troubleshooting Guide](SUPPORT_AND_TROUBLESHOOTING.md) for fallbacks and solutions!
