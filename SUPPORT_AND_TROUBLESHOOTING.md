# 🚑 Support, Troubleshooting & Fallbacks

Working with advanced system prompts that force multi-stage reasoning can sometimes lead to unexpected behavior from models. If an LLM misbehaves inside the Opus-Cognition framework, use this guide to identify the state, implement a fallback, and fix the loop.

---

## 1. 🛑 Common Issues & Solutions

### Issue: The AI cuts off halfway through the `<thinking>` tag.
**Diagnosis:** You ran out of `max_tokens`. The Opus Engine generates a significant amount of text *before* it gets to the final answer because it is verifying logic inside the XML tags.
- **Solution (API):** Increase your `max_tokens` argument. For this engine, `max_tokens=4000` or `8000` is highly recommended.
- **Solution (Web UI):** Simply type `"continue"` and hit enter. The model will pick up exactly where it left off.

### Issue: The AI gets stuck in an infinite `Stage 6 (Adversarial Critique)` loop.
**Diagnosis:** The AI keeps finding minor flaws in its own logic and refusing to proceed, looping through Stages 4 -> 6 infinitely. 
- **Solution:** This usually means the problem is genuinely impossible given the constraints provided, or the `temperature` is too low, blocking creative circumvention. 
- **Alternative Action:** Prompt the AI explicitly: *"Bypass the adversarial loop for this specific edge case and proceed to Stage 7 Calibration."*

### Issue: The AI ignores the rules and answers immediately.
**Diagnosis:** The LLM you are using has poor "System Adherence" (it ignores system prompts in favor of user prompts).
- **Fallback:** Move the contents of `opus46_cognitive_engine.md` completely out of the System config window, and paste it into the start of your actual User Prompt, formatting it like: `INSTRUCTIONS: [text] \n\n MY QUERY: [query]`.

---

## 2. 🔀 Fallbacks & Alternatives 

If the Opus 4.6 Heavy Engine is simply too expensive or slow for your specific use-case (e.g., highly repetitive micro-tasks), use these built-in alternative strategies:

### Fallback A: The "Lightweight" Run
If you need high-speed answers but want minor verification, tell the AI to skip stages.
**Working Example Prompt:**
> "Execute the task using the Opus Engine, but strictly bypass Stages 2, 4, and 5. Jump straight from Problem Framing to Stage 6 Critique."

### Fallback B: The "Silent" Mode
Sometimes you don't want to see 500 tokens of XML thinking in your UI, you just want the verified answer.
**Working Example Prompt:**
> "Follow the Opus 10-stage pipeline internally, but do not print the `<thinking>` or `<adversarial_review>` XML tags to the final output stream. Keep them hidden and only print the Final Stage 10 output."
*(Note: Some models struggle with this limitation, as writing down the thoughts is mathematically how they "think").*

---

## 3. 🛠 Skill Troubleshooting

Skills (found in `/skills/`) are powerful extensions, but they can misfire if not handled properly.

- **Claude-API Skill Not Caching:** Ensure you are using the exact `ephemeral` block specified in the skill doc. If the model hallucinations outside of `ephemeral` blocks, strictly remind the model: *"Check the claude-api skill. You forgot to cache the system content."*
- **MCP Builder Frying Protocols:** Model Context Protocol demands strict standard output. If the agent builds an MCP that crashes, it used a generic `print` state. Read the [`tests/fixtures/mcp_stdio_broken.py`](tests/fixtures/mcp_stdio_broken.py) trap to understand how the test suite prevents this.

---

## 🔗 Deep Links
If you need to understand core parameters or file bugs:
- [Opus 4.6 Architecture Rules](../system_instructions/opus46_cognitive_engine.md)
- [Review the Test Configurations](../tests/configs/eval_params.yaml)
