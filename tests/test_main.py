import unittest
from unittest.mock import patch, MagicMock
from main import detect_language, translate_text, text_to_speech

class TestMainFunctions(unittest.TestCase):

    @patch('main.translator.detect')
    def test_detect_language(self, mock_detect):
        # Mock the language detection
        mock_detect.return_value.lang = 'en'
        result = detect_language("Hello world!")
        self.assertEqual(result, 'en')
        mock_detect.assert_called_once()

    @patch('main.translator.translate')
    def test_translate_text(self, mock_translate):
        # Mock the translation
        mock_translate.return_value.text = 'Hola mundo!'
        result = translate_text("Hello world!", 'es')
        self.assertEqual(result, 'Hola mundo!')
        mock_translate.assert_called_once_with("Hello world!", dest='es')

    @patch('main.gTTS')
    @patch('main.playsound')
    @patch('main.os.remove')
    def test_text_to_speech(self, mock_remove, mock_playsound, mock_gTTS):
        # Mock text-to-speech
        mock_tts_instance = MagicMock()
        mock_gTTS.return_value = mock_tts_instance

        text_to_speech("Hola mundo!", 'es', filename="test.mp3")

        mock_gTTS.assert_called_once_with("Hola mundo!", lang='es')
        mock_tts_instance.save.assert_called_once_with("test.mp3")
        mock_playsound.assert_called_once_with("test.mp3")
        mock_remove.assert_called_once_with("test.mp3")


if __name__ == '__main__':
    unittest.main()
