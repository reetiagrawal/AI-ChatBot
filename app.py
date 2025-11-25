import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# OpenAI client
client = OpenAI(api_key="my_api_key")
app = FastAPI()
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI chatbot."},
            {"role": "user", "content": req.message}
        ]
    )
    reply = response.choices[0].message.content
    return {"reply": reply}