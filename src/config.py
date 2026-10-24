import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "gemini-embedding-001")

if not API_KEY:
    raise RuntimeError(
        "Missing GOOGLE_API_KEY (or GEMINI_API_KEY). Add it to your .env file."
    )

client = genai.Client(api_key=API_KEY)