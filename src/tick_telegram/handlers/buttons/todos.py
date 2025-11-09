from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram.localization import get_user_language, t
from tick_telegram.storage import todos


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # type: ignore
    user_id = query.from_user.id  # type: ignore
    action, index_str = query.data.split(":")  # type: ignore
    index = int(index_str)
    lang = get_user_language(update)

    if action == "done":
        try:
            todos.mark_done(user_id, index)
            await query.edit_message_text(  # type: ignore
                t("buttons.done.success", lang=lang, index=index + 1)
            )
        except IndexError:
            await query.edit_message_text(t("buttons.task_not_found", lang=lang))  # type: ignore
    elif action == "delete":
        try:
            todos.delete_task(user_id, index)
            await query.edit_message_text(  # type: ignore
                t("buttons.delete.success", lang=lang, index=index + 1)
            )
        except IndexError:
            await query.edit_message_text(t("buttons.task_not_found", lang=lang))  # type: ignore
