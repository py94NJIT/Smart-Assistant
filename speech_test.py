
import speech_recognition as sr
import pyttsx3
import requests
from datetime import date
from dotenv import find_dotenv, load_dotenv
import os 

# Load environment key & host from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
db_host = os.getenv('DB_HOST')

# Initialize recognizer class (for recognizing speech)
r= sr.Recognizer()

# Initialize TTS engine
engine = pyttsx3.init()


# Weather Date for current date YYYY-MM-DD
weather_date = date.today()

# Weather API Url Format after timeline/location/date/key
weather_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/08902/{weather_date}?key={API_KEY}"

# Initialize requests
response = requests.get(weather_url)
weather_data = response.json()
print(response.status_code)

#Speak
def speak(text):
    print (f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

#Listen
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        #Optional: Adjust for ambient noise 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Time over, Thanks.")

        try:
            print("Text: " + r.recognize_google(audio))
            text= r.recognize_google(audio)
            
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I could not understand audio.")
            return ""
        except sr.RequestError:
            speak(f"Could not request results from speech recognition service;")
            return ""
        
#Processing User commands, and responding appropriately
def process_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif "quit" in command:
        speak("Goodbye!")
        return True
    elif "weather" in command:
        # Location based on current user location
        #day is for today's date
        day = weather_data['days'][0]
        
        print(f"Date: {day['datetime']}, High: {day['tempmax']}, Temp Min: {day['tempmin']}")
        speak(f"The current weather for {weather_data['address']} is {day['temp']} degrees and is {day['conditions']} with a high of {day['tempmax']} and a low of {day['tempmin']}")
    else:
        speak("I'm sorry, I don't know how to do that yet.")
    return False

if __name__== "__main__":
    speak("Hello, how can I help you?")
    while True:
        command = listen()
        if command:
                if process_command(command):
                    break
    '''            
    with sr.Microphone() as source:
        print("Talk")
        audio_text= r.listen(source)
        text=r.recognize_google(audio_text)
        print("Time over, Thanks.")

        try:
            print("Text: " + r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
    

    if ("hello" in text):
        speak("Hello, how can I help you?")
    '''
