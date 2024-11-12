from src.translator import translate_content
# from test.unit.eval_sets import *
# from test.unit.eval_fns import eval_single_response_complete



def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    
    assert is_english == False
    assert translated_content == "This is a Chinese message"

# eval_example_good = {"post": "Hier ist dein erstes Beispiel.", "expected_answer": (False, "Here is your first example.")}
# eval_example_bad = {"post": "asdfghjkl", "expected_answer": (False, "I don't understand your request.")}


# def test_valid():
#     content = eval_example_good["post"]
#     expected = eval_example_good["expected_answer"]
#     llm_response = translate_content(content)

#     similarity = eval_single_response_complete(expected, llm_response)

#     assert (0.90 <= similarity)

# def test_invalid():
#     content = eval_example_bad["post"]
#     expected = eval_example_bad["expected_answer"]
#     llm_response = translate_content(content)

#     assert ValueError("Invalid translation response.")
    


# def test_llm_normal_response():
#     for item in valid_eval_set:
#         content = item["post"]
#         print(content)
#         expected = item["expected_answer"]
#         llm_response = translate_content(content)
#         print(llm_response)
#         similarity = eval_single_response_complete(expected, llm_response)

#         assert (0.90 <= similarity)

# def test_llm_gibberish_response():
#     for item in invalid_eval_set:
#         content = item["post"]
#         expected = item["expected_answer"]
#         llm_response = translate_content(content)

#         assert ValueError("Invalid translation response.")


# import unittest
# from unittest.mock import patch

# class TestQueryLLMRobust(unittest.TestCase):

#     @patch.object(client.chat.completions, 'create')
#     def test_valid_translation(self, mock_create):
#         mock_create.return_value.choices[0].message.content = "This is your first example."
#         result = translate_content("Hier ist dein erstes Beispiel.")
#         self.assertEqual(result, (False, "This is your first example."))

#     @patch.object(client.chat.completions, 'create')
#     def test_already_english(self, mock_create):
#         mock_create.return_value.choices[0].message.content = "English"
#         result = translate_content("This is an English post.")
#         self.assertEqual(result, (True, "This is an English post."))

#     @patch.object(client.chat.completions, 'create')
#     def test_unexpected_response(self, mock_create):
#         mock_create.return_value.choices[0].message.content = "I don't understand your request"
#         result = translate_content("asdfghjkl")
#         self.assertEqual(result, (False, "Translation unavailable."))

#     @patch.object(client.chat.completions, 'create')
#     def test_empty_response(self, mock_create):
#         mock_create.return_value.choices[0].message.content = ""
#         result = translate_content("1234567890")
#         self.assertEqual(result, (False, "Translation unavailable."))

# def mock_llm():
#     unittest.main(argv=[''], exit=False)