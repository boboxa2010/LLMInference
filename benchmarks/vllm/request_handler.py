import time
import requests

from typing import Any

def send_request(prompt: str,
                api_url: str,
                temperature: float = 0.7,
                max_tokens: int = 100,
                model_name: str = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
                ) -> dict[str, Any]:

    headers = {"Content-Type": "application/json"}
    payload = {
        "model" : model_name,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    start_time = time.time()
    response = requests.post(api_url, headers=headers, json=payload)
    end_time = time.time()
    
    if response.status_code == 200:
        return {
            "success": True,
            "latency": end_time - start_time,
            "response": response.json(),
            "input_tokens": response.json().get("usage", {}).get("prompt_tokens", 0),
            "output_tokens": response.json().get("usage", {}).get("completion_tokens", 0)
        }
    else:
        return {
            "success": False,
            "latency": end_time - start_time,
            "status_code": response.status_code,
            "error": response.text
        }
