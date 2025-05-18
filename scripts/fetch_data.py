# scripts/fetch_data.py
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

API_KEY = os.getenv('WEATHER_API_KEY')
CITY = 'Toronto'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()
    df = pd.DataFrame([{
        'datetime': datetime.now(),
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['main']
    }])
    df.to_csv('data/weather.csv', index=False)
    print("Datos guardados en weather.csv")

if __name__ == "__main__":
    fetch_weather()
# Add to fetch_data.py temporarily for quick testing
for _ in range(10):  # simulate 10 data points
    fetch_weather()
    time.sleep(2)  # wait 2 seconds between fetches
