from telegram import Update
from telegram.ext import ContextTypes

from tick_telegram_bot.localization import get_user_language, t


def get_help_text(lang: str) -> str:
    return t("help.text", lang=lang)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_user_language(update)
    await update.message.reply_text(get_help_text(lang), parse_mode="Markdown")
