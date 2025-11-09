import json

import pytest

from tick_telegram.storage import todos


@pytest.fixture(autouse=True)
def temp_todo_file(tmp_path, monkeypatch):
    """Force the storage module to use an isolated JSON file per test."""
    temp_path = tmp_path / "todos.json"
    monkeypatch.setattr(todos, "PATH", temp_path)
    yield temp_path


def test_add_and_list_tasks(temp_todo_file):
    todos.add(user_id=123, title="buy milk")
    todos.add(user_id=123, title="write report", description="due friday")

    tasks = todos.list_tasks(123)

    assert tasks == [
        {"title": "buy milk", "description": "", "done": False},
        {"title": "write report", "description": "due friday", "done": False},
    ]


def test_mark_done_updates_task_status(temp_todo_file):
    todos.add(1, "task a")
    todos.add(1, "task b")

    todos.mark_done(1, 1)

    tasks = todos.list_tasks(1)
    assert tasks[0]["done"] is False
    assert tasks[1]["done"] is True


def test_mark_done_invalid_index_raises(temp_todo_file):
    todos.add(1, "only task")

    with pytest.raises(IndexError, match="task not found\\.|task not found."):
        todos.mark_done(1, 5)


def test_add_description_updates_existing_task(temp_todo_file):
    todos.add(1, "task without description")

    todos.add_description(1, 0, "add more details")

    tasks = todos.list_tasks(1)
    assert tasks[0]["description"] == "add more details"


def test_delete_task_removes_task(temp_todo_file):
    todos.add(1, "task a")
    todos.add(1, "task b")

    todos.delete_task(1, 0)

    tasks = todos.list_tasks(1)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "task b"


def test_delete_invalid_index_raises(temp_todo_file):
    with pytest.raises(IndexError, match="task not found\\.|task not found."):
        todos.delete_task(1, 0)


def test_clear_all_resets_only_selected_user(temp_todo_file):
    todos.add(1, "user1 task")
    todos.add(2, "user2 task")

    todos.clear_all(1)

    assert todos.list_tasks(1) == []
    assert todos.list_tasks(2) == [
        {"title": "user2 task", "description": "", "done": False}
    ]


def test_corrupt_file_is_reset(temp_todo_file):
    temp_todo_file.parent.mkdir(parents=True, exist_ok=True)
    temp_todo_file.write_text("{invalid json", encoding="utf-8")

    tasks = todos.list_tasks(42)

    assert tasks == []
    assert json.loads(temp_todo_file.read_text(encoding="utf-8")) == {}
