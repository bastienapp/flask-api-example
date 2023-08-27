from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

reset_database = False  # set to True to reset the database
if reset_database:
    app.app_context().push()
    from app import migration
    migration.drop()
    migration.create()

bcrypt = Bcrypt(app)

from app.routes import dish, order, user, auth
