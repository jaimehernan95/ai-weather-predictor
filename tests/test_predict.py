# tests/test_predict.py
import requests

BASE_URL = "http://127.0.0.1:8000"  # FastAPI should be running locally

def test_prediction_success():
    """
    Test that the /predict endpoint returns a valid prediction.
    """
    # Define input matching your Pydantic model
    payload = {
        "humidity": 60.0,
        "day_of_week": 3,
        "is_rainy": 0
    }

    response = requests.post(f"{BASE_URL}/predict", json=payload)

    # Assert response is successful
    assert response.status_code == 200

    # Extract data
    result = response.json()

    # Assert keys exist in response
    assert "predicted_temperature" in result
    assert isinstance(result["predicted_temperature"], float)
    assert "inputs" in result
    assert result["inputs"] == payload

def test_prediction_invalid_input():
    """
    Test that the API returns an error for invalid input (e.g., missing fields).
    """
    bad_payload = {
        "humidity": 60.0,
        # "day_of_week" is missing
        "is_rainy": 0
    }

    response = requests.post(f"{BASE_URL}/predict", json=bad_payload)
    assert response.status_code == 422  # Unprocessable Entity (validation error)
