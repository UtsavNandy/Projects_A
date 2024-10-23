import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "497382a3de1aac03f9d314684c7d5157"

weather_params = {
    "lat": 22.943600,
    "lon": 88.462350,
    "appid": api_key,
    "cnt" : 4,
}

response =requests.get(OWM_endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
 condtion_code = hour_data["weather"][0]["id"]
 if condtion_code < 700:
  will_rain = True

if will_rain:
 print("It will rain today")
else:
 print("It will not rain today")
