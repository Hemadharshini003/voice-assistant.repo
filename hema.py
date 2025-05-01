import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a female voice (index may vary)

# Initialize the recognizer
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises... please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print('Your message:', command)
    except Exception as ex:
        print("Sorry, I could not understand. Error:", ex)
        return

    if 'chrome' in command:
        engine.say('Opening Chrome...')
        engine.runAndWait()
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program]) 

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is:', time)
        engine.say('The time is ' + time)
        engine.runAndWait()

    elif 'play' in command:
        engine.say('Opening YouTube')
        engine.runAndWait()
        pywhatkit.playonyt(command)

    elif 'youtube' in command:
        engine.say('Opening YouTube')
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')

# Run the assistant
cmd()









































