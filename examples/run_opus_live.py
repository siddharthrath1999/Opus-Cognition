"""
Opus-Cognition: 10-Second Live Demo
-----------------------------------
Run this script to instantly see the Opus Reasoning Engine in action.
Requires the 'anthropic' pip package and an Anthropic API Key.

Usage:
  export ANTHROPIC_API_KEY="your-key"
  python run_opus_live.py
"""

import os
try:
    import anthropic
except ImportError:
    print("❌ Error: Please run `pip install anthropic` first.")
    exit(1)

def run_demo():
    print("🧠 Initializing Opus-Cognition Engine...")
    
    # 1. Load the core rulebook natively
    with open("../system_instructions/opus46_cognitive_engine.md", "r") as f:
        system_prompt = f.read()

    client = anthropic.Anthropic()

    # 2. A deceptively simple prompt that standard models fail
    user_prompt = "Write a python function to transfer $50 from User A's bank balance to User B's balance."

    print(f"\\n👤 User Probe: {user_prompt}")
    print("🤖 Processing (Watch the slow thinking occur...)\\n")
    print("-" * 50)

    # 3. Stream the reasoning loop directly to the terminal
    with client.messages.stream(
        max_tokens=4000, 
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
        model="claude-3-7-sonnet-20250219",
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            
    print("\\n\\n" + "-" * 50)
    print("✅ Completed! Notice how it generated <thinking> tags to catch potential database race conditions before it gave you the final code.")

if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ Error: Missing ANTHROPIC_API_KEY environment variable.")
        exit(1)
        
    run_demo()
