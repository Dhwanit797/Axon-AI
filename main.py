import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclist


recognizer = sr.Recognizer()
engine = pyttsx3.init() 

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) ## [1] for female and [0] for male

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclist.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Alexa....")
    while True:
        # Listen for the wake word "Alexa"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "alexa"):
                speak("Yes,Sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Alexa active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)




        except Exception as e:
            print("Error; {0}".format(e))