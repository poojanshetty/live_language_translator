import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = Translator()

supported_languages = {
    '1': ('English', 'en'),
    '2': ('Dutch', 'nl'),
    '3': ('French', 'fr'),
    '4': ('Spanish', 'es'),
    '5': ('German', 'de'),
    '6': ('Italian', 'it'),
    '7': ('Japanese', 'ja'),
    '8': ('Chinese (Simplified)', 'zh-CN'),
    '9': ('Hindi', 'hi'),
    '10': ('Arabic', 'ar'),
    '11': ('Russian', 'ru'),
    '12': ('Portuguese', 'pt'),
}

print("Select the target language for translation:")
for key, (language, code) in supported_languages.items():
    print(f"{key}: {language} ({code})")

choice = input("Enter the number corresponding to your choice: ")

if choice in supported_languages:
    target_language = supported_languages[choice][1]
else:
    print("Invalid choice. Exiting program.")
    exit()

while True:
    with sr.Microphone() as source:
        print("Speak Now..! ")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print("You said:", speech_text)
            if speech_text == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand. Can you please repeat?")
            speech_text = ""  # Set to empty string if not recognized
        except sr.RequestError:
            print("Could not request results from Google.")

        if speech_text:
            translated = translator.translate(speech_text, dest=target_language)
            translated_text = translated.text
            print("Translated text:", translated_text)

            voice = gTTS(translated_text, lang=target_language)
            voice.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
