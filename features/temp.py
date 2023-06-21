import requests
from bs4 import BeautifulSoup
from body.speak import speak
def Temp():
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    print(f"The Temperature Outside Is {temperature}")
    speak(f"The Temperature Outside Is {temperature}")



