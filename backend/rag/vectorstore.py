import faiss
import numpy as np
import os


def create_vectorstore(embeddings):
    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index


def save_index(index, path="faiss_index.index"):
    faiss.write_index(index, path)


def load_index(path="faiss_index.index"):
    if os.path.exists(path):
        return faiss.read_index(path)

    return None