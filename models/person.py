from utils.db import db

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(10), unique=True)

    def __init__(self, names, email, phone):
        self.names = names
        self.email = email
        self.phone = phone