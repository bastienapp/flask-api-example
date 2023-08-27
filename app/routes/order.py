from flask import abort, jsonify, request
from app import app, db
from app.models.dish import Dish
from app.models.order import Order
from app.models.order_status import OrderStatus

@app.route('/orders', methods=['GET'])
def getAllOrders():
    return jsonify(Order.query.all())

@app.route('/orders/<int:id>', methods=['GET'])
def getOneOrder(id):
    order = Order.query.get(id)
    if order is None:
        abort(404)
    return jsonify(order)

@app.route('/orders', methods=['POST'])
def createOrder():
    data = request.get_json()
    new_order = Order(
        user_id=data.get('user_id'),
        status=OrderStatus.PENDING,
        dishes=[],
    )

    for dish_data in data.get('dishes'):
        dish = Dish.query.get(dish_data.get('id'))
        if dish is None:
            abort(404)
        new_order.dishes.append(dish)

    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order)