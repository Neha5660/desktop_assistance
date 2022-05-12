#import numpy
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
        speak('Good Morning')
    elif hour>=12 and hour <=18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am jarvis. How can I help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('recognise')
            query = r.recognize_google(audio,language ="en-in")
            print(f"User said:{query}\n")
        except Exception as e:
            print(e)
            print('say that again')
            return "None"
        return query

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia .......')
            #query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'youtube' in query:
            query = query.replace('youtube','')
            webbrowser.open('https://www.youtube.com/results?search_query='+ query +'')

        elif 'google' in query:
            query = query.replace('google','')
            webbrowser.open('https://www.google.com/search?q=' + query +'')

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is {time}")

        elif 'very slow' in query:
            speak('Its not my fault. Your Internet connection is poor')

