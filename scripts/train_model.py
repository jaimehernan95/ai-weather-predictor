# scripts/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train():
    df = pd.read_csv('data/weather_transformed.csv')
    X = df[['humidity', 'day_of_week', 'is_rainy']]
    y = df['temp']
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, 'app/model.joblib')
    print("Modelo entrenado y guardado")

if __name__ == "__main__":
    train()