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

The application currently supports the following 134 languages translation:

    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'as': 'Assamese',
    'ay': 'Aymara',
    'az': 'Azerbaijani',
    'bm': 'Bambara',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bho': 'Bhojpuri',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'zh-CN': 'Chinese (Simplified)',
    'zh-TW': 'Chinese (Traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'dv': 'Dhivehi',
    'doi': 'Dogri',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'ee': 'Ewe',
    'fil': 'Filipino (Tagalog)',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gn': 'Guarani',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'ilo': 'Ilocano',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jv': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'rw': 'Kinyarwanda',
    'gom': 'Konkani',
    'ko': 'Korean',
    'kri': 'Krio',
    'ku': 'Kurdish',
    'ckb': 'Kurdish (Sorani)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'ln': 'Lingala',
    'lt': 'Lithuanian',
    'lg': 'Luganda',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mai': 'Maithili',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mni-Mtei': 'Meiteilon (Manipuri)',
    'lus': 'Mizo',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ny': 'Nyanja (Chichewa)',
    'or': 'Odia (Oriya)',
    'om': 'Oromo',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'qu': 'Quechua',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'sa': 'Sanskrit',
    'gd': 'Scots Gaelic',
    'nso': 'Sepedi',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala (Sinhalese)',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tl': 'Tagalog (Filipino)',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'th': 'Thai',
    'ti': 'Tigrinya',
    'ts': 'Tsonga',
    'tr': 'Turkish',
    'tk': 'Turkmen',
    'ak': 'Twi (Akan)',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'

## Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:poojanshetty/live_language_translator.git
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
python3 main.py
```
## What does this application do?
- Select the target language code from the given list for translation.
- Speak into the microphone when prompted "Speak now...".
- The application will recognize your speech and which language you speak to the microphone, translate any language you speak into the selected/available language, and play the translation in audio.
- Say "exit", "quit", "stop" or "end" to close the application.

# Requirements
- Python 3.6 or higher
- A working microphone and speakers
- Internet connection (for Google APIs)
- Troubleshooting
- Ensure that your microphone is set up correctly and is not muted.
- Make sure you have an active internet connection as the translation and speech recognition require internet access.
- License

# Acknowledgments
- Speech recognition for speech recognition functionality.
- Googletrans for translation.
- gTTS for text-to-speech.
- playsound for playing audio files.
- css
