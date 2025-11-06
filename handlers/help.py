from telegram import Update
from telegram.ext import ContextTypes

HELP_TEXT = (
    "*tick commands*\n\n"
    "/start — welcome message\n"
    "/help — show this help\n"
    "/add <title> [description] — add a task\n"
    "/list — list all tasks\n"
    "/done <index> — mark as done\n"
    "/adddesc <index> <description> — add or update description\n"
    "/delete <index> — delete a task\n"
    "/clear — clear all tasks"
)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode="Markdown")
