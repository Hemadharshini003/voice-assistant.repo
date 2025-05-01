import speech_recognition as sr
import pyttsx3

import os  # For GPT-3/4 functionality
import time
from groq import Groq

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

        self.client = Groq(api_key="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")
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
            chat_response = self.client.chat.completions.create(
                messages=[
                    {
                "role": "system",
                "content": f"You are AI voice assistant get the message and reply to the user. ",
            },
                    {"role": "user", "content": input_text},
                ],
                model="llama3-8b-8192",
                temperature=0.5,
                max_tokens=1024,
                top_p=1)
            return chat_response.choices[0].message.content
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