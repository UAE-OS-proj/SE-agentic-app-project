from pathlib import Path
from src.rag.loader import load_text
from src.rag.chunker import chunk_text
from src.rag.store import add_document


def ingest_path(path: str) -> int:
    chunks = chunk_text(load_text(path))
    return add_document(chunks, Path(path).name)


def ingest_upload(uploaded) -> int:
    """Save a Streamlit UploadedFile to data/uploads and index it."""
    dest = Path("data/uploads")
    dest.mkdir(parents=True, exist_ok=True)
    file_path = dest / uploaded.name
    file_path.write_bytes(uploaded.getvalue())
    return ingest_path(str(file_path))