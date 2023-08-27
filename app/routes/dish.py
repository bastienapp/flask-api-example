from flask import abort, jsonify, request
from app import app, db
from app.models.dish import Dish

@app.route('/dishes', methods=['GET'])
def getAllDishes():
    return jsonify(Dish.query.all())

@app.route('/dishes/<int:id>', methods=['GET'])
def getOneDish(id):
    dish = Dish.query.get(id)
    if dish is None:
        abort(404)
    return jsonify(dish)

@app.route('/dishes', methods=['POST'])
def createDish():
    data = request.get_json()
    new_dish = Dish(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price')
    )
    db.session.add(new_dish)
    db.session.commit()
    return jsonify(new_dish)