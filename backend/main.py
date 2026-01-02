from fastapi import FastAPI
from pydantic import BaseModel
from logic import classify_question
from news import get_capgemini_news
from ai import ask_ai

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        intent = classify_question(req.message)

        if intent == "news":
            articles = get_capgemini_news()
            if not articles:
                return {"reply": "No recent news available right now."}

            prompt = f"Summarize these Capgemini news articles:\n{articles}"
            reply = ask_ai(prompt)

        else:
            reply = ask_ai(req.message)

        return {"reply": reply}

    except Exception as e:
        print("Critical Server Error:", e)
        return {
            "reply": "Something went wrong on the server. Please try again later."
        }
