from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF",
    filename="capybarahermes-2.5-mistral-7b.Q2_K.gguf",
)

def extract_contacts_with_hf(
    text: str, 
    max_tokens: int = 1024,
    temperature: float = 0.7, 
    top_p: float = 0.95
) -> str:
    """
    Utilise le modèle CapybaraHermes pour extraire toutes les informations de contact depuis le texte donné.
    """
    prompt = (
        "Extrait TOUS les contacts dans le texte suivant, y compris leurs noms, emails, téléphones et adresses. "
        "Il est essentiel de ne manquer AUCUN contact, même s'il y en a plusieurs. "
        "Retourne le résultat en format JSON, chaque contact doit avoir les informations suivantes : "
        "\"Nom\", \"Email\", \"Téléphone\", et \"Adresse\". Si une information est manquante, la valeur doit être vide. "
        "N'oublie pas de gérer correctement la ponctuation et l'espace dans les adresses email. "
        "Assure-toi d'extraire tous les contacts du texte, même ceux mal formatés.\n\n"
        f"{text}\n\n"
        "JSON:"
    )

    try:
        response = llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        
        response_text = (
            response.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )
        return response_text
    except Exception as e:
        print("Error during LLM query:", e)
        return "{}"

