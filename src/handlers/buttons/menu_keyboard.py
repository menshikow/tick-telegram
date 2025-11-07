from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def build_main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📝 Add Task", callback_data="menu:add"),
            InlineKeyboardButton("📋 List Tasks", callback_data="menu:list"),
        ],
        [
            InlineKeyboardButton("🧹 Clear All", callback_data="menu:clear"),
            InlineKeyboardButton("❓ Help", callback_data="menu:help"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
