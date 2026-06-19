import numpy as np


def search(query, model, index, chunks, k=5):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        if i != -1:
            results.append(chunks[i])

    return results


def search_with_sources(query, model, index, records, k=10):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    query_words = [
        word.lower()
        for word in query.replace("?", "").split()
        if len(word) > 3
    ]

    results = []

    for rank, i in enumerate(indices[0]):
        if i != -1 and i < len(records):
            item = records[i]
            text_lower = item["text"].lower()

            keyword_hits = sum(
                1 for word in query_words
                if word in text_lower
            )

            results.append({
                "chunk_id": item["chunk_id"],
                "source": item["source"],
                "text": item["text"],
                "score": float(distances[0][rank]),
                "keyword_hits": keyword_hits
            })

    results = sorted(
        results,
        key=lambda x: (-x["keyword_hits"], x["score"])
    )

    return results[:5]