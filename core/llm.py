import requests


# OLLAMA_URL = "http://localhost:11434/api/generate"
#
#
# def call_ollama(prompt: str, model: str = "llama3"):
#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": model,
#             "prompt": prompt,
#             "stream": False
#         }
#     )
#
#     return response.json()["response"]

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def call_ollama(prompt: str, model: str = "openai/gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "restaurant-agent"
            }
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("LLM Error:", e)
        return '{"intent": "unknown"}'