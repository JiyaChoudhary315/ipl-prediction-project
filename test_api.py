from fastapi.testclient import TestClient
from fastapi_app import app  # assuming your FastAPI app is in fastapi_app.py

client = TestClient(app)

def test_predict():
    response = client.get("/predict/?team1=MI&team2=CSK&venue=Mumbai")
    assert response.status_code == 200
    assert "winner" in response.json()
    assert "score_prediction" in response.json()
