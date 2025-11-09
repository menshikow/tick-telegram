from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram.localization import get_user_language, t
from tick_telegram.storage import todos


async def add_description_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    lang = get_user_language(update)
    if len(context.args) < 2:
        await update.message.reply_text(t("adddesc.usage", lang=lang))
        return

    try:
        index = int(context.args[0]) - 1
    except ValueError:
        await update.message.reply_text(t("adddesc.index_not_number", lang=lang))
        return

    description = " ".join(context.args[1:])
    user_id = update.effective_user.id

    try:
        todos.add_description(user_id, index, description)
        await update.message.reply_text(
            t("adddesc.success", lang=lang, description=description, index=index + 1)
        )
    except (IndexError, ValueError):
        await update.message.reply_text(t("adddesc.invalid_index", lang=lang))
