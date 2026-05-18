from openai import OpenAI
from prompts.system_prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def generate_response(user_input, chat_history):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Previous conversation
    for chat in chat_history:

        messages.append({
            "role": "user",
            "content": chat["user"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["assistant"]
        })

    # Current question
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate AI response
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content