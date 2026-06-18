class ClaudeClient:
    def __init__(self):
        pass

    def invoke(self, prompt: str) -> str:
        return (
            "MOCK ANSWER: LLM is disabled due to quota, "
            "but the API, retrieval, OCR cache, FAISS index, and RAG flow are working."
        )


if __name__ == "__main__":
    client = ClaudeClient()
    print(client.invoke("What is RAG?"))