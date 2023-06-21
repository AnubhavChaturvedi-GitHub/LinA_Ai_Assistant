from datetime import datetime
from body.speak import speak

def say_time():
    now = datetime.now()

    # Format the current time as a string
    time_string = now.strftime("the time is : %I:%M %p ")

    # Print the current time
    print(time_string)

    speak(time_string)

