from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from src.storage import todos


async def list_handler(update: Update, context: CallbackContext) -> None:
    try:
        user_id = update.effective_user.id
    except AttributeError:
        if update.callback_query:
            await update.callback_query.answer("could not identify user.")
        else:
            await update.message.reply_text("could not identify user.")
        return

    task_items = todos.list_tasks(user_id)

    if not task_items:
        text = "you have no task items."
        if update.message:
            await update.message.reply_text(text)
        elif update.callback_query:
            await update.callback_query.edit_message_text(text)
        return

    for index, item in enumerate(task_items):
        status = "✅" if item["done"] else ""
        text = f"{index + 1}. {item['title']} {status}"

        keyboard = [
            [
                InlineKeyboardButton("✅ Done", callback_data=f"done:{index}"),
                InlineKeyboardButton("🗑 Delete", callback_data=f"delete:{index}"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.message:
            await update.message.reply_text(text, reply_markup=reply_markup)
        elif update.callback_query:
            await update.callback_query.message.reply_text(
                text, reply_markup=reply_markup
            )
