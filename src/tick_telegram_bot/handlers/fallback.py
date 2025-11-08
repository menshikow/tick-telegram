from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram_bot.handlers.buttons.menu_keyboard import build_main_menu
from tick_telegram_bot.localization import get_user_language, t


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_user_language(update)
    await update.message.reply_text(
        t("fallback.unknown_command", lang=lang),
        parse_mode="Markdown",
        reply_markup=build_main_menu(lang),
    )
