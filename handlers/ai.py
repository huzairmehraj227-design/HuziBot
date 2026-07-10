import json

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from services.ai_service import ask_ai, extract_profile
from database.sqlite_db import (
    load_memory,
    save_memory,
    load_profile,
    save_profile,
)


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    context.user_data["ai_mode"] = True

    await query.message.reply_text(
        "🧠 AI Mode Enabled!\n\nNow send me any message."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("ai_mode"):
        return

    user_id = update.effective_user.id
    user_message = update.message.text

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    history = load_memory(user_id)
    profile = load_profile(user_id)

    prompt = f"""
User Profile:
{profile}

Conversation History:
{history}

User:
{user_message}
"""

    try:
        response = await ask_ai(prompt)

        history += (
            f"\nUser: {user_message}"
            f"\nHuziBot: {response}"
        )

        save_memory(user_id, history)

        try:
            extracted = await extract_profile(user_message, profile)

            new_profile = json.loads(extracted)

            profile.update(new_profile)

            save_profile(user_id, profile)

        except Exception:
            pass

        await update.message.reply_text(response)

    except Exception:
        await update.message.reply_text(
            "⚠️ I'm a little overloaded right now. Give me a few seconds and try again."
        )