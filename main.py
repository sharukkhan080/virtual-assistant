import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib


print("initialising sterex....")

MASTER = "MASTER"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)
    else:
        speak("good evening" +MASTER)

    speak("I am your creation welcome to my world")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sharukh.pathan245@gmail.com','microsoftaccount1234567890')
    server.sendmail("sharukh.pathan245@gmail.com",to,content)
    server.close()
if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'github' in query:
            url= "github.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'kaggle' in query:
            url= "kaggle.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'youtube' in query:
            url= "youtube.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        
        elif ' arif sir profile' in query:
            url= "https://www.linkedin.com/in/arifuddin-sohel-mohammed-37aaab20/"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            

        elif 'my college' in query:
            url= "http://mjcollege.ac.in/"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'satish' in query:
            url= "https://www.linkedin.com/in/indianservers/"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'whatsapp' in query:
            url= "https://web.whatsapp.com/"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'website' in query:
            url= "http://mjcollege.ac.in/studentresourceslist.php?resourceusername=arif.sohel"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query:
            url= "reddit.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        
        elif 'srk account' in query:
            url= "https://www.linkedin.com/in/pathan-sharuk-khan-402b2319b/"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query:
            songs_dir = "C:\\Users\\sharuk\\Downloads\\songs"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"{MASTER} THE TIME IS {strTime}")

        elif ' email to shahrukh' in query:
            try:
                speak("what should i send master")
                content = takeCommand()
                to = "sharukh.pathan245@gmail.com"
                sendEmail(to,content)
                speak("mail has been sent master thank you")
            except Exception as e:
                print(e)
                speak("i am sorry master i am unable to do that")