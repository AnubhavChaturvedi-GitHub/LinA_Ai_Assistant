import os
import pywhatkit
from body.listen import Listen
from body.speak import speak
def playMusic_on_youtube():
    speak("Tell Me The NamE oF The Song!")
    musicName = Listen().lower()

    if 'akeli' in musicName:
        os.startfile('E:\\Songs\\akeli.mp3')

    elif 'blanko' in musicName:
        os.startfile('E:\\Songs\\blanko.mp3')

    else:
        pywhatkit.playonyt(musicName)

    speak("Your Song Has Been Started! , Enjoy Sir!")