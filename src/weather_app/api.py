import requests

API_key = 123
base_url = f"https://api.openweathermap.org/data/2.5/weather?id="
#base_url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_key}"

def get_weather_data(cityName):
    city_url = cityName
    url = f"{base_url}{city_url}&appid={API_key}"
    responese = requests.get(url)

    if (responese.status_code == 200):
        print(f"Success!")
        weather_data = responese.json()
        return weather_data
    else:
        print(f"Failed to retrieve data. Status code: {responese.status_code}")
