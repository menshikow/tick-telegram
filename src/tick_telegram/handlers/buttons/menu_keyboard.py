from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tick_telegram.localization import t


def build_main_menu(lang: str = "en"):
    keyboard = [
        [
            InlineKeyboardButton(
                t("menu.buttons.add", lang=lang), callback_data="menu:add"
            ),
            InlineKeyboardButton(
                t("menu.buttons.list", lang=lang), callback_data="menu:list"
            ),
        ],
        [
            InlineKeyboardButton(
                t("menu.buttons.clear", lang=lang), callback_data="menu:clear"
            ),
            InlineKeyboardButton(
                t("menu.buttons.help", lang=lang), callback_data="menu:help"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
