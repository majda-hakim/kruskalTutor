import aiohttp
import asyncio
import json

async def invoke_chute(prompt):
    api_token = "cpk_ac4e9f899c894656b103dbec3e264045.16a9a0c8251b52cbbba99505e6bc716f.FKON2zTNlo1L0BzgVoY9dKJSFFgLd4wg"
    headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
    body = {
        "model": "deepseek-ai/DeepSeek-V3-0324",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,  # Disable streaming for simplicity
        "max_tokens": 1024,
        "temperature": 0.7
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://llm.chutes.ai/v1/chat/completions",
            headers=headers,
            json=body
        ) as response:
            if response.status != 200:
                error = await response.text()
                return {"error": f"API request failed: {error}"}
            data = await response.json()
            return data["choices"][0]["message"]["content"]
        
# Run the function and print the response
async def main():
    prompt = "Explain Dijkstra's algorithm in simple terms."
    print(f"Prompt: {prompt}\nResponse:")
    response = await invoke_chute(prompt)
    print("\n\nFull Response:", response)  # Optional: Print the full response at the end

# Execute the async function
asyncio.run(main())
