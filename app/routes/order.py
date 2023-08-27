from flask import abort, jsonify, request
from app import app, db
from app.models.dish import Dish
from app.models.order import Order
from app.models.order_status import OrderStatus
from app.routes.auth import token_required


@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify(Order.query.all())


@app.route('/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    order = Order.query.get(id)
    if order is None:
        abort(404)

    return jsonify(order)


@app.route('/orders/status/<status>', methods=['GET'])
def get_order_by_status(status):
    order = Order.query.filter(Order.status == status).all()
    if order is None:
        abort(404)

    return jsonify(order)


@app.route('/orders', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    new_order = Order(
        user_id=current_user.id,
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


@app.route('/orders/<int:id>/status/<status>', methods=['PUT'])
@token_required
def update_order_status(current_user, id, status):
    order = Order.query.get(id)
    if order is None:
        abort(404)

    if (current_user.id != order.user_id):
        # user can only update their own orders
        abort(401)

    if not OrderStatus.has_value(status):
        # invalid status
        abort(400)

    order.status = status
    db.session.commit()
    return jsonify(order)
