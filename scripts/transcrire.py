import whisper
import os
import json

# Spécifie explicitement le chemin de ffmpeg
os.environ["FFMPEG_BINARY"] = r"C:\Programs\ffmpeg\bin\ffmpeg.exe"  # Remplace par ton chemin exact

def transcrire_video(nom_fichier):
    chemin_fichier = os.path.join(os.path.dirname(__file__), "..", "videos", nom_fichier)
    model = whisper.load_model("medium")
    
    print(f"Chemin du fichier testé : {os.path.abspath(chemin_fichier)}")  # 🔍 DEBUG
    
    print(f"Transcription en cours pour : {chemin_fichier} ...")
    result = model.transcribe(chemin_fichier, fp16=False)
    texte = result["text"]
    print(f"Transcription terminée pour : {nom_fichier}\n")
    return texte

def transcrire_toutes_videos(dossier_videos):
    # Liste tous les fichiers du dossier
    videos = [f for f in os.listdir(dossier_videos) if f.endswith(('.mp4', '.mkv', '.avi'))]
    
    resultats = {}
    
    for video in videos:
        print(f"Traitement de la vidéo : {video}")
        texte_transcrit = transcrire_video(video)
        resultats[video] = texte_transcrit
    
    # Crée le dossier 'resultat_texte' s'il n'existe pas
    dossier_resultat = os.path.join(os.path.dirname(__file__), "..", "resultat_texte")
    os.makedirs(dossier_resultat, exist_ok=True)

    # Sauvegarder les résultats dans un fichier JSON
    chemin_json = os.path.join(dossier_resultat, "transcriptions.json")
    with open(chemin_json, "w", encoding="utf-8") as f:
        json.dump(resultats, f, ensure_ascii=False, indent=4)
    print(f"Toutes les transcriptions ont été enregistrées dans '{chemin_json}'.")

if __name__ == "__main__":
    dossier_videos = os.path.join(os.path.dirname(__file__), "..", "videos")
    transcrire_toutes_videos(dossier_videos)

