from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from tick_telegram_bot.localization import get_user_language, t
from tick_telegram_bot.storage import todos


async def list_handler(update: Update, context: CallbackContext) -> None:
    lang = get_user_language(update)
    try:
        user_id = update.effective_user.id
    except AttributeError:
        if update.callback_query:
            await update.callback_query.answer(t("errors.user_unknown", lang=lang))
        else:
            await update.message.reply_text(t("errors.user_unknown", lang=lang))
        return

    task_items = todos.list_tasks(user_id)

    if not task_items:
        text = t("list.empty", lang=lang)
        if update.message:
            await update.message.reply_text(text)
        elif update.callback_query:
            await update.callback_query.edit_message_text(text)
        return

    done_label = t("list.buttons.done", lang=lang)
    delete_label = t("list.buttons.delete", lang=lang)

    for index, item in enumerate(task_items):
        status = "✅" if item["done"] else ""
        text = f"{index + 1}. {item['title']} {status}"

        keyboard = [
            [
                InlineKeyboardButton(done_label, callback_data=f"done:{index}"),
                InlineKeyboardButton(delete_label, callback_data=f"delete:{index}"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.message:
            await update.message.reply_text(text, reply_markup=reply_markup)
        elif update.callback_query:
            await update.callback_query.message.reply_text(
                text, reply_markup=reply_markup
            )
