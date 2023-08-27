from flask import jsonify, request
from app import app, db, bcrypt
from app.models.user import User


@app.route('/users', methods=['POST'])
def createUser():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(
        data.get('password')
    ).decode('utf-8')
    new_user = User(
        email=data.get('email'),
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)
