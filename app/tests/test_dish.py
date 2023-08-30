import requests


ENDPOINT = 'http://localhost:5000/dishes'

response = requests.post(ENDPOINT, json={
    'name': 'Pasta',
    'price': 10.99,
    'description': 'Pasta with tomato sauce'
})

assert response.status_code == 201
assert response.json()['name'] == 'Pasta'
assert response.json()['price'] == 10.99
assert response.json()['description'] == 'Pasta with tomato sauce'
