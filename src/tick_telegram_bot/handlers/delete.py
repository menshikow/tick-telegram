from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram_bot.localization import get_user_language, t
from tick_telegram_bot.storage import todos


async def delete_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_user_language(update)
    try:
        user_id = update.effective_user.id
    except AttributeError:
        await update.message.reply_text(t("errors.user_unknown", lang=lang))
        return

    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text(t("delete.usage", lang=lang))
        return

    index = int(context.args[0]) - 1  # Convert to zero-based index
    try:
        todos.delete_task(user_id, index)
        await update.message.reply_text(t("delete.success", lang=lang, index=index + 1))
    except IndexError:
        await update.message.reply_text(t("errors.task_not_found", lang=lang))
