from telegram import Update
from telegram.ext import CallbackContext
from storage import todos


async def list_handler(update: Update, context: CallbackContext) -> None:
    try:
        user_id = update.effective_user.id
    except AttributeError:
        await update.message.reply_text("could not identify user.")
        return

    todoes_items = todos.list_todos(user_id)

    if not todoes_items:
        await update.message.reply_text("you have no todo items.")
        return

    message_lines = []
    for index, item in enumerate(todoes_items):
        status = "✓" if item["done"] else " "
        message_lines.append(f"{index + 1}. {item['title']} {status}")

    message = "\n".join(message_lines)
    await update.message.reply_text(message)
