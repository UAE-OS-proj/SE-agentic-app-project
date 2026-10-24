from pathlib import Path
from pypdf import PdfReader


def load_text(path: str) -> str:
    """Read a PDF or TXT file and return its text."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")

    suffix = p.suffix.lower()
    if suffix == ".pdf":
        reader = PdfReader(str(p))
        pages = [(page.extract_text() or "") for page in reader.pages]
        return "\n".join(pages).strip()
    if suffix == ".txt":
        return p.read_text(encoding="utf-8").strip()

    raise ValueError("Unsupported file type. Use .pdf or .txt")