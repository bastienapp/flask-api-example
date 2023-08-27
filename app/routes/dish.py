from flask import abort, jsonify, request
from app import app, db
from app.models.dish import Dish


@app.route('/dishes', methods=['GET'])
def get_all_dishes():
    return jsonify(Dish.query.all())


@app.route('/dishes/<int:id>', methods=['GET'])
def get_dish_by_id(id):
    dish = Dish.query.get(id)
    if dish is None:
        abort(404)

    return jsonify(dish)


@app.route('/dishes', methods=['POST'])
def create_dish():
    data = request.get_json()
    new_dish = Dish(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price')
    )

    db.session.add(new_dish)
    db.session.commit()
    return jsonify(new_dish)


@app.route('/dishes/<int:id>', methods=['PUT'])
def update_dish(id):
    dish = Dish.query.get(id)
    if dish is None:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400)

    if (data.get('name')):
        dish.name = data.get('name')
    if (data.get('description')):
        dish.description = data.get('description')
    if (data.get('price')):
        dish.price = data.get('price')

    db.session.commit()
    return jsonify(dish)


@app.route('/dishes/<int:id>', methods=['DELETE'])
def delete_dish_by_id(id):
    dish = Dish.query.get(id)
    if dish is None:
        abort(404)

    db.session.delete(dish)
    db.session.commit()
    return jsonify({'deleted': dish.id})
