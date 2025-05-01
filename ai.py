import speech_recognition as sr
import pyttsx3
import openai  # For GPT-3/4 functionality
import time

class VoiceAgent:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Configure voice properties (optional)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Change index for different voices
        self.engine.setProperty('rate', 150)  # Speed of speech
        
        # Set up OpenAI API (replace with your actual API key)
    
        openai.api_key =
    def listen(self):
        """Listen to microphone input and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                print("Could not request results; check your network connection.")
                return ""
    
    def think(self, input_text):
        """Process the input and generate a response"""
        if not input_text:
            return "I didn't hear anything. Could you repeat that?"
        
        # Using OpenAI's API for response generation
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": input_text}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I encountered an error processing your request."
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def run(self):
        """Main loop for the voice agent"""
        print("Voice Agent activated. Say 'exit' to quit.")
        
        while True:
            user__input = self.listen().lower()
            
            if "exit" in user__input:
                self.speak("Goodbye!")
                break
                
            if user__input:
                response = self.think(user__input)
                self.speak(response)

if __name__== "__main__":
    agent = VoiceAgent()
    agent.run()