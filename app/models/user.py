from dataclasses import dataclass
from app import db

@dataclass
class User(db.Model):
    id: int
    email: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)