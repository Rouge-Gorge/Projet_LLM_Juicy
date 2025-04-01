import ollama
import json
import random
from transformers import pipeline
import os

# 📂 Charger la transcription pour récupérer le style
def charger_style_transcription(fichier_json, nombre_extraits=3):
    try:
        with open(fichier_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Vérifier que le fichier contient bien des transcriptions
        if not isinstance(data, dict) or len(data) == 0:
            raise ValueError("Le fichier JSON semble vide ou mal formaté.")

        # Extraire les transcriptions sous forme de liste
        transcriptions = list(data.values())

        # Sélectionner aléatoirement quelques extraits pour capter le style
        exemples = random.sample(transcriptions, min(len(transcriptions), nombre_extraits))

        return " ".join(exemples)  # Fusionner quelques extraits
    except Exception as e:
        print(f"Erreur lors du chargement du style : {e}")
        return ""

# 📌 Définir le fichier contenant les transcriptions

fichier_transcriptions = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "resultat_texte", "transcriptions.json")
)# fichier_transcriptions = "../resultat_texte/transcriptions.json"

# 📜 Extraire le style depuis les vidéos
style_extrait = charger_style_transcription(fichier_transcriptions)

stream = ollama.chat(
    model = 'llama3.1',
    messages=[{'role':'user', 'content':f"""Style à utiliser : "{style_extrait}"
Rédige un commentaire qu'on pourrait poster sur google maps pour mettre 5 étoiles à une salle de sport, en t'inspirant du style à utiliser.
"""}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)

