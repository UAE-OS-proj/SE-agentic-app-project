
from src.agents.prompts import EXPLAINER_PROMPT


def test_prompt_fills_all_fields():
    p = EXPLAINER_PROMPT.format(concept="Scrum", level="beginner", context="x")
    assert "Scrum" in p and "beginner" in p