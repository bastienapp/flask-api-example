import requests

BASE_URL = "http://127.0.0.1:5000"


def test_bad_login():
    response = requests.post(
        BASE_URL + "/login", json={
            "email": "michel@michel.fr",
            "password": "michel"
        })
    assert response.status_code == 401


def test_good_login():
    response = requests.post(
        BASE_URL + "/login", json={
            "email": "tacoscopy@test.fr",
            "password": "tacostacos"
        })
    assert response.status_code == 200
    data = response.json()
    assert data.get("token") is not None
