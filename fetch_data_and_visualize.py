# -*- coding: utf-8 -*-
"""Fetch_Data_and_Visualize.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aN1VcJjMkm8EzdDaKkZhALfMkV42otTW
"""

# Import necessary libraries
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set up API details
API_KEY = '11feb1841571d0822157e2dfff44fd73'  #API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# List of major Indian states .
INDIAN_STATES = [
    'Delhi, IN', 'Mumbai, IN', 'Kolkata, IN', 'Chennai, IN',
    'Bangalore, IN', 'Hyderabad, IN', 'Pune, IN', 'Jaipur, IN',
    'Lucknow, IN', 'Patna, IN'
]

#function to fetch weather data for a given city
def fetch_weather_data(city):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None  # Return None if the request fails

# Fetch weather data for all Indian states
weather_data = []
for state in INDIAN_STATES:
    data = fetch_weather_data(state)
    if data:
        weather_data.append({
            'State': state.split(',')[0],  # Extract state name
            'Temperature': data['main']['temp'],  # Current temperature in Celsius
            'Humidity': data['main']['humidity']  # Humidity in percentage
        })

# check if not  data fetching was successful
if not weather_data:
    print("No data fetched. Please check the API key or network connection.")
    exit()

# Extract data for plotting
states = [item['State'] for item in weather_data]
temperatures = [item['Temperature'] for item in weather_data]
humidity = [item['Humidity'] for item in weather_data]

# Set the visual style
sns.set(style="whitegrid")

# Plotting temperature data
plt.figure(figsize=(10, 6))
sns.barplot(x=states, y=temperatures, palette="Blues_d")
plt.title('State-wise Temperature in India (°C)', fontsize=16)
plt.xlabel('State', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("indian_states_temperature_plot.png")  # Save the temperature plot
plt.show()

# Plotting humidity data
plt.figure(figsize=(10, 6))
sns.barplot(x=states, y=humidity, palette="Greens_d")
plt.title('State-wise Humidity in India (%)', fontsize=16)
plt.xlabel('State', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("indian_states_humidity_plot.png")  # Save the humidity plot
plt.show()