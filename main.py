import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('clearing background noises..please wait')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('ask me anything...')
        recorded_audio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(recorded_audio)

        print('your message',command)
    except Exception as ex:
        print("error recognizing speech:",ex)
        return
    command=command.lower()
    if 'chrome' in command:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndwait()
        program=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program]) 
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p') 
        print("current time:",time)
        engine.say(time)
        engine.runAndwait()
    if 'play' in command:
        b='Opening Youtube'
        engine.say(b) 
        engine.runAndWait()
        pywhatkit.playonyt(command) 
    if 'youtube' in command:
        b='opening Youtube'
        engine.say(b)
        engine.runAndwait()


# Run the assistant
cmd()        