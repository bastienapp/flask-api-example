import requests

BASE_URL = "http://127.0.0.1:5000"


def test_order_not_logged_in():
    response = requests.post(BASE_URL + '/orders', json={
        "dishes": [1],
    })
    assert response.status_code == 401


def test_order_wrong_jwt():
    response = requests.post(BASE_URL + '/orders', json={
        "dishes": [1],
    }, headers={
        "Authorization": "Bearer MYREALLYLONGTOKENIGOT"
    })
    assert response.status_code == 401


def test_order_good_jwt():
    response = requests.post(
        BASE_URL + "/login", json={
            "email": "tacoscopy@test.fr",
            "password": "tacostacos"
        })
    jwt = response.json().get("token")

    response = requests.post(BASE_URL + '/orders', json={
        "dishes": [{"id": 1}],
    }, headers={
        "Authorization": f"Bearer {jwt}"
    })
    assert response.status_code == 201
    data = response.json()
    assert data.get("status") == "Pending"
    assert data.get("dishes")[0].get("id") == 1
    assert data.get("user_id") == 1
