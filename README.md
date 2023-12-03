# FASTAPICakes

Below is a comprehensive listing of all the code, including the FastAPI script, PyTest test cases, and Docker-related files. Additionally, I've included installation steps and implementation details.
This comprehensive guide covers installation, FastAPI script, PyTest test cases, Docker setup, and Kubernetes deployment for the Cake API.



# Installation
# Step 1 Install Python and Setup Virtual Environment
 Install Python (skip if already installed)
 Visit https://www.python.org/downloads/
 Follow the installation instructions

# Install virtualenv
pip install virtualenv

# Create and activate a virtual environment
# On Linux/Mac
virtualenv venv
source venv/bin/activate

# On Windows
.\venv\Scripts\activate

# Step 2: Install FastAPI, Uvicorn, and PyTest
# Install FastAPI and Uvicorn
pip install fastapi uvicorn

# Install PyTest
pip install pytest

# FastAPI Script (main.py) 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cake(BaseModel):
    id: int
    name: str
    comment: str
    imageUrl: str
    yumFactor: int

cakes = []

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Cake API"}

@app.get("/cakes", response_model=List[Cake], tags=["Cakes"])
def list_cakes():
    """
    Retrieve a list of all cakes.
    """
    return cakes

@app.post("/cakes", response_model=Cake, tags=["Cakes"])
def create_cake(cake: Cake):
    """
    Create a new cake.
    """
    cakes.append(cake)
    return cake

@app.delete("/cakes/{cake_id}", response_model=Cake, tags=["Cakes"])
def delete_cake(cake_id: int):
    """
    Delete a cake by ID.
    """
    for i, cake in enumerate(cakes):
        if cake.id == cake_id:
            deleted_cake = cakes.pop(i)
            return deleted_cake
    raise HTTPException(status_code=404, detail="Cake not found")

""" 
Include OpenAPI documentation
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)

# PyTest Test Cases (test_main.py)
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

# Docker Setup
Dockerfile (Dockerfile) as follows :
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app


# Running the Application
Run FastAPI Locally as follows :
uvicorn main:app --reload


# Access OpenAPI documentation: http://127.0.0.1:8000/docs

# Run PyTest
pytest


# Build Docker image
docker build -t cake-api .

# Run Docker container
docker run -d -p 80:80 cake-api


# Kubernetes Setup
# Kubernetes Deployment (deployment.yaml) :

apiVersion: apps/v1
kind: Deployment
metadata:
  name: cake-api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cake-api
  template:
    metadata:
      labels:
        app: cake-api
    spec:
      containers:
      - name: cake-api
        image: cake-api:latest
        ports:
        - containerPort: 80


# Kubernetes Service (service.yaml)
apiVersion: v1
kind: Service
metadata:
  name: cake-api-service
spec:
  selector:
    app: cake-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer


# Apply Kubernetes Manifests

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Access the API in Kubernetes :
kubectl get service cake-api-service

Access the API using the assigned external IP.










