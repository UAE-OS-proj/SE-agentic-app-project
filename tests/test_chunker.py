from src.rag.chunker import chunk_text


def test_empty_text_returns_empty_list():
    assert chunk_text("") == []
    assert chunk_text("   ") == []


def test_returns_list_of_strings():
    chunks = chunk_text("Scrum is agile. " * 200)
    assert isinstance(chunks, list)
    assert all(isinstance(c, str) for c in chunks)


def test_chunks_respect_size_limit():
    chunks = chunk_text("word " * 1000, chunk_size=200, chunk_overlap=20)
    assert len(chunks) > 1
    assert all(len(c) <= 200 for c in chunks)