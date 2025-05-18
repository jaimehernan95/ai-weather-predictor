# Import the 'requests' library to make HTTP requests
import requests

# ---------------------------------------------------------
# Step 1: Define the URL of the API endpoint
# ---------------------------------------------------------
# This is the address where your FastAPI app is running.
# If you're running locally with Uvicorn, it's usually:
# http://127.0.0.1:8000
url = "http://127.0.0.1:8000/predict"

# ---------------------------------------------------------
# Step 2: Create the input data as a dictionary
# ---------------------------------------------------------
# The keys here must match the fields defined in your Pydantic model `WeatherInput`
# You can think of this like an "example case" to send to your model
payload = {
    "humidity": 65.0,        # Humidity in percentage (e.g., 65%)
    "day_of_week": 2,        # Day of the week (0 = Monday, 6 = Sunday)
    "is_rainy": 1            # 1 means it's raining, 0 means it's not
}

# ---------------------------------------------------------
# Step 3: Make a POST request to the API
# ---------------------------------------------------------
# We use requests.post() to send our payload (input data) to the /predict endpoint
# The payload is sent as a JSON object
response = requests.post(url, json=payload)

# ---------------------------------------------------------
# Step 4: Handle the API response
# ---------------------------------------------------------
# If the status code is 200, it means the request was successful
if response.status_code == 200:
    # Print the response in JSON format
    print("✅ Prediction response:")
    print(response.json())  # This shows the predicted temperature and input data
else:
    # If something went wrong, show the error message
    print("❌ Failed to get a response from the API:")
    print("Status Code:", response.status_code)
    print("Error Message:", response.text)
