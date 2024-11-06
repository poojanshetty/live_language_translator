import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = Translator()

supported_languages = {
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
}
exit_keywords = ["exit", "quit", "stop", "end"]

# Display the language options to the user
print("Select the target language for translation:")
for code, language in supported_languages.items():
    print(f"{language} ({code})")

# Get user's choice
choice = input("Enter the language code for your choice: ").strip()

# Verify if the choice is valid
if choice in supported_languages:
    target_language = choice
    print(f"Selected language: {supported_languages[choice]}")
else:
    print("Invalid choice. Exiting program.")
    exit()

# Translation and speech loop
while True:
    with sr.Microphone() as source:
        print("Speak Now..! ")
        audio = r.listen(source)
        try:
            # Recognize speech
            speech_text = r.recognize_google(audio)
            print("You said:", speech_text)
            detected_lang = translator.detect(speech_text).lang
            print("Detected language:", detected_lang)

            if speech_text.lower() in exit_keywords:
                print("Exiting the program.")
                break
        except sr.UnknownValueError:
            print("Could not understand. Can you please repeat?")
            continue
        except sr.RequestError:
            print("Could not request results from Google.")
            continue

        if speech_text:
            translated = translator.translate(speech_text, dest=target_language)
            translated_text = translated.text
            print("Translated text:", translated_text)

            voice = gTTS(translated_text, lang=target_language)
            voice.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
