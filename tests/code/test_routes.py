import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_samu_post(client):
    """Test successfull call through route"""

    rv = client.post('/v1/samu', json="aa ii aa oo")
    assert b'ii aa oo aa' in rv.data

def test_empty_samu_post(client):
    """Test empty call through route"""

    rv = client.post('/v1/samu')
    assert b'Payload missing' in rv.data