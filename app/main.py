from fastapi import FastAPI
from pydantic import BaseModel

from app.llm import call_llm
from app.prompts import build_prompt
from app.config import TEMPERATURES
from app.memory import add_memory, get_context

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    mode: str = "balanced"  # creative / precise / balanced

@app.post("/chat")
def chat(req: ChatRequest):
    context = get_context(req.message)

    prompt = build_prompt(req.message, context)

    temperature = TEMPERATURES.get(req.mode, 0.5)

    response = call_llm(prompt, temperature)

    add_memory(req.message)
    add_memory(response)

    return {"response": response}