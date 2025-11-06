from telegram import Update
from telegram.ext import ContextTypes
from src.storage import todos


async def done_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text(
            "please provide the index of the todo item to mark as done."
        )
        return

    try:
        index = int(context.args[0]) - 1  # Convert to zero-based index
    except ValueError:
        await update.message.reply_text("please provide a valid number for the index.")
        return

    try:
        user_id = update.effective_user.id
    except AttributeError:
        await update.message.reply_text("could not identify user.")
        return

    try:
        todos.mark_done(user_id, index)
        await update.message.reply_text(f"marked todo item #{index + 1} as done.")
    except IndexError:
        await update.message.reply_text(
            "todo item not found. please check the index and try again."
        )
