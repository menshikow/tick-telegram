from telegram import Update
from telegram.ext import ContextTypes
from tick_telegram_bot.handlers.help import get_help_text
from tick_telegram_bot.localization import get_user_language, t
from tick_telegram_bot.storage import todos


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    action = query.data.split(":")[1]
    lang = get_user_language(update)

    if action == "add":
        await query.edit_message_text(t("menu.add_prompt", lang=lang))
    elif action == "list":
        from tick_telegram_bot.handlers.list import list_handler

        await list_handler(update, context)
    elif action == "clear":
        todos.clear_all(user_id)
        await query.edit_message_text(t("menu.cleared", lang=lang))
    elif action == "help":
        await query.edit_message_text(get_help_text(lang), parse_mode="Markdown")
