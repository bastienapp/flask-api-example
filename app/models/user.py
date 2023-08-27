from dataclasses import dataclass
from enum import Enum
from app import db


class RoleNames(Enum):
    USER = 0
    ADMIN = 1


@dataclass
class User(db.Model):
    id: int
    email: str

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    role = db.Column(db.Enum(RoleNames), unique=False,
                     nullable=False, default=RoleNames.USER)
