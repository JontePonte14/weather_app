def get_temp(weather_info):
    temp = {
            "temp": weather_info['main']['temp'],                 # Current temperature (°C if units=metric)
            "feels_like": weather_info['main']['feels_like'],     # Feels like temperature
            "temp_min": weather_info['main']['temp_min'],         # Min temp (in current conditions)
            "temp_max": weather_info['main']['temp_max'],         # Max temp
            "pressure": weather_info['main']['pressure'],         # Atmospheric pressure (hPa)
            "humidity": weather_info['main']['humidity']          # Humidity (%)
    }
    return temp

def get_description(weather_info):
    return weather_info['weather'][0]['description'] # More detail (e.g., "light rain")

def get_wind_info(weather_info):
    wind_info = {
        "speed": weather_info['wind']['speed'],            # Wind speed (meter/sec or km/h if units=metric)
        "direction": weather_info['wind']['deg'],              # Wind direction (degrees)
        "gust": weather_info['wind'].get('gust')          # Optional: gust speed
    }
    return wind_info

def get_clouds(weather_info):
    return weather_info['clouds']['all']            # Cloudiness (%)

def get_downfall(weather_info):
    downfall_info = {
        "rain_1h": weather_info.get('rain', {}).get('1h'),
        "rain_3h": weather_info.get('rain', {}).get('3h'),
        "snow_1h": weather_info.get('snow', {}).get('1h'),
        "snow_3h": weather_info.get('snow', {}).get('3h')
    }
    return downfall_info

# Print functions

def print_all_weather_info(weather_info):
    pass

def print_short_summary(weather_info):
    if weather_info:
        print(f"City: {weather_info['name']}")
        print(f"Temperature: {weather_info['main']['temp']} C degrees")
        print(f"Description: {weather_info['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {weather_info['wind']['speed']} m/s")
    else:
        print("Failed, please try again later")

def print_temp(weather_info):
    pass

def print_downfall(weather_info):
    pass

