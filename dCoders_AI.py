import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeVoice():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am dCoders AI Sir. Please tell me how may I help you")

if __name__ == "__main__":
    wishMe()
    isRunning = True
    while isRunning:
        query = takeVoice().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            #open spotify
            webbrowser.open("spotify.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            #open vscode
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            #open chrome
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'shutdown system' in query:
            speak("Shutting down")
            isRunning = False

        elif 'about developers' in query:
            speak("The are pretty persion. ")
            
        elif 'open dCoders' in query:
            webbrowser.open("github.com/zamansheikh/dCoders_AI")

        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'shutdown computer' in query:
            speak("Shutting down your computer Sir")
            os.system("shutdown /s /t 1")
        elif 'restart computer' in query:
            speak("Restarting your computer Sir")
            os.system("shutdown /r /t 1")
        elif 'sleep computer' in query:
            speak("Sleeping your computer Sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'hibernate computer' in query:
            speak("Hibernating your computer Sir")
            os.system("shutdown /h")
        elif 'open notepad' in query:
            speak("Opening notepad")
            os.system("notepad")
        elif 'open calculator' in query:
            speak("Opening calculator")
            os.system("calc")
        elif 'open camera' in query:
            speak("Opening camera")
            os.system("start microsoft.windows.camera:")
        elif 'open task manager' in query:
            speak("Opening task manager")
            os.system("taskmgr")
        elif 'open control panel' in query:
            speak("Opening control panel")
            os.system("control panel")
        elif 'open command prompt' in query:
            speak("Opening command prompt")
            os.system("cmd")
        elif 'open paint' in query:
            speak("Opening paint")
            os.system("mspaint")
            