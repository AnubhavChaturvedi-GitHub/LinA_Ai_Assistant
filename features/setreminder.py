import datetime
import time
from body.speak import speak

def set_reminder(reminder_text):
    # Get the current time
    now = datetime.datetime.now()

    # Extract the reminder time from the reminder text
    reminder_time = datetime.datetime.strptime(reminder_text.split("at ")[-1], "%I:%M %p").time()

    # Calculate the time difference between the current time and the reminder time
    time_diff = datetime.datetime.combine(now, reminder_time) - now

    # Sleep for the time difference
    time.sleep(time_diff.seconds)

    # Print the reminder message
    while True:
        speak(reminder_text)

# Example usage
# set_reminder("02:14 a.m.")