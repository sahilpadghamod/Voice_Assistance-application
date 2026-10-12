# 🎙️ Nova Voice Assistant

An industry-level, object-oriented Voice-Controlled Assistant that bridges local operating system automation with cloud-based generative AI to provide a seamless, hands-free conversational experience. 

By integrating speech recognition, native Windows text-to-speech synthesis, and the Google Gemini Large Language Model (LLM), Nova successfully executes predefined local tasks and dynamically answers open-ended queries.

## ✨ Core Features

*   **System Automation:** Voice-triggered execution of local OS commands, including time reporting, file system operations (Notepad), and web navigation (Google, YouTube, News).
*   **Conversational AI Fallback:** Utilizes the Google GenAI SDK to route unmapped commands to the `gemini-3.6-flash` model for dynamic, concise answers.
*   **Synchronous Audio Processing:** Employs native Windows `win32com.client` (SAPI5) to achieve reliable, non-blocking asynchronous audio processing, resolving common thread-locking bugs.
*   **Secure Credential Management:** Protects cloud API credentials using `python-dotenv` environment variable injection to prevent secret exposure in version control.

## 🛠️ Technology Stack

*   **Language:** Python 3.12
*   **Generative AI:** `google-genai` SDK (Gemini 3.6 Flash)
*   **Speech-to-Text (STT):** `SpeechRecognition`, `PyAudio`
*   **Text-to-Speech (TTS):** `pywin32` (SAPI5)
*   **Security & Configuration:** `python-dotenv`

## ⚙️ System Architecture

The application is built around a central `VoiceAssistant` class ensuring modularity and state management through the following workflow:
1.  **Initialization:** The application boots, calibrates the microphone for ambient noise, and initializes the SAPI5 audio dispatcher.
2.  **Listening Loop:** The system enters a continuous listening state, capturing audio and converting it to lowercase string commands.
3.  **Routing Logic:** String commands are evaluated against conditional local triggers for immediate OS task execution.
4.  **API Handoff:** Unmapped commands are wrapped in a behavioral prompt and sent to the Gemini LLM. The AI's text response is then piped back into the TTS engine.

## 🚀 Installation & Setup

### Prerequisites
* Python 3.12+
* Windows OS (Required for SAPI5 native TTS)
* A Google Gemini API Key

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sahilpadghamod/nova-voice-assistant.git](https://github.com/sahilpadghamod/nova-voice-assistant.git)
   cd nova-voice-assistant

   
## 1. Create and activate a virtual environment:
python -m venv venv
# On Windows:
venv\Scripts\activate

## 2. Install dependencies:
pip install -r requirements.txt

## 3. Configure Environment Variables:
### Create a .env file in the root directory and add your Gemini API key:
GEMINI_API_KEY=your_actual_api_key_here

## 4. Run the main application script from your terminal:
python assistant.py

## 🔮 Future Scope

Implementation of a GUI using Tkinter or PyQt.

Custom wake-word detection (e.g., using Porcupine) to eliminate the continuous listening loop.

Calendar and scheduling integration.
