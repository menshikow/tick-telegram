from telegram import Update
from telegram.ext import ContextTypes
from src.storage import todos


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    action, index_str = query.data.split(":")
    index = int(index_str)

    if action == "done":
        try:
            todos.mark_done(user_id, index)
            await query.edit_message_text(f"✓ marked task #{index + 1} as done.")
        except IndexError:
            await query.edit_message_text("task not found.")
    elif action == "delete":
        try:
            todos.delete_task(user_id, index)
            await query.edit_message_text(f"🗑 deleted task #{index + 1}.")
        except IndexError:
            await query.edit_message_text("task not found.")
