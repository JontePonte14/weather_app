import tkinter as tk
from weather_app.api import get_weather_data
from weather_app.utils import *

state = {
    "weather_data": None,
    "text_general": None,
    "text_info" : None
              }

def start_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("900x400")
    entries = insert_data_boxes(root)
    buttons(root, entries)

    # Creates text boxes and stores them globally so they
    # can be editet with other functions
    text_general = tk.Text(root, height=4, width=22)
    text_general.grid(row=2, column=3, rowspan=4, columnspan=1)
    text_info = tk.Text(root, height=10, width=40)
    text_info.grid(row=9, column=4, rowspan=5)
    state["text_general"] = text_general
    state["text_info"] = text_info

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
                           command=lambda: handle_city_search(entries["city"], root), width=20)
    buttonCity.grid(row = 7, column = 0)

    buttonCord = tk.Button(root, text="Find weather for coordinates", 
                           command=lambda: handle_coords_search(entries["lat"], 
                                                                entries["lon"], root),width=20)
    buttonCord.grid(row = 8, column = 0)
    # Buttons to change what information to display
    r = 9
    c = 3
    buttonSummary = tk.Button(root, text="Short summary", width=20, 
                           command=lambda: view_short_summary(state["weather_data"], root))
    buttonSummary.grid(row=r, column=c)

    buttonTemp = tk.Button(root, text='Temperature', width=20, 
                           command=lambda: view_temp(state["weather_data"], root))
    buttonTemp.grid(row=r+1, column=c)

    buttonWind = tk.Button(root, text='Wind', width=20, 
                           command=lambda: view_wind(state["weather_data"], root))
    buttonWind.grid(row=r+2, column=c)

    buttonDownfall = tk.Button(root, text='Downfall', width=20, 
                           command=lambda: view_downfall(state["weather_data"], root))
    buttonDownfall.grid(row=r+3, column=c)

    buttonClearText = tk.Button(root, text="Clear text", width=20,
                            command=lambda: info_display(root, None, "clear"))
    buttonClearText.grid(row=r+4, column=c)


def handle_city_search(city_entry, root):
    city = city_entry.get()
    if not city:
        print("Error: No city entered")
        return
    print(f"Printing weather info for: {city}")
    weather_info = get_weather_data(city)
    if (weather_info):
        view_short_summary(weather_info, root)
        state["weather_data"] = weather_info
    else:
        print(f"Error: No weather data found")
    


def handle_coords_search(lat_entry, lon_entry, root):
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
        view_short_summary(weather_info, root)
        state["weather_data"] = weather_info
    else:
        print(f"Error: No weather data found")

def view_short_summary(weather_info, root):
    if (weather_info):
        # Should also draw icon, since this will be called everytime for a new
        # function

        print(f"Printing out short summary:")
        info_display(root, get_short_summary(weather_info), "summary")
        print_short_summary(weather_info)
    else:
        print(f"Error: No weather data found")

def view_temp(weather_info, root):
    if (weather_info):
        print(f"Printing temperature info: ")
        info_display(root, get_temp(weather_info), "temp")
        print_temp(weather_info)
    else:
        print(f"Error: No weather data found")

def view_wind(weather_info, root):
    if (weather_info):
        print(f"Printing wind info: ")
        info_display(root, get_wind_info(weather_info), "wind")
        print_wind_info(weather_info)
    else:
        print(f"Error: No weather data found")

def view_downfall(weather_info, root):
    if (weather_info):
        print(f"Printing downfall info: ")
        info_display(root, get_downfall(weather_info), "downfall")
        print_downfall(weather_info)
    else:
        print(f"Error: No weather data found")

def info_display(root, info, option):
    text_general = tk.Text(root, height=50, width=40)
    text_info = tk.Text(root, height=50, width=40)

    if (option == "clear"):
        print("Clearing text boxes")
        ## clear text and returns
        state["text_general"].delete("1.0", tk.END)
        state["text_info"].delete("1.0", tk.END)
        return
    # Rest of the options 
    if (state["weather_data"]):
        general_info = get_general_info(state["weather_data"])

        # Draw the following always. Country, city and coordinates
        state["text_general"].insert(tk.END, f"Country: {general_info['country']} \n")
        state["text_general"].insert(tk.END, f"City: {general_info['city']} \n")
        state["text_general"].insert(tk.END, f"Latitude: {general_info['latitude']} \n")
        state["text_general"].insert(tk.END, f"Longitude: {general_info['longitude']} \n")

        if (option == "summary"):
            return
        elif (option == "temp"):
            return
        elif (option == "wind"):
            return
        elif (option == "downfall"):
            return
        else:
            print(f'Error: No valid option')
            return 
    else:
        print(f"Error: No weather data found")

def error_messeage(root):
    pass

def update_text(root):
    pass

