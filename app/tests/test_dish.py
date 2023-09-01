import requests

BASE_URL = "http://127.0.0.1:5000/dishes"


def test_post_dishes():
    response = requests.post(
        BASE_URL, json={
            "name": "test name",
            "description": "test description",
            "price": 1.0})
    assert response.status_code == 201
    data = response.json()
    assert data.get("name") == "test name"
    assert data.get("description") == "test description"
    assert data.get("price") == 1.0

    dish_id = data.get("id")

    response = requests.get(f"{BASE_URL}/{dish_id}")
    assert response.status_code == 200
    data = response.json()
    assert data.get("name") == "test name"
    assert data.get("description") == "test description"
    assert data.get("price") == 1.0

    response = requests.delete(f"{BASE_URL}/{dish_id}")

    assert response.status_code == 200
    data = response.json()
    assert data.get("deleted") == dish_id
