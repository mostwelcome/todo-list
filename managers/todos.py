from database.db import db
from database.models.tables.todo import Todo
from datetime import datetime

def add_todo():
    todo = Todo(title='Start learning react', content='This is very important')
    db.session.add(todo)
    db.session.commit()


def get_todos():
    all_todo = Todo.query.all()
    return all_todo
