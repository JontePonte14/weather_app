def get_temp(weather_info):
    temp = [
                    weather_info['main']['temp'],             # Current temperature (°C if units=metric)
                    weather_info['main']['feels_like'],       # Feels like temperature
                    weather_info['main']['temp_min'],         # Min temp (in current conditions)
                    weather_info['main']['temp_max'],         # Max temp
                    weather_info['main']['pressure'],         # Atmospheric pressure (hPa)
                    weather_info['main']['humidity'],         # Humidity (%)
            ]
    return temp

def get_description(weather_info):
    return weather_info['weather'][0]['description'] # More detail (e.g., "light rain")

def get_wind_info(weather_info):
    wind_info = [
        weather_info['wind']['speed'],            # Wind speed (meter/sec or km/h if units=metric)
        weather_info['wind']['deg'],              # Wind direction (degrees)
        weather_info['wind'].get('gust')          # Optional: gust speed

        ]
    return wind_info

def get_clouds(weather_info):
    pass

def get_downfall(weather_info):
    pass