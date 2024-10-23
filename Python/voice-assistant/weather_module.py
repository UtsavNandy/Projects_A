# weather_module.py
import requests

def get_weather(city):
    api_key = '497382a3de1aac03f9d314684c7d5157'  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"The temperature in {city} is {temperature}°C with {description}."
    else:
        return "City not found."
