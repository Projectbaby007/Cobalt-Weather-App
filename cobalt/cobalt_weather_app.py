#usr/bin/bash

# import required modules
import tkinter as tk
import request
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# function to search weather for a city
def search():
    city = city_entry.get()
    result =getWeather(city)
    if result is None:
    return

#function to get weather info from OpenWeatherMap
def get_weather(city)
    API_key = ""
    url = f""
    res = request.geturl()
    if res.status_code == 404:
        messagebox.showerror("")

root = ttkbootstrap.Window(themename="morph")
root.title("Cobalt Weather App")
root.geometry("400x400")

# entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Chalkboard, 18")
city_entry.pack(pady=10)

# button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=20)

# label widget -> to show the city/country name
location_label = tk.Label(root, font="Chalkboard, 25")
location_label.pack(pady=20)

# label widget -> to show the weather icon
icon_label= tk.Label(root)
icon_label.pack()

# label widget -> to show the temperature
temperature_label = tk.Label(root, font="Chalkboard, 20")
temperature_label.pack()

#label widget -> to show the weather description
description_label = tk.Label(root, font="Chalkboard, 20")