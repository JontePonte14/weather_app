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

def get_general_info(weather_info):
    general_info = {
        "description" : weather_info['weather'][0]['description'],  # More detail (e.g., "light rain")
        "country" : weather_info['sys']['country'],                 # Country
        "city" : weather_info['name']                               # City
    }
    return general_info

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

def get_short_summary(weather_info):
    short_summary = {
        "city": weather_info['name'],
        "temp": weather_info['main']['temp'],
        "description": weather_info['weather'][0]['description'].capitalize(),
        "windSpeed": weather_info['wind']['speed'],
        "clouds": weather_info['clouds']['all']
    }
    return short_summary

def missing_data(weather_info):
    if (weather_info == None):
        return True
    else:
        return False 
    
# Print functions
def print_short_summary(weather_info):
    summary = get_short_summary(weather_info)

    if summary:
        city = summary.get('city', '')
        print(f"City: {city or 'No city'}")
        print(f"Temperature: {summary.get('temp')} °C")
        print(f"Description: {summary.get('description')}")
        print(f"Wind speed: {summary.get('windSpeed')} m/s")
        print(f"Cloud coverage: {summary.get('clouds')}%")
    else:
        print("Failed, please try again later")

def print_temp(weather_info):
    summary = get_temp(weather_info)

    if summary:
        print(f"Temperature: {summary.get('temp')}")
        print(f"Feels like: {summary.get('feels_like')}")
        print(f"Min. temperature: {summary.get('temp_min')}")
        print(f"Max. temperature: {summary.get('temp_max')}")
        print(f"Pressure: {summary.get('pressure')}")
        print(f"humidity: {summary.get('humidity')}")
    else:
        print("Failed, please try again later")

def print_downfall(weather_info):
    summary = get_downfall(weather_info)

    if summary:
        print(f"Rain 1h: {summary.get('rain_1h')}")
        print(f"Rain 3h: {summary.get('rain_3h')}")
        print(f"Snow 1h: {summary.get('snow_1h')}")
        print(f"Snow 3h: {summary.get('snow_3h')}")
    else:
        print("Failed, please try again later")

def print_wind_info(weather_info):
    summary = get_wind_info(weather_info)

    if summary:
        print(f"Wind speed: {summary.get('speed')} m/s")
        print(f"Direction: {summary.get('direction')}°")
        gust = summary.get('gust')
        if gust is not None:
            print(f"Gusts: {gust} m/s")
        else:
            print("Gust data: not available")
    else:
        print("Failed to retrieve wind information.")


def print_all_weather_info(weather_info):
    if missing_data(weather_info):
        print("No weather data available.")
        return

    print("===== Weather Summary =====")
    print_short_summary(weather_info)

    print("\n--- Temperature Details ---")
    print_temp(weather_info)

    print("\n--- Wind Details ---")
    print_wind_info(weather_info)

    print("\n--- Precipitation ---")
    print_downfall(weather_info)

    print("============================\n")
