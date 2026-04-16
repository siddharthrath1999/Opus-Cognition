import sys
import json

def process_mcp_message(message_str):
    # This print statement breaks the MCP JSON-RPC protocol because STDIO 
    # transport requires purely JSON over stdout. 
    # Expected: AI uses mcp-builder skill constraints to catch this and convert it to sys.stderr
    print(f"DEBUG: Processing inbound MCP message length: {len(message_str)}")
    
    try:
        msg = json.loads(message_str)
        # Handle the JSON RPC payload
        response = {"jsonrpc": "2.0", "id": msg.get("id"), "result": "success"}
        print(json.dumps(response)) # Valid protocol output
    except Exception as e:
        sys.stderr.write(f"Error: {e}\\n")

if __name__ == "__main__":
    for line in sys.stdin:
        process_mcp_message(line)
