# 🚀 Usage & Integration Guide

The **Opus Cognition Framework** is designed to be highly portable. Below are step-by-step instructions for integrating the reasoning engine and specialized skills across consumer AI platforms and professional developer environments.

---

## 🤖 1. General AI Platforms (Web / Consumer)

For general daily usage, inject `system_instructions/opus46_cognitive_engine.md` into the custom instructions menu of your preferred AI platform. 

### ChatGPT (Custom GPT)
1. Go to **Explore GPTs** -> **Create**.
2. Click the **Configure** tab.
3. **Name:** Opus Engine
4. **Instructions:** Paste the entirety of `opus46_cognitive_engine.md`.
5. **Knowledge:** Upload any relevant skills from the `skills/` directory (e.g., `xlsx_skill.md` or `pdf_skill.md`) into the **Knowledge** file upload section.
6. Make sure "Code Interpreter" is enabled for spreadsheet/file manipulation.

### Gemini (Gems)
1. Navigate to **Gemini Advanced** -> **Gem manager** -> **Create a new Gem**.
2. **Name:** Opus Core
3. **Instructions:** Paste the `opus46_cognitive_engine.md` text.
4. **System behavior:** The Gem will inherently follow the `<thinking>` and `<adversarial_review>` XML tags before printing final markdown.

### Claude (Projects / Skills)
1. Create a new **Project** in the left sidebar.
2. Under **Project Instructions**, paste the Opus framework.
3. Click "Add Content" and upload the Markdown `.md` files from the `skills/` directory. Claude's high recall window makes this the most effective way to load the entire skill suite simultaneously.

---

## 💻 2. IDEs & Agentic Helpers

Injecting the framework into Agent IDEs prevents them from hastily generating buggy code.

### Cursor
1. Create a `.cursorrules` file in the root of your workspace workspace.
2. Paste the `opus46_cognitive_engine.md` directly into `.cursorrules`.
3. When using the Composer or Chat, Cursor will now write out its reasoning paths and self-correct prior to modifying files.
4. *Loading Skills:* If building an MCP, simply append the `skills/mcp-builder/SKILL.md` rules below the Opus framework inside `.cursorrules`.

### VS Code / Visual Studio
If you use standard VS Code with AI extensions (like Github Copilot Chat):
1. Copilot allows setting workspace instructions via `.github/copilot-instructions.md`.
2. Save the Opus layout and relevant skills into that markdown file.
3. The Copilot Chat agent will utilize these constraints when generating inline suggestions or answering terminal queries.

### GitHub Copilot (Workspace Level)
1. For Copilot Workspace (the PR generation tool), inclusion of `system_instructions` in a top-level `.copilot` or configuration block allows the PR builder to utilize multi-pass reasoning before submitting code across files.

### Claude Code (CLI)
1. Claude Code looks for `.claude-code.txt` or general instructions. 
2. Pass the framework file in your prompt context via file inclusion:  
   `claude "Analyze this issue using the framework strictly defined in Opus-Cognition/system_instructions/opus46_cognitive_engine.md"`

### Google Antigravity
If utilizing the advanced Antigravity workspace, the skills and Opus system can be seamlessly mapped into your local `<appDataDir>/knowledge` directory.
1. Place the engine as a Knowledge Item (`KI`). 
2. Antigravity will check KIs and pull the Opus 10-stage logic loop automatically for high-complexity analysis queries.
