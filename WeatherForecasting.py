import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '199387ea730db7cbc0736a468ffcd424'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Define the parameters for the API request
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    # Send a GET request to the API
    response = requests.get(BASE_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and display weather information
        city_name = data['name']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f"City: {city_name}")
        print(f"Weather: {weather_description.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error: Unable to fetch weather data")

# Ask the user for a city name
city = input("Enter city name: ")
get_weather(city)
