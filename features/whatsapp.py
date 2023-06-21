from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from body.speak import speak
import pathlib
from body.listen import Listen

scriptDirectory = pathlib.Path().absolute()






def WhatsappSender(Name):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
    os.environ["WDM_LOG_LEVEL"] = "0"
    PathofDriver = "DataBase\\chromedriver.exe"
    driver = webdriver.Chrome(PathofDriver, options=options)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    speak("Initializing The Whatsapp Software.")

    ListWeb = {'dhruv': "+917011024588",
               'dost': "+91",
               "papa": '+918226098666'}
    speak(f"Preparing To Send a Message To {Name}")
    speak("What's The Message By The Way?")
    Message = Listen()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(10)
    try:
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        speak("Message Sent")
    except Exception as e:
        print(f"An error occurred: {e}")
    driver.quit()

