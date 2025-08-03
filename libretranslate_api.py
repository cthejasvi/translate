import requests

BASE_URL = "http://127.0.0.1:5000"

def get_supported_languages():
    response = requests.get(f"{BASE_URL}/languages")
    response.raise_for_status()
    return response.json()

def translate_text(text, source_lang, target_lang):
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/translate", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["translatedText"]
