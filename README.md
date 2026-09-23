🎙️ Nova: AI Voice Assistant

A Python-based desktop voice assistant capable of executing system-level commands, integrating speech recognition and text-to-speech, and handling asynchronous user interactions.

✨ Features
System Automation:** Converts speech to text and executes local OS commands.
Conversational AI:** Integrates with the official Google Gemini API (`gemini-3.6-flash`) for open-ended queries.
Native Audio:** Utilizes Microsoft's native SAPI5 COM interface for blocking, reliable text-to-speech synthesis.
Secure Architecture:** Implements `.env` variable injection to secure API keys.

🚀 Installation
1. Clone the repository.
2. Install dependencies: `pip install SpeechRecognition pywin32 python-dotenv google-genai pyaudio`
3. Add your Gemini API key to a `.env` file: `GEMINI_API_KEY=your_key_here`
4. Run `python assistant.py`
