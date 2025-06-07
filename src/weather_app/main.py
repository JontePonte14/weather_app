from utils import *
from api import *
from gui import *


def main():
    print("Hello! Insert below what city you want weather info on")
    cityName = input()
    print("Fetching...")
    weather_info = get_weather_data(cityName)

    print("")
    if weather_info:
        print(f"City: {weather_info['name']}")
        print(f"Temperature: {weather_info['main']['temp']} C degrees")
        print(f"Description: {weather_info['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {weather_info['wind']['speed']} m/s")
    else:
        print("Failed, please try again later")
    # 1. Get input (e.g. a city name)
    # 2. Fetch weather data via your API function
    # 3. Use utility functions to extract what you want
    # 4. Print it nicely



if __name__ == "__main__":
    main()

