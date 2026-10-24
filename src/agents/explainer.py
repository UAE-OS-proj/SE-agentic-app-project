from src.config import client, MODEL
from src.rag.store import retrieve
from src.agents.prompts import EXPLAINER_PROMPT, FOLLOW_UP_PROMPT

LEVELS = ("beginner", "intermediate", "advanced")


def explain(concept: str, level: str = "beginner") -> str:
    concept = concept.strip()
    if not concept:
        raise ValueError("Please enter a concept.")
    if level not in LEVELS:
        level = "beginner"
    context = "\n---\n".join(retrieve(concept)) or "None provided."
    prompt = EXPLAINER_PROMPT.format(concept=concept, level=level, context=context)
    return client.models.generate_content(model=MODEL, contents=prompt).text


def follow_up(concept: str, previous: str, question: str) -> str:
    prompt = FOLLOW_UP_PROMPT.format(
        concept=concept, previous=previous, question=question
    )
    return client.models.generate_content(model=MODEL, contents=prompt).text