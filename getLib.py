import requests
import json
import pandas as pd



def getJson(params):
    url="https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
        }
    url=url+params
    response = requests.get(url, headers=headers)
    data = response.json()
    print(response.text)
    for session_id, session_data in data["contenu"]["sessions"].items():
        for sequence in session_data["sequences"]:
            sequence_structure = sequence["sequenceStructure"]
            sequence_data = sequence["data"]
    
            # Créer un dictionnaire de données pour le DataFrame
            data_dict = {column_name: [row[i] for row in sequence_data] for i, column_name in enumerate(sequence_structure)}
    
            # Créer un DataFrame à partir du dictionnaire de données
            df = pd.DataFrame(data_dict)
            df['TIME'] = (df['INDEX']) / 50 #modifier en fréquence
            
    
            # Afficher le DataFrame et la moyenne
            print(f"DataFrame pour la séquence {sequence['sequenceId']} de la session {session_id}:")
            print(df)
            print("\n")
    df.to_csv('datagret.csv', index=False)
    return df
