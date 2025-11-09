"""Simple localization utilities for the bot."""

from __future__ import annotations

from typing import Any, Mapping

DEFAULT_LANG = "en"
SUPPORTED_LANGS = {"en", "ru"}


TRANSLATIONS: Mapping[str, Mapping[str, str]] = {
    "add.missing_title": {
        "en": "please provide a title for the task.",
        "ru": "пожалуйста, укажите название задачи.",
    },
    "add.success_no_desc": {
        "en": 'task "{title}" added.',
        "ru": 'таска "{title}" добавлена.',
    },
    "add.success_with_desc": {
        "en": 'task "{title}" with description "{description}" added.',
        "ru": 'таска "{title}" с описанием "{description}" добавлена.',
    },
    "adddesc.usage": {
        "en": "usage: /adddesc <index> <description>",
        "ru": "использование: /adddesc <номер> <описание>",
    },
    "adddesc.index_not_number": {
        "en": "the index must be a number.",
        "ru": "индекс должен быть числом.",
    },
    "adddesc.success": {
        "en": 'added description "{description}" to task number {index}.',
        "ru": 'описание "{description}" добавлено к таске №{index}.',
    },
    "adddesc.invalid_index": {
        "en": "invalid task number.",
        "ru": "неверный номер таски.",
    },
    "errors.user_unknown": {
        "en": "could not identify user.",
        "ru": "не удалось определить пользователя.",
    },
    "errors.index_number_required": {
        "en": "please provide a valid number for the index.",
        "ru": "пожалуйста, введите корректный номер.",
    },
    "errors.task_not_found": {
        "en": "task not found.",
        "ru": "таска не найдена.",
    },
    "errors.task_not_found_retry": {
        "en": "task not found. please check the index and try again.",
        "ru": "таска не найдена. проверьте номер и попробуйте снова.",
    },
    "list.empty": {
        "en": "you have no task items.",
        "ru": "у вас нет тасок.",
    },
    "done.missing_index": {
        "en": "please provide the index of the task to mark as done.",
        "ru": "укажите номер таски, чтобы отметить её выполненной.",
    },
    "done.success": {
        "en": "marked task #{index} as done.",
        "ru": "таска №{index} отмечена выполненной.",
    },
    "delete.usage": {
        "en": "usage: /delete <todo_index>",
        "ru": "использование: /delete <номер_таски>",
    },
    "delete.success": {
        "en": "deleted task #{index}.",
        "ru": "таска №{index} удалена.",
    },
    "clear.cleared": {
        "en": "all your tasks have been cleared.",
        "ru": "все ваши таски удалены.",
    },
    "fallback.unknown_command": {
        "en": "I didn’t recognize that command.\n\n",
        "ru": "я не понял эту команду.\n\n",
    },
    "help.text": {
        "en": (
            "*tick commands*\n\n"
            "/start — welcome message\n"
            "/help — show this help\n"
            "/add <title> [description] — add a task\n"
            "/list — list all tasks\n"
            "/done <index> — mark as done\n"
            "/adddesc <index> <description> — add or update description\n"
            "/delete <index> — delete a task\n"
            "/clear — clear all tasks"
        ),
        "ru": (
            "*команды tick*\n\n"
            "/start — приветственное сообщение\n"
            "/help — показать эту справку\n"
            "/add <название> [описание] — добавить задачу\n"
            "/list — показать все задачи\n"
            "/done <номер> — отметить выполненной\n"
            "/adddesc <номер> <описание> — добавить или изменить описание\n"
            "/delete <номер> — удалить задачу\n"
            "/clear — очистить список задач"
        ),
    },
    "start.welcome": {
        "en": (
            " Welcome to *tick!* 👋\n"
            "Your personal to-do bot.\n\n"
            "Use the buttons below to get started:"
        ),
        "ru": (
            " Добро пожаловать в *tick!* 👋\n"
            "Ваш личный бот-список дел.\n\n"
            "Используйте кнопки ниже, чтобы начать:"
        ),
    },
    "menu.add_prompt": {
        "en": "Use /add <title> to add a new task.",
        "ru": "Используйте /add <название>, чтобы добавить новую задачу.",
    },
    "menu.cleared": {
        "en": "🧹 All tasks cleared!",
        "ru": "🧹 Все таски очищены!",
    },
    "menu.buttons.add": {
        "en": "📝 Add Task",
        "ru": "📝 Добавить",
    },
    "menu.buttons.list": {
        "en": "📋 List Tasks",
        "ru": "📋 Список Тасок",
    },
    "menu.buttons.clear": {
        "en": "🧹 Clear All",
        "ru": "🧹 Очистить",
    },
    "menu.buttons.help": {
        "en": "❓ Help",
        "ru": "❓ Помощь",
    },
    "list.buttons.done": {
        "en": "✅ Done",
        "ru": "✅ Готово",
    },
    "list.buttons.delete": {
        "en": "🗑 Delete",
        "ru": "🗑 Удалить",
    },
    "buttons.done.success": {
        "en": "✓ marked task #{index} as done.",
        "ru": "✓ задача №{index} отмечена выполненной.",
    },
    "buttons.delete.success": {
        "en": "🗑 deleted task #{index}.",
        "ru": "🗑 задача №{index} удалена.",
    },
    "buttons.task_not_found": {
        "en": "task not found.",
        "ru": "задача не найдена.",
    },
}


def normalize_lang(lang_code: str | None) -> str:
    if not lang_code:
        return DEFAULT_LANG
    normalized = lang_code.split("-")[0].lower()
    return normalized if normalized in SUPPORTED_LANGS else DEFAULT_LANG


def get_user_language(update: Any) -> str:
    user = getattr(update, "effective_user", None)
    lang_code = getattr(user, "language_code", None)
    return normalize_lang(lang_code)


def t(key: str, lang: str | None = None, **kwargs: Any) -> str:
    lang = normalize_lang(lang or DEFAULT_LANG)
    entries = TRANSLATIONS.get(key, {})
    template = entries.get(lang) or entries.get(DEFAULT_LANG) or key
    return template.format(**kwargs)
