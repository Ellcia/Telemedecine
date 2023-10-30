import requests
import json
import pandas as pd
import os



def postJson(jsonfile):
    url="https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    with open(jsonfile) as f:
        json1=json.load(f)
        dataset=json.dumps(json1)
        
    data={'dataset':dataset}

    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    
    
def postDossier(folder):
    # Poste l'intégralité des fichiers json d'un dossier sur le serveur
    fichiers = os.listdir(folder)

    for fichier in fichiers:
        if fichier.endswith(".json"):
            chemin_fichier = os.path.join(folder, fichier)
            postJson(chemin_fichier)