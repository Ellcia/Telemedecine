import requests
import pandas as pd



def convert(df,fe):
    # Applique les fonctions de transferts aux signaux


    # Fonction de transfert pour la colonne "ACC_VERTICAL"

    cmin = df["ACC_VERTICAL"].min()
    cmax = df["ACC_VERTICAL"].max()
    df["ACC_VERTICAL"] = ((df["ACC_VERTICAL"] - cmin) / (cmax - cmin)) * 2 - 1

    # Fonction de transfert pour la colonne "ACC_HORIZONTAL"

    cmin = df["ACC_HORIZONTAL"].min()
    cmax = df["ACC_HORIZONTAL"].max()
    df["ACC_HORIZONTAL"] = ((df["ACC_HORIZONTAL"] - cmin) / (cmax - cmin)) * 2 - 1
        
    # Convertion de l'accélération en m/s^2 (1 g = 9.81 m/s^2)
    df["ACC_VERTICAL2"] = df["ACC_VERTICAL"] * 9.81
    df["ACC_HORIZONTAL2"] = df["ACC_HORIZONTAL"] * 9.81
    
    # Fonction de transfert pour la colonne "RESP_THORAX""
    adc=df["RESP_THORAX"]
    df["RESP_THORAX"] = (adc/((2**16)-1))*3
    
    # Fonction de transfert pour la colonne "RESP_ABDOMEN""
    adc=df["RESP_ABDOMEN"]
    df["RESP_ABDOMEN"] = (adc/((2**16)-1))*3
    
        
    return df

    

def getJson(params):
    # Récupère un fichier json depuis le serveur et le convertit en dataframes exploitables 
    
    # Lien du serveur
    url = "https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    
    # Headers d'autentification
    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
    }
    url = url + params
    
    # Requête GET
    response = requests.get(url, headers=headers)

    data = response.json()
    
    # Cas les données n'ont pas pu être récupérées
    if data["code"] != "G00":
        return 0,0

    # Liste pour stocker les informations des séquences
    sequence_info_list = []
    
    # Extraction des informations du json
    for session_id, session_data in data["contenu"]["sessions"].items():
        for sequence in session_data["sequences"]:
            sequence_info = {
                "studentId": data["contenu"]["studentId"],
                "session_id": session_id,
                "sequenceId": sequence["sequenceId"],
                "sequenceStartDateTime": sequence["sequenceStartDateTime"],
                "sequenceContext": sequence["sequenceContext"],
                "sequenceSamplingRate": sequence["sequenceSamplingRate"],
                "sequenceDescription": sequence["sequenceDescription"],
                "sequenceResolution": sequence["sequenceResolution"],
                "deviceId": sequence["deviceId"],
                "sequenceRowNumber": sequence["sequenceRowNumber"]
            }
            
            # Dataframe d'informations
            sequence_info_list.append(sequence_info)
            info_df = pd.DataFrame(sequence_info_list)
            
            # Création d'un dictionnaire de données pour le DataFrame
            sequence_structure = sequence["sequenceStructure"]
            sequence_data = sequence["data"]
            data_dict = {column_name: [row[i] for row in sequence_data] for i, column_name in enumerate(sequence_structure)}

            # Création d'un DataFrame à partir du dictionnaire de données
            df = pd.DataFrame(data_dict)
            
            # Appel de la fonction convert pour appliquer les fonctions de transfert
            df=convert(df,info_df["sequenceSamplingRate"][0])


    # Création d'un colonne "TIME"

    df['TIME'] = (df['INDEX']) / (info_df["sequenceSamplingRate"][0])

    return df,info_df



    
