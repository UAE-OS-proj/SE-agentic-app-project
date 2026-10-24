import pytest
from src.rag.loader import load_text


def test_loads_txt(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("hello world", encoding="utf-8")
    assert load_text(str(f)) == "hello world"


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_text("no_such_file.txt")