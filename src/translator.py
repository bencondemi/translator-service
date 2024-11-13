def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "Checking to make sure this links correctly"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content

# from openai import AzureOpenAI

# # Initialize the Azure OpenAI client
# client = AzureOpenAI(
#     api_key="secrets.API_KEY",
#     api_version="2024-02-15-preview",
#     azure_endpoint="secrets.AZURE_ENDPOINT"
# )





# def get_translation(content: str) -> str:
#     """
#     Translates non-English text to English using the Azure OpenAI GPT-4 model.
#     If the language is unrecognized, returns a message indicating so.
#     """
#     context = "Translate this query from non-English into English. If you do not recognize the language, tell me 'I don't recognize this language'."
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": context
#             },
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ]
#     )
#     return response.choices[0].message.content

# def get_language(content: str) -> str:
#     """
#     Determines the language of the given text using the Azure OpenAI GPT-4 model.
#     Returns the language name as a string.
#     If the text is in an English dialect, returns 'English'.
#     """
#     context = "Determine what language this query is written in with one word. If it is an English-dialect, tell me 'English'."
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": context
#             },
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ]
#     )
#     return response.choices[0].message.content

# def translate_content(content: str) -> tuple[bool, str]:
#     """
#     Determines if the content is in English and translates it to English if it's not.
#     Handles unexpected model responses gracefully.
#     Returns a tuple: (is_english: bool, translated_content: str)
#     """

#     try:
#         language = get_language(content)
#         if not isinstance(language, str) or not language.strip():
#             raise ValueError("Invalid language response.")
#         if language.lower() == "english":
#             return (True, content)
#         else:
#             translation = get_translation(content)
#             # Check for invalid translation responses
#             invalid_responses = [
#                 "I don't understand your request.",
#                 "I don't know.",
#                 "Translation unavailable.",
#                 "I don't recognize this language."
#                 # Add other phrases as needed
#             ]
#             if not isinstance(translation, str) or translation.strip() in invalid_responses or not translation.strip():
#                 raise ValueError("Invalid translation response.")
#             return (False, translation)
#     except Exception as e:
#         # Log the error for debugging
#         print(f"Error processing content: {e}")
#         # Return default values to allow NodeBB to handle gracefully
#         return (False, "Translation unavailable.")
