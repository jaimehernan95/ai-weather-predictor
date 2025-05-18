# scripts/train_model.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Load the dataset
df = pd.read_csv('data/weather.csv')

# Preprocessing
df['datetime'] = pd.to_datetime(df['datetime'])
df['day_of_week'] = df['datetime'].dt.dayofweek  # 0=Monday, 6=Sunday
df['is_rainy'] = df['weather'].apply(lambda w: 1 if 'Rain' in w else 0)

# Features and label
X = df[['humidity', 'day_of_week', 'is_rainy']]
y = df['temp']

# Model pipeline
model = Pipeline([
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X, y)

# Save the model
model_path = os.path.join('app', 'model.joblib')
joblib.dump(model, model_path)

print(f"✅ Model trained and saved to {model_path}")
