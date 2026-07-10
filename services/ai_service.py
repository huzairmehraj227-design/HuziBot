import google.generativeai as genai

from config.config import GEMINI_API_KEY
from config.personality import PERSONALITY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def ask_ai(prompt: str):
    response = model.generate_content(
        PERSONALITY + "\n\n" + prompt
    )

    return response.text


async def extract_profile(user_message: str, profile: dict):
    prompt = f"""
You update a user's profile.

Current profile:
{profile}

User message:
{user_message}

Update the profile only if the user clearly provides personal information.

Possible fields:
- name
- age
- favorite_game
- favorite_movie
- favorite_color
- location

Return ONLY valid JSON.

Example:
{{
"name":"Huzair",
"favorite_game":"Minecraft"
}}

Do not explain anything.
"""

    response = model.generate_content(prompt)

    return response.text