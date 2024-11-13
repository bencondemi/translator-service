# from sentence_transformers import SentenceTransformer, util
# model = SentenceTransformer('all-MiniLM-L6-v2')

# def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
#     """
#     Compares an LLM response to the expected answer using similarity scores.
#     Returns a score between 0 and 1, where 1 means identical and 0 means completely different.
#     """

#     embeddings = model.encode([expected_answer, llm_response])

#     similarity_scores = model.similarity(embeddings, embeddings)

#     return similarity_scores[0][1]

# def eval_single_response_classification(expected_answer: str, llm_response: str) -> float:
#     """
#     Compares an LLM response to the expected answer.
#     Returns 1.0 if they match exactly (case-insensitive), else 0.0.
#     """
#     return 1.0 if expected_answer.lower() == llm_response.strip().lower() else 0.0
    

# def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str]) -> float:
#     '''
#     Compares an LLM response tuple to the expected answer tuple.
#     Returns the average of classification and translation scores.
#     '''
#     expected_is_english, expected_translation = expected_answer
#     response_is_english, response_translation = llm_response

#     # Evaluate classification
#     classification_score = eval_single_response_classification(expected_translation, response_translation)

#     # Evaluate translation only if not English
#     if not expected_is_english:
#         translation_score = eval_single_response_translation(expected_translation, response_translation)
#     else:
#         # If English, ensure translation matches the original post
#         translation_score = eval_single_response_translation(expected_translation, response_translation)

#     # Return average score
#     return ((classification_score + translation_score) / 2)
    

from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from scipy.spatial.distance import cosine

# Load tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def encode_text(text: str) -> np.ndarray:
    # Tokenize input and convert to model embeddings
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings

def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
    embeddings_1 = encode_text(expected_answer)
    embeddings_2 = encode_text(llm_response)
    # Cosine similarity between embeddings
    similarity_score = 1 - cosine(embeddings_1, embeddings_2)
    return similarity_score

def eval_single_response_classification(expected_answer: str, llm_response: str) -> float:
    return 1.0 if expected_answer.lower() == llm_response.strip().lower() else 0.0

def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str]) -> float:
    expected_is_english, expected_translation = expected_answer
    response_is_english, response_translation = llm_response

    # Evaluate classification
    classification_score = eval_single_response_classification(expected_translation, response_translation)

    # Evaluate translation only if not English
    if not expected_is_english:
        translation_score = eval_single_response_translation(expected_translation, response_translation)
    else:
        translation_score = eval_single_response_translation(expected_translation, response_translation)

    return (classification_score + translation_score) / 2
