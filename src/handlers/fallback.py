from telegram import Update
from telegram.ext import ContextTypes
from src.handlers.help import HELP_TEXT


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I didn’t recognize that command.\n\n" + HELP_TEXT, parse_mode="Markdown"
    )
