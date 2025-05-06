import requests

headers = {
    "Authorization": "sk-9d2be95ee8344455a33c1eeba9f15027",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}

response = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers=headers,
    json=data
)

print(response.json())
