import os
import requests

# Replace with DeepSeek endpoint if different
API_URL = "https://api.deepseek.com/v1/chat/completions"  # hypothetical endpoint
API_KEY = os.getenv("sk-9d2be95ee8344455a33c1eeba9f15027")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek-coder",  # or the correct model name you’re using
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the best way to start a GitHub Actions workflow for a Python project?"}
    ],
    "temperature": 0.7
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print("🤖 DeepSeek Response:\n", answer)
else:
    print("❌ Error:", response.status_code, response.text)
