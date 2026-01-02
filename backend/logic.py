def classify_question(text: str) -> str:
    text = text.lower()

    if "news" in text or "latest" in text or "update" in text:
        return "news"

    if "about" in text or "what does" in text or "company" in text:
        return "about"

    return "general"
