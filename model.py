from datetime import datetime

from pprint import pprint as pp

from helpers import generate_id

todos = [
    {
        "id": 1,
        "title": "lear python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now()
    },
    {
        "id": 5,
        "title": "lear python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now()
    }
]


def add_todo(tasks, title, duration=60):
    todo = {
        "id": generate_id(tasks),
        "title": title,
        "status": False,
        "duration": duration,
        "created_date": datetime.now()
    }

    tasks.append(todo)


def find_todo_by_id(tasks, idx):
    for task in tasks:
        if task["id"] == idx:
            return task


def toggle_status(tasks, idx):
    task = find_todo_by_id(tasks, idx)
    task["status"] = not task["status"]


def delete_todo(tasks, idx):
    task = find_todo_by_id(tasks, idx)
    tasks.remove(task)
