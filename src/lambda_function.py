import logging
import os
from dotenv import load_dotenv


logging_level = os.environ.get("logging-level", "INFO")

logging.basicConfig(level = logging._nameToLevel.get(logging_level))
log = logging.getLogger()

def get_weather(api_key, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"q": city, "appid": api_key, "units": "metric"}
    headers = {"content-type": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        return None

def lambda_handler(event=None, context=None):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    cities = ["Manchester", "London", "Edinburgh"]
    weather_data = {}
    for city in cities:
        data = get_weather(api_key, city)
        if data:
            weather_data[city] = data
        else:
            weather_data[city] = "City not found or an error occurred."
    return weather_data

if __name__ == '__main__':
    log.info(lambda_handler(None, None))