import requests

API_key = "fd9e57c5e47a438296a6f5251dc3bb92"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Fetch the weather info for the giving city
# Input: string name of city
# Output: json with info / or None if fail
def get_weather_data(cityName):
    url = f"{base_url}?q={cityName}&appid={API_key}&units=metric"
    response = requests.get(url)

    if (response.status_code == 200):
        print(f"Success!")
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    return None