import requests
import json


def detect_language(input_text: str) -> str:
    if all("а" <= char <= "я" or char == "ё" for char in input_text.lower() if char.isalpha()):
        return "ru-ru"
    return "en-us"


def get_weather_city(city_name: str, api_key: str) -> int | None:
    try:
        request_url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
        query = {
            'apikey': api_key,
            'q': city_name,
            'language': detect_language(city_name),
            'details': True,
            'toplevel': False,

        }
        response = requests.get(url=request_url, params=query)

        if response.status_code == 200:
            location: dict = response.json()[0]
            location_key = location.get('Key')

            return location_key
        else:
            raise f''
    except Exception as e:
        print(e ,'|',  f'{response.status_code} | {response.text}')
        return None
    

def get_weather_data(locations, api_key, days):
    all_data = {}
    for location in locations:
        location_key = get_weather_city(location, api_key)
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/{days}day/{location_key}"
        params = {
            "apikey": api_key,
            "metric": True,
            "details": True,
            }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_data[location] = data
        else:
            raise Exception(f"API Error for {location}: {response.status_code}")
    return all_data