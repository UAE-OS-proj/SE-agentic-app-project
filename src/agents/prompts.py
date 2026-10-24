EXPLAINER_PROMPT = """You are a friendly tutor.
Explain "{concept}" for a {level} learner in under 150 words, with one simple example.
Use the reference material only if it is relevant. If it is not, use general knowledge.

Reference material:
{context}
"""

FOLLOW_UP_PROMPT = """Concept: {concept}
Previous explanation: {previous}
The student asks: {question}
Answer briefly and clearly."""