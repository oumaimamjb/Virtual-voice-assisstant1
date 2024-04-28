import pyttsx3 as p 
import speech_recognition as sr
import selenium_web as sw
import YT_audio as yt
from News import *
import randfacts
from jokes import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your voice assistant. How are you ?")



r=sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        engine.say("You said: {}".format(text))
        engine.runAndWait()
    except:
        print("Sorry, I did not get that")
        engine.say("Sorry, I did not get that")
        engine.runAndWait()


if "what" and "about" and "you" in text:
    speak("I am also good. Thanks for asking")

speak("How can I help you today?")

with sr.Microphone() as source:
    r.energy_threshold = 10800
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("What information do you need?")
    with sr.Microphone() as source:
        r.energy_threshold = 10800
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        query = r.recognize_google(audio)


    speak("Searching for {} on Wikipedia".format(query))
    print("Searching for {} on Wikipedia".format(query))
    sw.get_info(query)

elif "play" in text2:
    speak("What song do you want to play?")
    with sr.Microphone() as source:
        r.energy_threshold = 10800
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        query = r.recognize_google(audio)

    speak("Playing {} on YouTube".format(query))
    yt = sw.MusicPlayer()
    yt.play(query)
    
elif "news" in text2:
    print("Sure , Now I will read news for you")
    speak("Sure , Now I will read news for you")
    news = sw.News()
    for i in range(len(articles)):
        print(articles[i])
        speak(articles[i])


elif "fact" in text2:
    speak("Sure ,Here is a random fact for you")
    fact = randfacts.getFact()
    print(fact)
    speak("did you know that, " + fact)

elif "joke" in text2:
    speak("Sure , get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

else:
    speak("Sorry, I did not get that")



    

        
    
