import requests

def dummy_answer(question):
    return f"Answer to: {question}"

def process_query(doc_url, questions):
    # This is a placeholder logic. Replace with actual PDF/docx parsing and FAISS logic.
    # For demo purposes, we'll just echo the question.
    return [dummy_answer(q) for q in questions]
