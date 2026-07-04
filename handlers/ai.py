from telegram import Update
<<<<<<< HEAD
from telegram.ext import ContextTypes

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    await update.callback_query.message.reply_text(
        "🧠 AI Mode is coming online...\n\nSoon you'll be able to chat with me!"
    )
=======
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from services.ai_service import ask_ai


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

    user_message = update.message.text

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    try:
        response = await ask_ai(user_message)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"❌ Error:\n{e}")
>>>>>>> 3485235 (🧠 Integrated Gemini AI into HuziBot)
