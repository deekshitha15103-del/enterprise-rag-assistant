from backend.rag.pipeline import RAGPipeline

def main():
    rag = RAGPipeline()

    rag.build("sample.txt")

    print("\n=== QUERY TEST ===")

    query = "what is this document about?"

    answer = rag.query(query)

    print("\nFINAL ANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()
