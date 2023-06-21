import requests
import json
from body.speak import speak
# API endpoint and API key
endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "1be737aa91bc5e80430e62bea9db39a4"

# location
city = "Satna"

# send GET request to API endpoint
response = requests.get(endpoint, params={"q": city, "appid": api_key})

# parse JSON response
def rain():
    data = json.loads(response.text)

    # check if it will rain today
    rain = False
    for forecast in data["list"]:
        if "12:00:00" in forecast["dt_txt"]:
            if "rain" in forecast:
                if forecast["rain"]["3h"] > 0:
                    rain = True
                    break

    # print forecast
    if rain:
        print("It will rain today In your location ")
        speak("It will rain today In your location ")
    else:
        print("It will not rain today In your location ")
        speak("It will not rain today In your location ")

