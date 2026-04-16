import argparse
import sys
import os
from .engine_wrapper import call_opus_with_caching

def cli():
    parser = argparse.ArgumentParser(description="Opus-Cognition Terminal CLI")
    parser.add_argument("prompt", type=str, help="The engineering prompt to send to the cognitive engine")
    
    # UNIVERSAL ALIGNMENT: Dynamically resolve to the core repo instructions even if executed globally via pip.
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    default_path = os.path.join(base_dir, "system_instructions", "opus46_cognitive_engine.md")
    
    parser.add_argument("--sys-path", type=str, default=default_path, help="Path to engine override")
    
    args = parser.parse_args()
    print("🧠 Booting Opus Engine (Token Caching Enabled)...")
    try:
        output = call_opus_with_caching(args.prompt, args.sys_path)
        print("\\n--- Output ---\\n", output)
    except Exception as e:
        print(f"❌ Execution Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    cli()
