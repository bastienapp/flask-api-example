from dataclasses import dataclass
from app import db

@dataclass
class Dish(db.Model):
  id: int
  name: str
  description: str
  price: float

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=False, nullable=False)
  description = db.Column(db.Text, unique=False, nullable=False)
  price = db.Column(db.Float, unique=False, nullable=False)