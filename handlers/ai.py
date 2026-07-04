from telegram import Update
from telegram.ext import ContextTypes

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    await update.callback_query.message.reply_text(
        "🧠 AI Mode is coming online...\n\nSoon you'll be able to chat with me!"
    )