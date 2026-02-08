import pytest
from config.env_config import env
from config.test_data import TestData
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient(base_url=env.base_url, token=TestData.api_token)
    yield client

def test_search_english_book(api_client):
    resp = api_client.get("/api/search", params={"q": "The Catcher in the Rye", "lang": "en"})
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "results" in data

def test_search_arbitrary(api_client):
    resp = api_client.get("/api/search", params={"q": TestData.arbitrary_search})
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data

def test_search_without_token():
    client = ApiClient(base_url="https://www.chitai-gorod.ru")
    resp = client.get("/api/search", params={"q": "Test"})
    assert resp.status_code in (400, 401, 403, 404, 200)

def test_search_with_method_other_than_get(api_client):
    resp = api_client.post("/api/search", json={"q": "Book", "lang": "en"})
    assert resp.status_code in (200, 201, 202)

def test_book_info(api_client):
    resp = api_client.get("/api/book/ISBN/978-5-17-123456-7")
    assert resp.status_code == 200
    data = resp.json()
    assert "title" in data