"""
Generate Agent-SafetyBench framework flowchart using nano-banana-2 (Gemini 3.1 Flash Image Preview)
"""

import os
from inferencesh import inference

# Get API key from environment variable
api_key = os.environ.get('INFERENCE_API_KEY')
if not api_key:
    raise ValueError(
        "Please set INFERENCE_API_KEY environment variable first.\n"
        "You can get your API key from https://inference.sh after logging in."
    )

client = inference(api_key=api_key)

# Detailed prompt for flowchart generation
prompt = """
Professional technical flowchart diagram of the Agent-SafetyBench framework for LLM agent safety evaluation.

Structure the flowchart with these sections:

1. TOP - FRAMEWORK OVERVIEW (摘要):
- Agent-SafetyBench: LLM Agent 安全测评基准框架
- 349 interactive environments (Email, Web, Slack, Bank etc)
- 2000 test cases covering 8 risk categories & 10 failure modes
- Automated scorer: fine-tuned Qwen2.5-7B-Instruct, 91.5% accuracy

2. MIDDLE - DATA FLOW (数据流转):
Start → Test Case Input (environment parameters + user prompt) → LLM Agent → Tool calls to Environment → Environment feedback → Agent → Final Response → Interaction Log → Scoring Model → Safety Evaluation Result

3. LOWER LEFT - EVALUATION RESULTS (测评结果数据):
- 16 tested mainstream LLMs (Claude 3.5, GPT-4o, Gemini 1.5, Llama 3.1, Qwen 2.5, GLM-4 etc)
- Score range: 18.8% ~ 59.4% (Claude-3.5-Sonnet highest)
- Key findings: Lowest in misinformation propagation (15.6%), lowest failure mode M2 (18.1%)

4. LOWER RIGHT - CONCLUSIONS & NEXT STEPS (结论与后续动作):
- Conclusions: Two main safety issues → insufficient robustness (tool parameter errors), lack of risk awareness (ignores hidden risks)
- Future work: Develop safety-oriented fine-tuning, build domain-specific test cases (medical/finance)
- Action plan: Short-term (Q4) complete compliance check, deploy compliance tools; Long-term adopt Hainan free trade port tax structure (15% corporate income tax), establish regular risk audit mechanism

Style requirements:
- Clean professional flowchart, clear box arrows and labels
- Business technology diagram style, readable text, clear connections
- Blue-based color scheme, professional corporate report style
- Landscape orientation (16:9 aspect ratio)
- All text must be in Chinese
- Use standard flowchart symbols: rectangles for processes, ovals for start/end, diamonds for decisions if needed
- Clear hierarchy: top overview → center data flow → bottom results/conclusion

Please generate a clear, professional technical flowchart that is easy to understand at a glance.
"""

# Run the generation
result = client.run({
    "app": "google/gemini-3-1-flash-image-preview@0c7ma1ex",
    "input": {
        "prompt": prompt,
        "num_images": 1,
        "aspect_ratio": "16:9",
        "resolution": "2K"
    }
})

print("Generation completed!")
print("Result:", result)

# Save the result
if "output" in result and "images" in result["output"]:
    print(f"\nGenerated {len(result['output']['images'])} image(s)")
    for i, img in enumerate(result["output"]["images"]):
        ext = img.split(".")[-1]
        filename = f"agent_safetybench_flowchart_{i}.{ext}"
        print(f"Saved to {filename}")
else:
    print("\nNo images in output")
    print("Full output:", result)
