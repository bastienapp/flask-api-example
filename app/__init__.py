import os
from flask import Flask

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

# uncomment to drop and/or create tables
#app.app_context().push()
#from app import migration
#migration.drop()
#migration.create()

from app.routes import dish