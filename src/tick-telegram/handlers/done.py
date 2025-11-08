from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram_bot.localization import get_user_language, t
from tick_telegram_bot.storage import todos


async def done_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_user_language(update)
    if not context.args:
        await update.message.reply_text(t("done.missing_index", lang=lang))
        return

    try:
        index = int(context.args[0]) - 1  # Convert to zero-based index
    except ValueError:
        await update.message.reply_text(
            t("errors.index_number_required", lang=lang)
        )
        return

    try:
        user_id = update.effective_user.id
    except AttributeError:
        await update.message.reply_text(t("errors.user_unknown", lang=lang))
        return

    try:
        todos.mark_done(user_id, index)
        await update.message.reply_text(t("done.success", lang=lang, index=index + 1))
    except IndexError:
        await update.message.reply_text(
            t("errors.task_not_found_retry", lang=lang)
        )
