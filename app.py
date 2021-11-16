from flask import Flask
from database.db import db

app = Flask(__name__)


@app.before_first_request
def create_tables():
    db.create_all()


app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)


@app.route('/')
def home():
    return "Hello"


if __name__ == '__main__':
    app.run()
