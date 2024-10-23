# assistant.py
from speech_module import speak, listen
from weather_module import get_weather
from calendar_integration import schedule_meeting
import datetime

def handle_command(command):
    if "weather" in command:
        speak("Which city?")
        city = listen()
        if city:
            weather_info = get_weather(city)
            speak(weather_info)
    elif "schedule" in command and "meeting" in command:
        speak("What is the meeting about?")
        summary = listen()
        speak("When is the meeting?")
        # For simplicity, we'll use a fixed date/time. Replace with actual parsing.
        start_time = datetime.datetime(2024, 8, 21, 10, 0)  # Example time
        schedule_meeting(summary, start_time)
    else:
        speak("Sorry, I don't know how to handle that command.")

# Run the assistant
if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            handle_command(command)


