import pytest
import requests
from dotenv import load_dotenv
import os


load_dotenv()

BASE_URL = os.getenv('BASE_URL')


def test_create_user():
    payload = {
        "username": "teste_de_usuario3",
        "password": "123senha"
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json


def test_login_user():
    payload = {
        "username": "teste_de_usuario3",
        "password": "123senha"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json


def test_create_meal():
    payload = {
        "title": "Minha refeição",
        "description": "Uma refeição muito deliciosa",
        "in_diet": 1,
    }
    response = requests.post(f"{BASE_URL}/meals", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

