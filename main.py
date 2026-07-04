import os
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💬 AI", callback_data="ai"),
            InlineKeyboardButton("🛠️ Tools", callback_data="tools"),
        ],
        [
            InlineKeyboardButton("🌐 Search", callback_data="search"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
        ],
    ]

    await update.message.reply_text(
        "👋 Welcome to *HuziBot*!\n\nChoose an option:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "ai": "🤖 AI module coming soon...",
        "tools": "🛠️ Tools coming soon...",
        "search": "🌐 Search coming soon...",
        "settings": "⚙️ Settings coming soon...",
    }

    await query.edit_message_text(responses.get(query.data, "Unknown option."))


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🚀 HuziBot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()