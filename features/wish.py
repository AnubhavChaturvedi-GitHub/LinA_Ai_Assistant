import datetime
from features.wether import rain
from features.timesay import say_time
from body.speak import speak
from features.temp import Temp
from features.citytem import temcity
from playsound import playsound
import threading



now = datetime.datetime.now()

def wish():
    if now.hour < 12:
        print("Good morning")
        speak("Good morning")
        say_time()
        Temp()
        temcity()
        rain()
        print("i am Ready  & online ! now you can ask me any question")
        speak("i am Ready  & online ! now you can ask me any question")

    elif now.hour < 18:
        print("Good afternoon sir  ")
        speak("Good afternoon sir  ")
        say_time()
        Temp()
        temcity()
        rain()
        print("! i am Ready & online ! how can i assist you")
        speak("! i am Ready & online ! how can i assist you")
    else:
        print("Good evening sir ")
        speak("Good evening sir ")
        say_time()
        Temp()
        temcity()
        rain()
        print("! i am ready & online ! how can i help you ?  ")
        speak("! i am ready & online ! how can i help you ?  ")


def play_sound():
    playsound("C:\\Users\\chatu\\OneDrive\\Desktop\\LiNa\\mp3file\\itoperf.mp3")

def Mer():
    t1 = threading.Thread(target=play_sound)
    t2 = threading.Thread(target=wish)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return "completed : INTRO"

# Mer()


