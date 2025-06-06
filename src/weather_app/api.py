import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("OPENWEATHER_API_KEY")

#API_key = "fd9e57c5e47a438296a6f5251dc3bb92"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Fetch the weather info for the giving city
# Input: string name of city
# Output: json with info / or None if fail
def get_weather_data(cityName=None, latitude=None, longitude=None):
    if (cityName):
        url = f"{base_url}?q={cityName}&appid={API_key}&units=metric"
    elif(longitude is not None and latitude is not None):
        url = f"{base_url}?lon={longitude}&lat={latitude}&appid={API_key}&units=metric"
    else:
        raise ValueError("You must provide either a city name or both longitude and latitude.")
    
    response = requests.get(url)

    if (response.status_code == 200):
        print(f"Success!")
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    return None