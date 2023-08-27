from app import db
from app.models.order_status import OrderStatus

order_dishes = db.Table('order_dish',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False, default=1)
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dishes = db.relationship('Dish', secondary=order_dishes, backref=db.backref('orders', lazy=True))
    status = db.Column(db.Enum(OrderStatus), nullable=False)