from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from prompts.system_prompts import SYSTEM_PROMPT
import os

# Load environment variables
load_dotenv()

# Hugging Face Client
client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

def generate_response(user_input, chat_history):

    # System Prompt
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add previous chat history
    for chat in chat_history:

        messages.append({
            "role": "user",
            "content": chat["user"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["assistant"]
        })

    # Current user input
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    response = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=messages,
        max_tokens=300
    )

    return response.choices[0].message.content