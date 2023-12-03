import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Cake API"}

def test_list_cakes():
    response = client.get("/cakes")
    assert response.status_code == 200
    assert response.json() == []

def test_create_cake():
    new_cake = {
        "id": 1,
        "name": "Chocolate Cake",
        "comment": "Delicious chocolate cake",
        "imageUrl": "chocolate.jpg",
        "yumFactor": 5
    }
    response = client.post("/cakes", json=new_cake)
    assert response.status_code == 200
    assert response.json() == new_cake

def test_delete_cake():
    response = client.delete("/cakes/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Chocolate Cake",
        "comment": "Delicious chocolate cake",
        "imageUrl": "chocolate.jpg",
        "yumFactor": 5
    }
