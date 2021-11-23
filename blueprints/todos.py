from database.models.tables.todo import Todo
from flask import Blueprint, render_template
from managers.todos import add_todo, get_todos

TODOS_BLUEPRINT = Blueprint('todos', __name__)


@TODOS_BLUEPRINT.route('/add')
def add_todo_item():
    add_todo()
    return render_template('index.html')


@TODOS_BLUEPRINT.route('/')
def get_todo_list():
    all_todo = get_todos()
    return render_template('index.html', all_todo=all_todo)
