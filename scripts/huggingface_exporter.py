import os
import json
import yaml

def export_huggingface_dataset():
    """
    Compiles local test suites into a HuggingFace fine-tuning/eval dataset format (.jsonl).
    Running this exposes the rigorous Opus-Cognition testing logic to global AI researchers.
    """
    output_path = "huggingface_benchmark.jsonl"
    config_path = "tests/configs/eval_params.yaml"
    
    if not os.path.exists(config_path):
        print("❌ Cannot find evaluation configs.")
        return

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    dataset = []
    for test in config['tests']:
        try:
            fixture_target = f"tests/fixtures/{test['fixture']}"
            if os.path.exists(fixture_target):
                with open(fixture_target, "r") as f:
                    content = f.read()
                    
                    dataset.append({
                        "system_instruction_source": "Opus-Cognition Framework",
                        "instruction": f"Execute this prompt mimicking the 10-stage Opus pipeline: {test['name']}",
                        "input_context": content,
                        "success_criteria_regex": test['metrics'][0]['pattern'],
                        "difficulty": test.get('difficulty', 'Unknown')
                    })
        except Exception as e:
            print(f"Skipping {test['name']}: {e}")
            
    with open(output_path, "w") as f:
        for entry in dataset:
            f.write(json.dumps(entry) + "\\n")
            
    print(f"✅ HuggingFace Dataset successfully compiled to {output_path}")

if __name__ == "__main__":
    export_huggingface_dataset()
