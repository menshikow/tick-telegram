import json
import os
from pathlib import Path

PATH = Path(__file__).parent.parent / "data" / "todos.json"


def _ensure_file():
    os.makedirs(PATH.parent, exist_ok=True)
    if not PATH.exists():
        PATH.write_text("{}", encoding="utf-8")


def load():
    _ensure_file()
    with PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save(data):
    os.makedirs(PATH.parent, exist_ok=True)
    with PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add(user_id, title, description=""):
    data = load()
    user_todos = data.setdefault(str(user_id), [])
    user_todos.append({"title": title, "description": description, "done": False})
    save(data)


def list_todos(user_id):
    data = load()
    return data.get(str(user_id), [])


def mark_done(user_id, index):
    data = load()
    todos = data.get(str(user_id), [])
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save(data)
    else:
        raise IndexError("Todo item not found.")


def add_description(user_id, index, description):
    data = load()
    todos = data.get(str(user_id), [])
    if not (0 <= index < len(todos)):
        raise ValueError("Todo item with the given index not found.")
    todos[index]["description"] = description
    save(data)


def delete_todo(user_id, index):
    data = load()
    todos = data.get(str(user_id), [])
    if 0 <= index < len(todos):
        todos.pop(index)
        save(data)
    else:
        raise IndexError("todo item not found.")


def clear_all(user_id):
    data = load()
    data[str(user_id)] = []  # replace with a new empty list
    save(data)
