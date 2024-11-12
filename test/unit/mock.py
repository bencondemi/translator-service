import unittest
from unittest.mock import patch

from src.translator import translate_content

class TestQueryLLMRobust(unittest.TestCase):

    @patch.object(client.chat.completions, 'create')
    def test_valid_translation(self, mock_create):
        mock_create.return_value.choices[0].message.content = "This is your first example."
        result = translate_content("Hier ist dein erstes Beispiel.")
        self.assertEqual(result, (False, "This is your first example."))

    @patch.object(client.chat.completions, 'create')
    def test_already_english(self, mock_create):
        mock_create.return_value.choices[0].message.content = "English"
        result = translate_content("This is an English post.")
        self.assertEqual(result, (True, "This is an English post."))

    @patch.object(client.chat.completions, 'create')
    def test_unexpected_response(self, mock_create):
        mock_create.return_value.choices[0].message.content = "I don't understand your request"
        result = translate_content("asdfghjkl")
        self.assertEqual(result, (False, "Translation unavailable."))

    @patch.object(client.chat.completions, 'create')
    def test_empty_response(self, mock_create):
        mock_create.return_value.choices[0].message.content = ""
        result = translate_content("1234567890")
        self.assertEqual(result, (False, "Translation unavailable."))

# # Run the tests
# if __name__ == "__main__":
#     unittest.main(argv=[''], exit=False)
