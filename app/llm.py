import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("La clé API Hugging Face n'est pas définie. Vérifie ton fichier .env.")

MODEL = "facebook/bart-large-cnn"

def extract_contacts_with_hf(text: str) -> dict:
    """
    Utilise l'API Hugging Face pour extraire et structurer les informations de contact présentes dans le texte.
    Retourne un JSON structuré avec Nom, Email, Téléphone, Adresse.
    """
    prompt = f"""
    Extrait les informations de contact du texte suivant au format JSON :

    Texte :
    {text}

    Format attendu :
    {{
        "nom": "Nom de la personne",
        "email": "email@example.com",
        "telephone": "+33123456789",
        "adresse": "123 rue Exemple, Paris"
    }}
    """

    API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        response_json = response.json()
        print("Réponse de l'API Hugging Face :", json.dumps(response_json, indent=4)) 
        return response_json
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    texte_exemple = (
        "Jean Dupont, 45 rue Lafayette, Paris. "
        "Contact: jean.dupont@example.com, +33 6 12 34 56 78."
    )
    result = extract_contacts_with_hf(texte_exemple)
    print(json.dumps(result, indent=4))
