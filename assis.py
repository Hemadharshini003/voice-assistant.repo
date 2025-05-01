import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)  # Listen to microphone input

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Error fetching results; {e}")
