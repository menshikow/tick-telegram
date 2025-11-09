from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram.localization import get_user_language, t
from tick_telegram.storage import todos


async def clear_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_user_language(update)
    try:
        user_id = update.effective_user.id
    except AttributeError:
        await update.message.reply_text(t("errors.user_unknown", lang=lang))
        return

    todos.clear_all(user_id)
    await update.message.reply_text(t("clear.cleared", lang=lang))
