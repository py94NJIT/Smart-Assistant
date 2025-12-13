
import speech_recognition as sr
import pyttsx3


# Initialize recognizer class (for recognizing speech)
r= sr.Recognizer()

#Initialize TTS engine
engine = pyttsx3.init()

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
def process_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif "quit" in command:
        speak("Goodbye!")
        return True
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
