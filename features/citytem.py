import requests
import json
from body.speak import speak

# API endpoint and API key
endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = ""

# location
def temcity():
    city = "Satna"

    # send GET request to API endpoint
    response = requests.get(endpoint, params={"q": city, "appid": api_key})

    # parse JSON response
    data = json.loads(response.text)

    # print current temperature
    print("Temperature in " + city + ": " + str(data["main"]["temp"]) + "°F")
    speak("Temperature in " + city + ": " + str(data["main"]["temp"]) + "°F")
