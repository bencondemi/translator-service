from src.translator import translate_content
from test.unit.eval_sets import *
from test.unit.eval_fns import eval_single_response_complete

import unittest
from unittest.mock import patch
from src.translator import client

# def test_llm_normal_response():
#     is_english, translated_content = translate_content("这是一条中文消息")
#     assert is_english == False
#     assert translated_content in ["This is a Chinese message.", 
#                                     "This is a message in Chinese."]

#     # is_english, translated_content = translate_content("Je suis vraiment content de te voir.")
#     # assert is_english == False
#     # assert translated_content in ["I am really happy to see you.",]



# def test_llm_gibberish_response():
#     is_english, translated_content = translate_content("asldjkjhfjsdh")
#     assert is_english == False
#     assert ValueError("Invalid translation response.")

#     is_english, translated_content = translate_content("1234567890")
#     assert is_english == False
#     assert ValueError("Invalid translation response.")
    


def test_llm_normal_response():
    for item in valid_eval_set:
        content = item["post"]
        print(content)
        expected = item["expected_answer"]
        llm_response = translate_content(content)
        print(llm_response)
        similarity = eval_single_response_complete(expected, llm_response)

        assert (0.90 <= similarity)

def test_llm_gibberish_response():
    for item in invalid_eval_set:
        content = item["post"]
        expected = item["expected_answer"]
        llm_response = translate_content(content)

        assert ValueError("Invalid translation response.")


@patch.object(client.chat.completions, 'create')
def test_llm_normal_response_mock(mocker):
    mocker.return_value.choices[0].message.content = "This is your first example."
    isEnglish, translatedContent = translate_content("Hier ist dein erstes Beispiel.")
    assert isEnglish == False
    similarity = eval_single_response_complete((False, "This is your first example."), (isEnglish, translatedContent))
    assert 0.90 <= similarity

    mocker.return_value.choices[0].message.content = "English"
    isEnglish, translatedContent = translate_content("This is an English post.")
    assert isEnglish == True
    similarity = eval_single_response_complete((True, "This is an English post."), (isEnglish, translatedContent))
    assert 0.90 <= similarity

@patch.object(client.chat.completions, 'create')
def test_llm_gibberish_response_mock(mocker):
    mocker.return_value.choices[0].message.content = "I don't understand your request."
    isEnglish, translatedContent = translate_content("asldjkjhfjsdh")
    assert isEnglish == False
    assert ValueError("Invalid translation response.")

    mocker.return_value.choices[0].message.content = "I don't understand your request."
    isEnglish, translatedContent = translate_content("1234567890")
    assert isEnglish == False
    assert ValueError("Invalid translation response.")

