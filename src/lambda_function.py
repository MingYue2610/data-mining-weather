import os
import requests
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")  # Replace with your actual OpenWeatherMap API key
DATABASE_URL = os.getenv("DATABASE_URL")  # Replace with your ElephantSQL database URL

def get_weather(api_key, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"q": city, "appid": api_key, "units": "metric"}

    headers = {
        "content-type": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        return None

def store_weather_data(weather_data):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city VARCHAR(50),
            temperature FLOAT,
            weather VARCHAR(50),
            timestamp TIMESTAMP
        )
    """)
    cursor.execute("""
        INSERT INTO weather (city, temperature, weather, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (weather_data['name'], weather_data['main']['temp'], weather_data['weather'][0]['description'], datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    cities = ["Manchester", "London", "Edinburgh"]
    for city in cities:
        weather_data = get_weather(API_KEY, city)
        if weather_data:
            print(f"{city}: {weather_data}")
            store_weather_data(weather_data)
        else:
            print(f"City {city} not found or an error occurred.")

if __name__ == "__main__":
    main()