from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

app = FastAPI()

class Query(BaseModel):
    question:str

@app.post("/ask")

def ask(query:Query):

    prompt=f"""
    You are a regulatory compliance AI expert.

    Answer accurately.

    Question:
    {query.question}
    """

    response=model.generate_content(prompt)

    return {
        "answer":response.text
    }
