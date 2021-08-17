import pyttsx3
import speech_recognition as sr

ears = sr.Recognizer()
mouth = pyttsx3.init()
voices = mouth.getProperty('voices')


def set_voice(voice):
    mouth.setProperty('voice', voice.id)

def speak(text):
    mouth.say(text)
    mouth.runAndWait()

try:
    with sr.Microphone() as source:
        speech = ears.listen(source)
        cmd = ears.recognize_google(speech).lower()
        if "baymax" in cmd:
            print("S")
except:
    pass
