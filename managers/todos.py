from database.db import db
from database.models.tables.todo import Todo
from datetime import datetime


def add_todo(title, description):
    todo = Todo(title=title, content=description)
    db.session.add(todo)
    db.session.commit()


def get_todos():
    all_todo = Todo.query.all()
    return all_todo


def delete_todo(sno):
    todo_item = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo_item)
    db.session.commit()


def update_todo(sno):
    pass
