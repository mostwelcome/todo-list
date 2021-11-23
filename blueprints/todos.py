from database.models.tables.todo import Todo
from flask import Blueprint, render_template, request, redirect, url_for
from managers.todos import add_todo, get_todos, delete_todo

TODOS_BLUEPRINT = Blueprint('todos', __name__)


@TODOS_BLUEPRINT.route('/add', methods=['GET', 'POST'])
def add_todo_item():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']
        add_todo(title, desc)
        return redirect(url_for('todos.get_todo_list'))


@TODOS_BLUEPRINT.route('/update/<int:sno>')
def update_todo_item(sno):
    pass


@TODOS_BLUEPRINT.route('/delete/<int:sno>')
def delete_todo_item(sno):
    delete_todo(sno)
    return redirect(url_for('todos.get_todo_list'))


@TODOS_BLUEPRINT.route('/')
def get_todo_list():
    all_todo = get_todos()
    return render_template('index.html', all_todo=all_todo)
