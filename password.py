import speech_recognition as sr
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        return 'none'
    query = query.lower()
    return query


def Pass(pass_inp):
    password = "jarvis"
    passss = str(pass_inp)

    if passss == password:  # Compare with the actual password
        speak("Password matched")
        speak("Welcome sir")
    else:
        speak("Password not matched")
        sys.exit()


if __name__ == "__main__":  # Fix the __name__ variable
    speak("This particular device is password protected")
    passs = input("Enter the password:")
    Pass(passs)
