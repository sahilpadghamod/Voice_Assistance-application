import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import logging
import datetime
import sys
# Configure application-level logging
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

class VoiceAssistant:
    """An object-oriented voice assistant handling STT, task mapping, and TTS."""
    
    def __init__(self, name: str = "Nova"):
        self.name = name
        self.recognizer = sr.Recognizer()
        self.is_listening = True
        
        # Initialize text-to-speech engine
        try:
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty('voices')
            # Select secondary voice if available (often female on Windows/Mac)
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)
            self.engine.setProperty('rate', 165) # Optimize speaking pace
        except Exception as e:
            logging.critical(f"Failed to initialize TTS engine: {e}")
            sys.exit(1)

    def speak(self, text: str):
        """Convert string to audible speech."""
        logging.info(f"System Output: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> str:
        """Capture microphone audio and return transcribed text."""
        with sr.Microphone() as source:
            logging.info("Listening for command...")
            # Calibrate dynamically to ambient background noise
            self.recognizer.adjust_for_ambient_noise(source, duration=0.8)
            
            try:
                # Timeout limits how long it waits for speech to begin
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio).lower()
                logging.info(f"Recognized Input: '{command}'")
                return command
                
            except sr.WaitTimeoutError:
                logging.debug("Listening timed out. No speech detected.")
                return ""
            except sr.UnknownValueError:
                logging.warning("Speech detected but could not be deciphered.")
                return ""
            except sr.RequestError as e:
                logging.error(f"Speech recognition API error: {e}")
                self.speak("My speech services are currently offline.")
                return ""
            except Exception as e:
                logging.error(f"Unexpected audio error: {e}")
                return ""

    def process_command(self, command: str):
        """Route the transcribed text to the appropriate system function."""
        if not command:
            return

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}.")
            
        elif "open google" in command:
            self.speak("Opening Google Chrome.")
            webbrowser.open("https://www.google.com")
            
        elif "open notepad" in command:
            self.speak("Launching Notepad.")
            # OS-agnostic text editor launch
            os.system("notepad" if os.name == "nt" else "open -a TextEdit")

        elif "open youtube" in command:
                    self.speak("Opening YouTube.")
                    webbrowser.open("https://www.youtube.com")
            
        elif "news" in command:
            self.speak("Pulling up the latest headlines.")
            webbrowser.open("https://news.google.com")
            
        elif "take a note" in command or "write this down" in command:
            self.speak("What would you like me to write?")
            note_content = self.listen()
            if note_content:
                with open("assistant_notes.txt", "a") as file:
                    file.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] {note_content}\n")
                self.speak("I have successfully saved your note.")
            else:
                self.speak("I didn't catch that. Canceling note.")
                
        elif "joke" in command:
            self.speak("Why do software engineers prefer dark mode? Because light attracts bugs.")
            
        elif "exit" in command or "stop listening" in command or "quit" in command:
            self.speak(f"Shutting down {self.name} services. Goodbye!")
            self.is_listening = False
            
        else:
            logging.debug(f"Unhandled command: {command}")
            # Failsafe for unmapped commands
            self.speak("I am not programmed to handle that request yet.")

    def run_lifecycle(self):
        """Execute the primary assistant event loop."""
        self.speak(f"System online. Hello, I am {self.name}. Awaiting your instructions.")
        while self.is_listening:
            command = self.listen()
            self.process_command(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    try:
        assistant.run_lifecycle()
    except KeyboardInterrupt:
        logging.info("Application terminated by user via CLI.")