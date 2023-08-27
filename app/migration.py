from app import db

from app.models.dish import Dish
from app.models.order_status import OrderStatus
from app.models.order import Order
from app.models.user import User


def drop():
    db.drop_all()


def create():
    db.create_all()
