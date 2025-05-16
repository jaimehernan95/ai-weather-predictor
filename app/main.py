# app/main.py
from fastapi import FastAPI
import joblib
import pandas as pd
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), 'model.joblib'))
app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de predicción del clima"}

@app.post("/predict")
def predict(humidity: float, day_of_week: int, is_rainy: int):
    df = pd.DataFrame([[humidity, day_of_week, is_rainy]], columns=['humidity', 'day_of_week', 'is_rainy'])
    prediction = model.predict(df)[0]
    return {"predicted_temp": round(prediction, 2)}