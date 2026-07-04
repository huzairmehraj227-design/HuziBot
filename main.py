from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config.config import BOT_TOKEN
from handlers.start import start
from handlers.ai import ai, chat


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ai":
        await ai(update, context)
        return

    responses = {
        "tools": "🛠️ Tools coming soon...",
        "search": "🌐 Search coming soon...",
        "settings": "⚙️ Settings coming soon...",
    }

    await query.edit_message_text(
        responses.get(query.data, "Unknown option.")
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🚀 HuziBot is running...")

    app.run_polling(
        drop_pending_updates=True,
        close_loop=False,
    )


if __name__ == "__main__":
    main()