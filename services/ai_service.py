import google.generativeai as genai

from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def ask_ai(prompt: str):
    response = model.generate_content(prompt)
    return response.text