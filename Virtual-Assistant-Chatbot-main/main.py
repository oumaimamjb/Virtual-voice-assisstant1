import pyttsx3 as p 
import speech_recognition as sr
from News import *
import randfacts
from jokes import joke
from selenium_web import *
from YT_audio import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize pyttsx3 engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user
speak("Hello, I am your voice assistant. How can I help you today?")

# Initialize the speech recognizer
r = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Begin listening for user input asynchronously
while True:
    text = recognize_speech()

    if text:
        engine.say("You said: {}".format(text))
        engine.runAndWait()

        # Respond based on user's response
        if "what" in text and "about" in text and "you" in text:
            speak("I am also good. Thanks for asking")

        elif "information" in text:
            speak("What information do you need?")
            print("Waiting for information query...")
            query = recognize_speech()
            print("You asked for information about:", query)
            speak("Searching for {} on Wikipedia".format(query))
            get_info(query)  # Perform Wikipedia search and speak the result

        elif "play" in text:
            speak("What song do you want to play?")
            print("Waiting for song query...")
            query = recognize_speech()
            print("You want to play the song:", query)
            speak("Playing {} on YouTube".format(query))
            yt = MusicPlayer()
            yt.play(query)  # Play the song on YouTube

        elif "news" in text:
            print("Sure, Now I will read news for you")
            speak("Sure, Now I will read news for you")
            news_obj = News()
            articles = news_obj.get_top_headlines()
            for article in articles:
                print(article)
                speak(article)
                
        elif "fact" in text:
            speak("Sure, Here is a random fact for you")
            fact = randfacts.getFact()
            print(fact)
            speak("Did you know that, " + fact)

        elif "joke" in text:
            speak("Sure, get ready for some chuckles")
            joke_data = joke()
            print(joke_data[0])
            speak(joke_data[0])
            print(joke_data[1])
            speak(joke_data[1])

        elif "exit" in text:
            speak("Goodbye!")
            break  # Exit the loop and end the program

        else:
            speak("Sorry, I didn't understand that. Could you repeat?")
