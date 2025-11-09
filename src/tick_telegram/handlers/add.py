from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram.localization import get_user_language, t
from tick_telegram.storage import todos


async def add_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    lang = get_user_language(update)
    if not context.args:
        await update.message.reply_text(t("add.missing_title", lang=lang))  # type: ignore
        return

    title = context.args[0]
    description = " ".join(context.args[1:]) if len(context.args) > 1 else ""
    user_id = update.effective_user.id  # type: ignore

    todos.add(user_id, title, description)
    message_key = (
        "add.success_no_desc" if description == "" else "add.success_with_desc"
    )
    await update.message.reply_text(  # type: ignore
        t(message_key, lang=lang, title=title, description=description)
    )
