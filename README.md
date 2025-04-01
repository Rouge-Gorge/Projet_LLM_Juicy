# Projet_LLM_Juicy
Récupérer les vidéos du personnage muscu de l'instagrammeur Galansire, les passer dans un algo de speech to text pour récupérer le texte. Demander à un LLM de s'inspirer du style du personnage pour rédiger des commentaires google maps.

NECESSAIRE POUR FAIRE TOURNER, IL FAUT FAIRE CA AVANT !!!

1️⃣ Tester directement avec le chemin absolu
Dans un terminal VS Code, essaye cette commande :

powershell
Copier
Modifier
C:\Programs\ffmpeg\bin\ffmpeg.exe -version
Si ça affiche la version, alors FFmpeg fonctionne bien.

2️⃣ Forcer VS Code à trouver FFmpeg
Si la commande ci-dessus fonctionne mais pas ffmpeg -version, alors ajoute ceci dans ton terminal :

powershell
Copier
Modifier
$env:Path += ";C:\Programs\ffmpeg\bin"
Puis réessaie :

powershell
Copier
Modifier
ffmpeg -version
Cela ajoute temporairement FFmpeg au Path pour ta session actuelle.