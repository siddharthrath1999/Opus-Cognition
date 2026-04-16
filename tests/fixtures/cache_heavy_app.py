import anthropic

# Expected AI behavior: AI should detect caching limits are broken.
# Anthropic only supports 4 ephemeral cache breakpoints! This script attempts 5.
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    system=[
        {"type": "text", "text": "Rules 1...", "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": "Rules 2...", "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": "Rules 3...", "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": "Rules 4...", "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": "Rules 5...", "cache_control": {"type": "ephemeral"}}
    ],
    messages=[{"role": "user", "content": "Help me code."}]
)
