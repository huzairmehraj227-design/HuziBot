from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from services.ai_service import ask_ai
from database.sqlite_db import get_memory, save_memory


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

    history = get_memory(user_id)

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    try:
        response = await ask_ai(
            f"""
Previous conversation:
{history}

User:
{user_message}
"""
        )

        history += (
            f"\nUser: {user_message}"
            f"\nHuziBot: {response}"
        )

        save_memory(user_id, history)

        await update.message.reply_text(response)

    except Exception:
        await update.message.reply_text(
            "⚠️ I'm a little overloaded right now. Give me a few seconds and try again."
        )