from . import db

class Todo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    content = db.Column(db.String(80), nullable = False)
    complete = db.Column(db.Boolean, default=False)