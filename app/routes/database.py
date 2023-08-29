from flask import jsonify
from app import app, db


@app.route('/create-database', methods=['GET'])
def create_database():
    with app.app_context():
        # db.drop_all()
        db.create_all()
    return jsonify({'message': 'Database created'})
