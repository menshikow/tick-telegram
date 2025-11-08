import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

PATH = Path(__file__).parent.parent / "data" / "todos.json"


def _ensure_file():
    os.makedirs(PATH.parent, exist_ok=True)
    if not PATH.exists():
        PATH.write_text("{}", encoding="utf-8")


def _safe_load():
    _ensure_file()
    try:
        with PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Reset corrupted or unreadable file
        PATH.write_text("{}", encoding="utf-8")
        return {}


def _safe_save(data):
    os.makedirs(PATH.parent, exist_ok=True)
    # atomic write: write to tmp, then replace
    with NamedTemporaryFile(
        "w", dir=PATH.parent, delete=False, encoding="utf-8"
    ) as tmp:
        json.dump(data, tmp, indent=4)
        tmp.flush()
        os.fsync(tmp.fileno())
    os.replace(tmp.name, PATH)


def add(user_id, title, description=""):
    data = _safe_load()
    todos = data.setdefault(str(user_id), [])
    todos.append({"title": title, "description": description, "done": False})
    _safe_save(data)


def list_tasks(user_id):
    return _safe_load().get(str(user_id), [])


def mark_done(user_id, index):
    data = _safe_load()
    todos = data.get(str(user_id), [])
    try:
        todos[index]["done"] = True
    except IndexError:
        raise IndexError("task not found.")
    _safe_save(data)


def add_description(user_id, index, description):
    data = _safe_load()
    todos = data.get(str(user_id), [])
    try:
        todos[index]["description"] = description
    except IndexError:
        raise ValueError("task with the given index not found.")
    _safe_save(data)


def delete_task(user_id, index):
    data = _safe_load()
    todos = data.get(str(user_id), [])
    try:
        todos.pop(index)
    except IndexError:
        raise IndexError("task not found.")
    _safe_save(data)


def clear_all(user_id):
    data = _safe_load()
    data[str(user_id)] = []
    _safe_save(data)
