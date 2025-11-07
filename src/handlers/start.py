from telegram import Update
from telegram.ext import ContextTypes
from src.handlers.buttons.menu_keyboard import build_main_menu


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Welcome to *tick!* Your personal to-do bot.\n\n"
        "Use the buttons below to get started:",
        parse_mode="Markdown",
        reply_markup=build_main_menu(),
    )
