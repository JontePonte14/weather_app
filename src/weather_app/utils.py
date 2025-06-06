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
