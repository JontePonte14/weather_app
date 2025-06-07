from utils import *
from api import *
from gui import *


def main():
    print("Hello! Insert below what city you want weather info on")
    cityName = input()
    print("Fetching...")
    weather_info = get_weather_data(cityName=cityName)

    print("")
    if weather_info:
        print(f"City: {weather_info['name']}")
        print(f"Temperature: {weather_info['main']['temp']} C degrees")
        print(f"Description: {weather_info['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {weather_info['wind']['speed']} m/s")
    else:
        print("Failed, please try again later")

    print("Hello! Insert below what latitude and longitude you want weather info on")
    # 59.33, 18.07 for stockholm
    print("Latitude: ")
    lati = input()
    print("Longitude: ")
    longi = input()
    print("Fetching...")
    weather_info = get_weather_data(latitude=lati, longitude=longi)

    print("")
    if weather_info:
        print(f"City: {weather_info['name']}")
        print(f"Temperature: {weather_info['main']['temp']} C degrees")
        print(f"Description: {weather_info['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {weather_info['wind']['speed']} m/s")
    else:
        print("Failed, please try again later")


if __name__ == "__main__":
    main()

