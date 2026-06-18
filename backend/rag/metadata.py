import json
import os

METADATA_FILE = "backend/rag/chunks.json"


def save_chunk_records(records):
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def load_chunk_records():
    if not os.path.exists(METADATA_FILE):
        return []

    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_chunks():
    records = load_chunk_records()
    return [item["text"] for item in records]