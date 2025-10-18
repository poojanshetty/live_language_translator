import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
import tempfile
from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator

# Import your app (assuming app.py is in the same folder)
import app

class TestAppFunctions(unittest.TestCase):

    @patch.object(Translator, 'detect')
    def test_detect_language(self, mock_detect):
        mock_detect.return_value.lang = 'en'
        text = "Hello world!"
        detected_lang = app.translator.detect(text).lang
        self.assertEqual(detected_lang, 'en')
        mock_detect.assert_called_once_with(text)

    @patch.object(Translator, 'translate')
    def test_translate_text(self, mock_translate):
        mock_translate.return_value.text = 'Hola mundo!'
        text = "Hello world!"
        target_lang = 'es'
        translated = app.translator.translate(text, dest=target_lang).text
        self.assertEqual(translated, 'Hola mundo!')
        mock_translate.assert_called_once_with(text, dest=target_lang)

    @patch('app.gTTS')
    def test_tts_generation(self, mock_gTTS):
        # Mock gTTS instance
        mock_instance = MagicMock()
        mock_gTTS.return_value = mock_instance

        translated_text = "Hola mundo!"
        target_lang = 'es'

        # Use a temporary file to simulate audio generation
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_file:
            tts = gTTS(translated_text, lang=target_lang)
            tts.save(temp_file.name)
            mock_gTTS.assert_called_once_with(translated_text, lang=target_lang)
            mock_instance.save.assert_called_once_with(temp_file.name)

if __name__ == '__main__':
    unittest.main()
