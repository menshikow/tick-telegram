from telegram import Update
from telegram.ext import ContextTypes
from src.storage import todos
from src.handlers.help import HELP_TEXT


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    action = query.data.split(":")[1]

    if action == "add":
        await query.edit_message_text("Use /add <title> to add a new task.")
    elif action == "list":
        from src.handlers.list import list_handler

        await list_handler(update, context)
    elif action == "clear":
        todos.clear_all(user_id)
        await query.edit_message_text("🧹 All tasks cleared!")
    elif action == "help":
        await query.edit_message_text(HELP_TEXT, parse_mode="Markdown")
