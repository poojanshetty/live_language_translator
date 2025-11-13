import streamlit as st
import sounddevice as sd
import numpy as np
import tempfile
import time
import base64
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
from langdetect import detect
import scipy.io.wavfile as wav

# Page config
st.set_page_config(page_title="Voice Translator 🌍", page_icon="🎙", layout="centered")

# Title
st.markdown("<h1 style='text-align:center;'>🌍 Auto Voice Translator</h1>", unsafe_allow_html=True)

translator = GoogleTranslator(source='auto', target='en')
recognizer = sr.Recognizer()

languages = {
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

# Session state
if "exited" not in st.session_state:
    st.session_state.exited = False
if "running" not in st.session_state:
    st.session_state.running = False


def record_audio(duration=6, samplerate=16000):
    """Record audio from microphone using sounddevice"""
    st.info("🎙 Listening...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return np.squeeze(recording), samplerate


if not st.session_state.exited:

    # Get list of all language options
    language_options = list(languages.keys())

    # SINGLE SEARCHABLE DROPDOWN - Combines both search and selection
    st.markdown("### 🎯 Choose Target Language")

    # Create the searchable selectbox with a placeholder that suggests searching
    target_lang = st.selectbox(
        "**Type to search or select from dropdown:**",
        options=language_options,
        format_func=lambda x: f"{languages[x]} ({x})",  # Display format
        index=language_options.index('es'),  # Default to Spanish
        help="Start typing to search languages. Select from the filtered results."
    )

    # Show selected language confirmation
    st.success(f"✅ **Selected:** {languages[target_lang]} ({target_lang})")

    # Control buttons
    col1, col2 = st.columns(2)
    with col1:
        start_btn = st.button("▶️ Start Auto Translation", key="start_btn", type="primary")
    with col2:
        exit_btn = st.button("🚪 Exit", key="exit_btn")

    if exit_btn:
        st.session_state.exited = True
        st.rerun()

    if start_btn:
        st.session_state.running = True
        st.success("🎧 Auto translation started! Speak now...")

        stop_placeholder = st.empty()  # placeholder for the stop button

        while st.session_state.running:
            try:
                # Record with sounddevice
                audio_data, samplerate = record_audio(duration=6)

                # Save to a temporary WAV file (for SpeechRecognition)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
                    wav.write(temp_wav.name, samplerate, audio_data)

                # Recognize using Google Speech Recognition
                with sr.AudioFile(temp_wav.name) as source:
                    audio = recognizer.record(source)
                    text = recognizer.recognize_google(audio)

                text = text.strip().lower()
                if not text:
                    continue

                st.write(f"🗣 You said: {text}")

                # ✅ Voice exit command
                if text in ["exit", "stop", "quit", "close"]:
                    st.session_state.exited = True
                    st.session_state.running = False
                    st.success("👋 Exit command received. Closing translator...")
                    time.sleep(1.5)
                    st.rerun()

                detected_lang = detect(text)
                st.write(f"🌐 Detected Language: {detected_lang}")

                translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
                st.success(f"💬 Translated ({languages[target_lang]}): {translated}")

                # Speak translation (autoplay)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                    tts = gTTS(translated, lang=target_lang)
                    tts.save(temp_file.name)

                    with open(temp_file.name, "rb") as f:
                        b64_audio = base64.b64encode(f.read()).decode()

                    audio_html = f"""
                        <audio autoplay>
                            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                        </audio>
                    """
                    st.markdown(audio_html, unsafe_allow_html=True)

                # Check stop button dynamically
                if stop_placeholder.button("🛑 Stop Auto Translation", key=f"stop_btn_{time.time()}"):
                    st.session_state.running = False
                    st.rerun()

                time.sleep(1.5)

            except sr.UnknownValueError:
                st.warning("🤔 Didn't catch that, please repeat...")
                continue
            except sr.RequestError:
                st.error("⚠️ Speech recognition service unavailable.")
                break
            except Exception as e:
                st.error(f"Unexpected error: {e}")
                break

else:
    st.markdown("""
        <div style='text-align:center; margin-top:50px;'>
            <h2>👋 Thank you for using Voice Translator!</h2>
            <p style='font-size:18px;'>You can now safely close this browser tab.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr><p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
