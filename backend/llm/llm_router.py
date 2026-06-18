# backend/llm/llm_router.py

from backend.llm.config import USE_MOCK_LLM

def mock_response(prompt: str):
    return f"[MOCK RESPONSE] You asked: {prompt}"


def call_llm(prompt: str, real_llm_function):
    """
    This controls ALL LLM calls so we don't waste AWS tokens.
    """

    if USE_MOCK_LLM:
        return mock_response(prompt)

    return real_llm_function(prompt)