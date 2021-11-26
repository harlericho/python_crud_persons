from flask import Flask
from routes.persons import persons
from flask_sqlalchemy import SQLAlchemy
from config import url_connection

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = url_connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)
app.register_blueprint(persons)