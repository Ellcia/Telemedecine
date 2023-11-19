import requests
import json
import pandas as pd
import os



def postJson(jsonfile):
    # Envoi un fichier json sur le serveur
    
    # Lien du serveur
    url="https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    
    # Ouverture du fichier json et conversion en dataset
    with open(jsonfile) as f:
        json1=json.load(f)
        dataset=json.dumps(json1)
        
    data={'dataset':dataset}
    
    # Header avec les identifiants
    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Requête POST
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    
    
def postDossier(folder):
    # Poste l'intégralité des fichiers json d'un dossier sur le serveur
    
    # Liste des fichiers du dossier
    fichiers = os.listdir(folder)

    for fichier in fichiers:
        # Appel de la fonction postJson pour chaque fichier json
        if fichier.endswith(".json"):
            chemin_fichier = os.path.join(folder, fichier)
            postJson(chemin_fichier)