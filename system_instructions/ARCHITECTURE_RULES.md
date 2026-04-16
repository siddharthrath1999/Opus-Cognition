# 🏛️ Opus 4.6 Architecture Rules (Master Guide)

This document is the **Master Architecture Guide** for the Opus Cognition framework. While `opus46_cognitive_engine.md` acts as the literal machine-readable instruction set that you feed to an AI, this page breaks down the theory, logic, and structural rules of *why* those instructions are written the way they are.

---

## The Rule of Constraint

The core rule of Opus-Cognition is **Constraint before Generation**. Large Language Models natively generate tokens linearly. Once they write a bad token, they are mathematically forced to justify that bad token in the next sentence. 

To break this cycle, the Architecture enforces a non-linear staging ground (`<thinking>`) where the LLM is allowed to generate, discard, and revise tokens invisibly before it is allowed to write a single public "Final Output" token.

---

## The 10 Architectural Stages (Deep Dive)

### Stage 1: Problem Formalization
**The Rule:** *Never trust the user's premise directly.*
The first architectural rule is that the AI must break down the prompt into objective functions. If you prompt, "Why is my database slow when I run this query?", the standard model assumes the query is the problem. Stage 1 forces the model to ask internally: *"Is the database actually slow, or is the network connection hanging?"*

### Stage 2 & 3: Exploration and Verification (The Split Path)
**The Rule:** *Never formulate a single answer.*
The architecture demands at least 2 distinct, conflicting paths of reasoning. 
- *Path A:* The obvious, lazy solution.
- *Path B:* First-principles engineering.
The Verification layer (Stage 3) acts as a mathematical filter. It cross-checks Path A and Path B against known physics, SDK constraints, or logical consistency. It deletes paths that are ungrounded.

### Stage 4 & 5: Iterative Deepening & Synthesis
**The Rule:** *Stress-test the survivor.*
Once a path survives verification, the architecture forces the AI to iterate on it at scale. If writing code, it must imagine that code processing 10,000 requests. It simulates edge cases, then synthesizes a unified blueprint.

### Stage 6: Adversarial Self-Critique (The Red-Team)
**The Rule:** *Assume the synthesized answer is fundamentally flawed.*
This is the heart of the Opus framework. The AI must open an `<adversarial_review>` tag and ruthlessly attack its own blueprint from Stage 5. 
- *What happens if memory fills up?*
- *Did I hardcode a variable?*
- *Is this vulnerable to SQL injection?*
**Critical Loop:** If the AI finds a fatal flaw here, the architecture strictly forbids it from moving to Stage 7. It *must* return to Stage 4 and rebuild the blueprint. 

### Stage 7: Uncertainty Calibration
**The Rule:** *Absolute refusal to guess.*
If the AI cannot resolve a conflict in Stage 6, it reaches Stage 7. Here, the architecture blocks generation. The AI is instructed to stop the `<thinking>` tag immediately and output a response like: *"I cannot answer this safely. I need to know your postgres version before I can guarantee this query won't deadlock your system."*

### Stage 8 & 9: Bias Checking & Adaptive Output
**The Rule:** *Form dictates function.*
The AI checks if it was influenced by the phrasing of the prompt (e.g. "Create a React component" -> *Does this actually need React?*). It then dynamically formats the output (using Mermaid diagrams for causality, markdown tables for comparisons, etc.).

### Stage 10: Final Refinement
**The Rule:** *Maximum Signal Density.*
The architecture bans conversational "fluff". The AI strips out *"Certainly! Here is your code..."* and outputs purely the vetted, necessary response.

---

## Modifying the Master Rules

If you are a prompt engineer or system architect looking to tune the `opus46_cognitive_engine.md` system prompt:

1. **Changing Depth Limits:** If the prompt loop feels too deep for your use case, find the `STAGE 4` block in the engine and change `Complex tasks: 3–5 cycles` to `Maximum cycles: 1` to force a faster synthesis.
2. **Loosening the Adversarial Trigger:** If your model gets stuck in an infinite loop (e.g., rejecting its own code repeatedly), you must relax the constraints in `STAGE 6`. Instruct the model to *accept "good enough" non-breaking code constraints*.
3. **Escalation Thresholds:** In `STAGE 7`, you can dictate exactly what constitutes an "ambiguous" risk. (e.g., "Only halt execution if financial data is at risk, otherwise proceed with a disclaimer.").
