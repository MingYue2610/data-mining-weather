import requests
import os
import logging
from dotenv import load_dotenv

log = logging.getLogger()


def get_weather(api_key, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"q": city, "appid": api_key, "units": "metric"}

    headers = {
        "content-type": "application/json"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()

    else:
        print(response.json())
        return None


def get(endpoint, params={}) -> requests.Response:
        r = requests.get(endpoint, params)
        log.info("Request url: %s", r.request.url)
        log.info("Response status code: %s", r.status_code)
        return r


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")  # Replace with your actual OpenWeatherMap API key
    cities = ["Manchester", "London", "Edinburgh"]
    for city in cities:

        weather_data = get_weather(api_key, city)
        if weather_data:
            print(city + ":" + str(weather_data))

        else:
            print("City not found or an error occurred.")


if __name__ == "__main__":
    main()
