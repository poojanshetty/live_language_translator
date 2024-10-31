# Live Language Translator

This application allows you to translate spoken language into another language and hear the translation using text-to-speech. It uses the following libraries:

- `speech_recognition`: To recognize spoken language.
- `googletrans`: To translate recognized speech into the desired language.
- `gtts`: To convert the translated text to speech.
- `playsound`: To play the audio generated from the translated text.

## Features

- Supports multiple languages for translation.
- Real-time speech recognition.

## Supported Languages

The application currently supports the following languages:

1. English (`en`)
2. Dutch (`nl`)
3. French (`fr`)
4. Spanish (`es`)
5. German (`de`)
6. Italian (`it`)
7. Japanese (`ja`)
8. Chinese (Simplified) (`zh-CN`)
9. Hindi (`hi`)
10. Arabic (`ar`)
11. Russian (`ru`)
12. Portuguese ('pt')

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/live_language_translator.git
   cd live_language_translator
   ```
2. Create a virtual environment:

  ```bash
pipenv install
```

3. Install the required packages:

```bash
pipenv install speech_recognition googletrans gtts playsound
```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Run the application:

```bash
python your_script_name.py
```

6. Select the target language for translation from the list provided.

7. Speak into the microphone when prompted.

The application will recognize your speech, translate it into the selected language, and play the translated audio.

Say "exit" to close the application.

# Requirements
- Python 3.6 or higher
- A working microphone and speakers
- Internet connection (for Google APIs)
- Troubleshooting
- Ensure that your microphone is set up correctly and is not muted.
- Make sure you have an active internet connection as the translation and speech recognition require internet access.
- License

# Acknowledgments
- SpeechRecognition for speech recognition functionality.
- Googletrans for translation.
- gTTS for text-to-speech.
- playsound for playing audio files.
- css
