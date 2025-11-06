from telegram import Update
from telegram.ext import ContextTypes
from storage import todos


async def add_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if not context.args:
        await update.message.reply_text("please provide a title for the todo item.")
        return

    title = context.args[0]
    description = " ".join(context.args[1:]) if len(context.args) > 1 else ""
    user_id = update.effective_user.id

    todos.add(user_id, title, description)
    await update.message.reply_text(
        f'todo item "{title}" added.'
        if description == ""
        else f'todo item "{title}" with description "{description}" added.'
    )
