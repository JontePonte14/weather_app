import requests

#API_key = "fd9e57c5e47a438296a6f5251dc3bb92"
base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(cityName):
    city_url = cityName
    url = f"{base_url}?q={cityName}&appid={API_key}&units=metric"
    response = requests.get(url)

    if (response.status_code == 200):
        print(f"Success!")
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

weather_city = "Stockholm"
weather_info = get_weather_data(weather_city)

if weather_info:
    print(f"City: {weather_info['name']}")
    print(f"Temperature: {weather_info['main']['temp']} C degrees")
    print(f"Description: {weather_info['weather'][0]['description'].capitalize()}")
    print(f"Wind speed: {weather_info['wind']['speed']} m/s")