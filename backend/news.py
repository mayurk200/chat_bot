import requests
import os
from dotenv import load_dotenv

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

def get_capgemini_news():
    try:
        url = "https://gnews.io/api/v4/search"
        params = {
            "q": "Capgemini",
            "lang": "en",
            "max": 5,
            "apikey": GNEWS_API_KEY
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return [
            {
                "title": a.get("title"),
                "description": a.get("description")
            }
            for a in data.get("articles", [])
        ]

    except requests.exceptions.RequestException as e:
        print("News API Error:", e)
        return []

    except Exception as e:
        print("Unexpected News Error:", e)
        return []
