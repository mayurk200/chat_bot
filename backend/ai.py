import os
from dotenv import load_dotenv
from groq import Groq
from groq import GroqError

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You answer only questions related to Capgemini."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )
        return completion.choices[0].message.content.strip()

    except GroqError as e:
        print("Groq API Error:", e)
        return "AI service is temporarily unavailable. Please try again."

    except Exception as e:
        print("Unexpected AI Error:", e)
        return "An unexpected error occurred while generating a response."
