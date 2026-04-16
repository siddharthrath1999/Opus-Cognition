# Opus-Cognition CLI
This is the global terminal execution wrapper for the Opus-Cognition agentic framework.

## Installation
```bash
pip install opus-cognition-cli
```

## Usage
It natively wraps Anthropic's Beta Prompt Caching around the massive 10-stage `opus46_cognitive_engine.md` framework, allowing you to use the engine locally without burning thousands of input tokens on every pass.

```bash
export ANTHROPIC_API_KEY="your-key-here"
opus "Find a memory leak in my script"
```
