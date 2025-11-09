from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram.handlers.buttons.menu_keyboard import build_main_menu
from tick_telegram.localization import get_user_language, t


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_user_language(update)
    await update.message.reply_text(
        t("start.welcome", lang=lang),
        parse_mode="Markdown",
        reply_markup=build_main_menu(lang),
    )
