import requests

url = "http://127.0.0.1:8000/predict"

params = {
    "humidity": 60.0,
    "day_of_week": 2,
    "is_rainy": 1
}

response = requests.post(url, params=params)

if response.status_code == 200:
    print("Prediction response:", response.json())
else:
    print(f"Failed to get prediction. Status code: {response.status_code}")
    print("Response:", response.text)
