import chromadb
from src.config import client, EMBED_MODEL

_db = chromadb.PersistentClient(path="data/chroma")
_col = _db.get_or_create_collection("knowledge_base")


def embed(texts: list[str]) -> list[list[float]]:
    result = client.models.embed_content(model=EMBED_MODEL, contents=texts)
    return [e.values for e in result.embeddings]


def add_document(chunks: list[str], source: str) -> int:
    if not chunks:
        return 0
    _col.upsert(
        ids=[f"{source}-{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embed(chunks),
        metadatas=[{"source": source}] * len(chunks),
    )
    return len(chunks)


def retrieve(query: str, k: int = 3) -> list[str]:
    if _col.count() == 0:
        return []
    result = _col.query(query_embeddings=embed([query]), n_results=k)
    return result["documents"][0]