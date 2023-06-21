import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

def listen_and_searchyt():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.non_speaking_duration = 1.5
        audio = r.listen(source, 0, 8)

        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
        except:
            print("Sorry, I could not understand you.")


