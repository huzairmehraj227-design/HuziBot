from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
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

    return InlineKeyboardMarkup(keyboard)