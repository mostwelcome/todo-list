from flask import Flask, url_for, redirect
from database.db import db
from blueprints.todos import TODOS_BLUEPRINT

app = Flask(__name__)


@app.before_first_request
def create_tables():
    db.create_all()


app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)
app.register_blueprint(TODOS_BLUEPRINT, url_prefix='/todos')


@app.route('/')
def home():
    return redirect(url_for('todos.get_todo_list'))


if __name__ == '__main__':
    app.run()
