from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test__read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "wikipedia api call/search or wiki"}


def test__read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "44th president",
        ]
    }
