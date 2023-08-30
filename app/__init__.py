from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from app.routes import database, dish, order, user, auth  # noqa
