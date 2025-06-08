import tkinter as tk
from weather_app.api import get_weather_data
from weather_app.utils import *

def start_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("600x300")
    entries = insert_data_boxes(root)
    buttons(root, entries)

    root.mainloop()

def insert_data_boxes(root):
    tk.Label(root, text = 'Weather Finder').grid(row = 0, column= 3)
    tk.Label(root, text = '').grid(row = 1)
    
    tk.Label(root, text='Enter City').grid(row = 2)
    tk.Label(root, text='Enter Latitude').grid(row = 4)
    tk.Label(root, text='Enter Longitude').grid(row = 5)
    eCity = tk.Entry(root)
    eLatitude = tk.Entry(root)
    eLongitude = tk.Entry(root)
    eCity.grid(row=2, column = 2)
    eLatitude.grid(row=4, column = 2)
    eLongitude.grid(row=5, column = 2)

    return {
        "city" : eCity,
        "lat" : eLatitude,
        "lon" : eLongitude
    }

def buttons(root, entries):
    # Buttons for checking city or coords weather
    buttonCity = tk.Button(root, text="Find weather for city", 
                           command=lambda: handle_city_search(entries["city"])).grid(row = 6, column = 0 )
    buttonCord = tk.Button(root, text="Find weather for coordinates", 
                           command=lambda: handle_coords_search(entries["lat"], 
                                                                entries["lon"])).grid(row = 7, column = 0)
    # Buttons to change what information to display
    buttonSummary = tk.Button(root, text="Short summary")
    buttonSummary.grid(row=4, column=2)

    buttonTemp = tk.Button(root, text='Temperature')
    buttonTemp.grid(row=5, column=2)

    buttonWind = tk.Button(root, text='Wind')
    buttonWind.grid(row=6, column=2)

    buttonCloud = tk.Button(root, text='Cloud')
    buttonCloud.grid(row=7, column=2)

def handle_city_search(city_entry):
    city = city_entry.get()
    if not city:
        print("Error: No city entered")
        return
    print(f"Printing weather info for: {city}")
    weather_info = get_weather_data(city)
    if (weather_info):
        print_short_summary(weather_info)
    else:
        print(f"Error: No weather data found")
    


def handle_coords_search(lat_entry, lon_entry):
    try:
        lat = float(lat_entry.get())
        lon = float(lon_entry.get())
    except ValueError:
        print("Error: Latitude and Longitude must be valid numbers.")
        return
    
    if not -90 <= lat <= 90 and -180 <= lon <= 180:
        print("Error: Invalid range for latitude and/or longitude")
        return
    
    print(f'Printing weather info for lat: {lat}, lon: {lon}')
    weather_info = get_weather_data(latitude=lat, longitude=lon)
    if (weather_info):
        print_short_summary(weather_info)
    else:
        print(f"Error: No weather data found")
    pass


def info_display(root):
    pass

def error_messeage(root):
    pass

def update_text(root):
    pass

