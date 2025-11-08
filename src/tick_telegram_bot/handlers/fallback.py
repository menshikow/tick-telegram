from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram_bot.handlers.help import HELP_TEXT
from tick_telegram_bot.handlers.buttons.menu_keyboard import build_main_menu


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I didn’t recognize that command.\n\n",
        parse_mode="Markdown",
        reply_markup=build_main_menu(),
    )
