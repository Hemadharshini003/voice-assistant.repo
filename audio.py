import pyttsx3

def text_to_speech(text, voice_id=None, rate=150):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set voice (optional)
    if voice_id is not None:
        engine.setProperty('voice', voice_id)

    # Set speech rate
    engine.setProperty('rate', rate)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Example text
    input_text = input("Enter the text you want to convert to speech:\n")
    text_to_speech(input_text)