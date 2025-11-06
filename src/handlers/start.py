from telegram import Update
from telegram.ext import ContextTypes
from src.handlers.help import HELP_TEXT


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "welcome to tick 👋\n\n" + HELP_TEXT, parse_mode="Markdown"
    )
