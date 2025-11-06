from telegram import Update
from telegram.ext import ContextTypes
from storage import todos


async def add_description_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if len(context.args) < 2:
        await update.message.reply_text("usage: /adddesc <index> <description>")
        return

    try:
        index = int(context.args[0]) - 1
    except ValueError:
        await update.message.reply_text("the index must be a number.")
        return

    description = " ".join(context.args[1:])
    user_id = update.effective_user.id

    try:
        todos.add_description(user_id, index, description)
        await update.message.reply_text(
            f'added description "{description}" to task number {index + 1}.'
        )
    except IndexError:
        await update.message.reply_text("invalid task number.")
