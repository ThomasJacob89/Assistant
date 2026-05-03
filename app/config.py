import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4o-mini"  # cheap + fast for testing

TEMPERATURES = {
    "creative": 0.8,
    "balanced": 0.5,
    "precise": 0.2
}