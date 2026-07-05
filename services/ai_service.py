import google.generativeai as genai

from config.config import GEMINI_API_KEY
from config.personality import SYSTEM_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def ask_ai(prompt: str):
    full_prompt = f"""
{SYSTEM_PROMPT}

User: {prompt}

HuziBot:
"""

    response = model.generate_content(full_prompt)
    return response.text