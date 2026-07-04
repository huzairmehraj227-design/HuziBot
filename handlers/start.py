from telegram import Update
from telegram.ext import ContextTypes

from keyboards.menu import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to *HuziBot!*\n\nChoose an option:",
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )