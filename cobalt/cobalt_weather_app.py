
# import required modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

#function to get weather info from OpenWeatherMap
def get_weather(city):
    API_key = "cf8b0987cb1ddffbfc1cffb34fec78cc"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.geturl()

    if res.status_code == 404:
        messagebox.showerror("Error, City not found")
        return None

    # parse the response JSON to get weather info
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # get the icon url and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # if city is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # get the weather icon image from the url and update the icon label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    #update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature: .2f}℃")
    description_label.configure(text=f"Description: {description}")

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
description_label.pack()

root.mainloop()