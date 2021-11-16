from database.db import db
from datetime import datetime


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.Date, default=datetime.utcnow())

    def __repr__(self):
        return f'{self.sno} {self.title}'
