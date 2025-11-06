from telegram import Update
from telegram.ext import ContextTypes
from storage import todos


async def clear_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    todos.clear_all(user_id)
    await update.message.reply_text("all your tasks have been cleared.")
