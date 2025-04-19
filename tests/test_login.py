import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_no_login(client):
    rv = client.get('/')
    assert b"You are not logged in" in rv.data

def test_register_and_login(client):
    # Register
    client.post('/register', data={'username': 'admin', 'password': 'pass'})
    # Login
    rv = client.post('/login', data={'username': 'admin', 'password': 'pass'}, follow_redirects=True)
    assert b"Welcome, admin!" in rv.data

