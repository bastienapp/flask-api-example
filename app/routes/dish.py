from flask import abort, jsonify, request
from app import app, db
from app.models.dish import Dish

@app.route('/dishes', methods=['GET'])
def getAll():
    return jsonify(Dish.query.all())

@app.route('/dishes/<int:id>', methods=['GET'])
def getOne(id):
    dish = Dish.query.get(id)
    if dish is None:
        abort(404)
    return jsonify(dish)

@app.route('/dishes', methods=['POST'])
def create():
    data = request.get_json()
    newDish = Dish(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price')
    )
    db.session.add(newDish)
    db.session.commit()
    return jsonify(newDish)