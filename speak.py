import pyttsx3
import datetime
import wikipedia
import sys
import webbrowser
import os
import pyjokes
import random
import pyautogui
import wolframalpha
import speech_recognition as sr
from password import Pass

app = wolframalpha.Client("5X2G99-Y4JYP73JJK")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis, please tell me how may I help you")


def tell_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    speak("Today is " + day_dict[day])


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


if __name__ == '__main__':
    speak("This particular device is password protected")
    passs = input("Enter the password:")
    Pass(passs)  # Call the Pass function from password module
    wishme()
    tell_day()
    while True:
        query = take_command()

        if 'wikipedia' in query.lower():
            speak('Sure')
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            speak("Sir, do you have any other work for me?")
        elif "open google" in query.lower():
            speak("sir, what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")
        elif 'open youtube' in query.lower():
            speak("sure")
            webbrowser.open("www.youtube.com")
            speak("here is your youtube")
        elif 'open spotify' in query.lower():
            speak("sure")
            webbrowser.open("www.spotify.com")
            speak("here is your spotify")
        elif 'open facebook' in query.lower():
            speak("sure")
            webbrowser.open("www.facebook.com")
            speak("here is your facebook")
        elif 'open whatsapp' in query.lower():
            speak("sure")
            webbrowser.open("www.whatsapp.com")
            speak("here is your whatsapp")
        elif 'open chatgpt' in query.lower():
            speak("sure")
            webbrowser.open("www.chatgpt.com")
            speak("here is your chatgpt")
        elif 'open notepad' in query.lower():
            speak("sure")
            apath = "C:/Users/ASUS/Downloads/notepad2.txt"
            os.startfile(apath)
            speak("here is your notepad")
        elif 'open cmd' in query.lower():
            speak("sure")
            os.system("start cmd")
            speak("here is your cmd")
        elif "play music" in query.lower():
            speak("sure")
            music_dir = "C:/Users/ASUS/Music/New folder"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("okay, here is your music sir! enjoy!")
        elif "play my favourite music on youtube" in query.lower():
            speak("sure")
            webbrowser.open("https://youtu.be/vgm1u2gPxzw?si=LmpVdflbnXeKJqz5")
            speak("here is your favourite song sir!")
        elif "tell me a joke" in query.lower():
            jokes = pyjokes.get_joke()
            speak(jokes)
        elif "tell me time" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
        elif "calculate" in query.lower():
            speak("what should i calculate ,sir!")
            query = input(":enter the query")
            res = app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text)
            speak("this is your required answer sir")
        elif "open whatsapp" in query.lower():
            speak('sure')
            pyautogui.click(x=1406, y=29)

        elif "hello jarvis" in query.lower():
            speak("hi sir, how are you?")
        elif "good" in query.lower():
            speak("thank you sir")
        elif "who made you" in query.lower():
            speak("i have been created by Mr Sainath, Mr Sainath is my god")
        elif"new tab" in query.lower():
            pyautogui.hotkey('ctrl','t')
            speak("hear is your new tab sir")
        elif "minimise the window" in query.lower():
            pyautogui.hotkey('win', 'd')
            speak("window minimized successfully")
        elif"volume up" in query.lower():
            pyautogui.hotkey("volumeup")
            speak("volume up successfully")
        elif "volume down" in query.lower():
            pyautogui.hotkey("volumedown")
            speak("volume down successfully")
        elif "volume mute" in query.lower():
            pyautogui.hotkey("volumemute")
            speak("volume mute successfully")
        elif("restart the system") in query.lower():
            os.system("shutdown /r /t 0")
        elif("shutdown the system") in query.lower():
            os.system("shutdown /s /t 0")


        elif 'goodbye' in query:
            speak("Thank you, sir. Have a nice day.")
            sys.exit()