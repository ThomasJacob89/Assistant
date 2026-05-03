def build_prompt(user_input: str, context: str = ""):
    return f"""
You are a focused assistant.

Context:
{context}

User:
{user_input}

Respond clearly and concisely.
"""