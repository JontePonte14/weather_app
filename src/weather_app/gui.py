import tkinter as tk

def start_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("600x300")
    insert_data_boxes(root)

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

def buttons(root):
    pass

def info_display(root):
    pass

def error_messeage(root):
    pass

def update_text(root):
    pass

