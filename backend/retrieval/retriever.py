import numpy as np


def search(query, model, index, chunks, k=3):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        if i != -1:
            results.append(chunks[i])

    return results


def search_with_sources(query, model, index, records, k=3):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for rank, i in enumerate(indices[0]):
        if i != -1 and i < len(records):
            item = records[i]

            results.append({
                "chunk_id": item["chunk_id"],
                "source": item["source"],
                "text": item["text"],
                "score": float(distances[0][rank])
            })

    return results