from openai import OpenAI

client = OpenAI(
    api_key="sk-9d2be95ee8344455a33c1eeba9f15027",  # Replace with env variable in production
    base_url="https://api.deepseek.com/v1"  # Note the /v1 endpoint
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    temperature=0.7,  # Recommended to add parameters
    stream=False
)

print(response.choices[0].message.content)