from telegram import Update
from telegram.ext import ContextTypes
from src.storage import todos


async def delete_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("usage: /delete <todo_index>")
        return

    index = int(context.args[0]) - 1  # Convert to zero-based index
    try:
        todos.delete_task(user_id, index)
        await update.message.reply_text(f"deleted task #{index + 1}.")
    except IndexError:
        await update.message.reply_text("task not found.")
