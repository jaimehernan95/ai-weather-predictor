from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(title="Weather Temperature Predictor")

# Load the trained model
# The model was saved in train_model.py using joblib
model = joblib.load("app/model.joblib")

# Define input data schema using Pydantic
# This ensures input validation and generates docs automatically
class WeatherInput(BaseModel):
    humidity: float              # Humidity percentage (e.g., 60.5)
    day_of_week: int             # Day of the week as a number: Monday = 0, Sunday = 6
    is_rainy: int                # 1 if it's raining, 0 otherwise

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather Predictor API!"}

# Define the prediction endpoint
@app.post("/predict")
def predict_temperature(data: WeatherInput):
    """
    Predict the temperature based on humidity, day of the week, and weather condition.
    """
    # Prepare the input data for the model
    # It must be in the same format and order as during training
    features = np.array([[data.humidity, data.day_of_week, data.is_rainy]])

    # Predict using the trained model
    prediction = model.predict(features)[0]

    # Return the prediction result
    return {
        "predicted_temperature": round(prediction, 2),
        "inputs": data.dict()
    }