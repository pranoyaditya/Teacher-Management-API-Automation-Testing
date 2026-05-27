import pytest
import random
import requests
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def login_data():
    login_payload = {
        "username": os.getenv("PROJECT_USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    return BASE_URL, login_payload


@pytest.fixture
def get_header(login_data):
    base_url, login_payload = login_data

    # Send login request and extract the auth token
    login_response = requests.post(f'{base_url}/login', json=login_payload)
    token = login_response.json().get('authToken')
    headers = {
        'Authorization': f'Bearer {token}'
    }
    return headers


@pytest.fixture
def schema_structure():
    return {
        "_id": str,
        "name": str,
        "email": str,
        "department": str,
        "teacherId": int,
        "designation": str
    }


@pytest.fixture
def new_teacher_data():
    faker = Faker()
    return {
        "name": faker.name(),
        "email": faker.email(),
        "department": random.choice(["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"]),
        "teacherId": faker.random_int(min=1000, max=99999),
        "designation": random.choice(["Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Instructor"])
    }


@pytest.fixture
def teacher_data(login_data, get_header):
    headers = get_header
    base_url, login_payload = login_data

    response = requests.get(f'{base_url}/api/teacher', headers=headers)
    teachers = response.json()

    return teachers, response.status_code
