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
see :
https://github.com/goldcupco/FASTAPICakes/blob/main/main.py


# PyTest Test Cases (test_main.py)
see :
https://github.com/goldcupco/FASTAPICakes/blob/main/test_main.py

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
see :
https://github.com/goldcupco/FASTAPICakes/blob/main/deployment.yaml

# Kubernetes Service (service.yaml)
https://github.com/goldcupco/FASTAPICakes/blob/main/service.yaml

# Apply Kubernetes Manifests

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Access the API in Kubernetes :
kubectl get service cake-api-service

Access the API using the assigned external IP.










