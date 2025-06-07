from utils import *
from api import *
from gui import *


def main():
    testCity()
    testLongiLat()


def testLongiLat():
    # Test for lat and longi
    print("Hello! Insert below what latitude and longitude you want weather info on")
    # 59.33, 18.07 for stockholm
    print("Latitude: ")
    lati = input()
    print("Longitude: ")
    longi = input()
    print("Fetching...")
    weather_info = get_weather_data(latitude=lati, longitude=longi)

    print("")
    print_short_summary(weather_info)

def testCity():
    # Test for city
    print("Hello! Insert below what city you want weather info on")
    cityName = input()
    print("Fetching...")
    weather_info = get_weather_data(cityName=cityName)

    print("")
    print_short_summary(weather_info)
    print("")

if __name__ == "__main__":
    main()

