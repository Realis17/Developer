import tkinter as tk
import requests

api_key = "gdxcj1LCOk7ZiA5sbZdybsluArTqwpeC"

def get_weather(api_key, city):
    base_url = "http://dataservice.accuweather.com"
    
    # Search for the location key of the city
    location_url = f"{base_url}/locations/v1/cities/search"
    location_params = {"apikey": api_key, "q": city}
    location_response = requests.get(location_url, params=location_params)
    location_data = location_response.json()
    
    if location_data:
        location_key = location_data[0]["Key"]
        
        # Get current conditions using location key
        current_conditions_url = f"{base_url}/currentconditions/v1/{location_key}"
        current_conditions_params = {"apikey": api_key}
        current_conditions_response = requests.get(current_conditions_url, params=current_conditions_params)
        current_conditions_data = current_conditions_response.json()
        
        return location_data[0], current_conditions_data[0]
    
    else:
        return None, None


def show_weather():
    city = city_entry.get()
    location_data, weather_data = get_weather(api_key, city)
    if location_data and weather_data:
        temperature = weather_data["Temperature"]["Metric"]["Value"]
        weather_text = weather_data["WeatherText"]
        ftemp = temperature*1.8 + 32
        result_label.config(text=f"Weather in {city}: {weather_text}, Temperature: {temperature}°C,\n Temperature in F: {ftemp}°F")

    else:
        result_label.config(text="City not found.")


# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create widgets
city_label = tk.Label(window, text="Enter city name:")
city_entry = tk.Entry(window)
get_weather_button = tk.Button(window, text="Get Weather", command=show_weather)
result_label = tk.Label(window, text="")

# Arrange widgets using grid layout
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()
