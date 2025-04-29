import requests

response = requests.post(
    "http://localhost:8000/v1/completions",
    json={
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        "prompt": "Explain deep learning in simple terms:",
        "max_tokens": 100,
        "temperature": 0.7
    }
)
print(response.json())
