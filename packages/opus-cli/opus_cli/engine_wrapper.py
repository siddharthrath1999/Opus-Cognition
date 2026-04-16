import anthropic
import os

def call_opus_with_caching(user_prompt: str, system_prompt_path: str):
    """
    Hits the Anthropic API utilizing the cost-saving Ephemeral Cache control.
    Because the Opus-Cognition framework is massive natively, executing it
    normally burns thousands of input tokens. This wrapper inherently cuts
    infrastructure costs locally by 90% by forcing Anthropic cache tracking.
    """
    client = anthropic.Anthropic()
    
    with open(system_prompt_path, "r", encoding='utf-8') as f:
        system_rules = f.read()

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        system=[
            {
                "type": "text",
                "text": system_rules,
                "cache_control": {"type": "ephemeral"}  # Native Beta caching trigger
            }
        ],
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.content[0].text
