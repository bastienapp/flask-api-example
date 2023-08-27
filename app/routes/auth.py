import datetime
from functools import wraps
from flask import abort, jsonify, request
import jwt
from app import app, db, bcrypt
from app.models.user import User

app.config['SECRET_KEY'] = 'tacostacostacostacostacostacostacostacostacostacostacostacos'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user: User = User.query.filter(User.email == data.get('email')).first()

    if (user is None):
        abort(401)

    if (not bcrypt.check_password_hash(user.password, data.get('password'))):
        abort(401)

    token = jwt.encode(
        {
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token})


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not "authorization" in request.headers:
            abort(401)

        auth = request.headers["authorization"]
        token = ''
        if auth:
            try:
                token = auth.split(" ")[1]
            except IndexError:
                abort(401)
        else:
            abort(401)

        if token:
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

                if not data['email'] or not data['exp']:
                    abort(401)

                current_user: User = User.query.filter(
                    User.email == data['email']).first()

                if current_user is None:
                    abort(401)

                return func(current_user, *args, **kwargs)
            except Exception as error:
                print(error)
                abort(401)

    return wrapper
