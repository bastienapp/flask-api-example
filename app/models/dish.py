from app import db

class Dish(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True, nullable=False)
  description = db.Column(db.Text, unique=False, nullable=False)
  price = db.Column(db.Float, unique=False, nullable=False)