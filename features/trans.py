import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium
import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.5
        r.non_speaking_duration = 1.5
        audio_text = r.listen(source, 0, 8)
    try:
        print('Recognizing...')
        text = r.recognize_google(audio_text, language='hi')
        print('Converting audio transcripts into text...')
        # print(text)
        return text
    except Exception as e:
        print("An error occurred:", e)
        return ""


def trans(text):
    lang_code = 'en '
    input1 = text
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://translate.google.co.in/?sl=auto&tl=" + lang_code + "&text=" + input1 + "&op=translate")
    time.sleep(2)
    output1 = browser.find_element(By.CLASS_NAME, 'HwtZe').text
    print(output1)

# trans("कोरोनवायरस संबंधित वायरस का एक समूह है जो स्तनधारियों और पक्षियों में बीमारियों का कारण बनता है।")

def FinalInp():
    text = Listen()
    trans(text)



FinalInp()