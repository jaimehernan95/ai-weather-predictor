# scripts/transform.py
import pandas as pd

def transform():
    df = pd.read_csv('data/weather.csv')
    df['day_of_week'] = pd.to_datetime(df['datetime']).dt.dayofweek
    df['is_rainy'] = df['weather'].apply(lambda x: 1 if x.lower() in ['rain', 'drizzle'] else 0)
    df.drop(columns=['weather'], inplace=True)
    df.to_csv('data/weather_transformed.csv', index=False)
    print("Datos transformados y guardados")

if __name__ == "__main__":
    transform()