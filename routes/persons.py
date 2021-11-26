from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from utils.db import db
from models.person import Person

persons = Blueprint('persons', __name__)

@persons.route('/')
def index():
    try:
        data = Person.query.all()
        return render_template('index.html', list=data)
    except Exception as e:
        return render_template('error.html', error=e)

@persons.route('/add', methods=['GET', 'POST'])
def add():
    names = request.form.get("names")
    email = request.form.get("email")
    phone = request.form.get("phone")
    data = Person(names, email, phone)
    db.session.add(data)
    db.session.commit()
    flash("Person saved successfully")
    return redirect(url_for("persons.index"))

@persons.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    data = Person.query.get(id)
    if request.method == "POST":
        names = request.form.get("names")
        email = request.form.get("email")
        phone = request.form.get("phone")
        data.names = names
        data.email = email
        data.phone = phone
        db.session.commit()
        flash("Person updated successfully")
        return redirect(url_for("persons.index"))
    return render_template("update.html", data=data)

@persons.route('/delete/<int:id>')
def delete(id):
    data = Person.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash("Person deleted successfully")
    return redirect(url_for("persons.index"))