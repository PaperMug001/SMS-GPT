from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_KEY")
)

def ask_ai(prompt, system="You are a helpful AI assistant. This will be forwarded to SMS, so pls keep in mind the restriction of length of a SMS as much possible, otherwise We will manually split/chunk your message if needed."):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content