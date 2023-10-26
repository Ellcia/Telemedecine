import requests
import json
import pandas as pd


def accelerometre_convert(df):

    # Fonction pour vérifier si une série contient uniquement des entiers
    def is_int_series(series):
        return all(value.is_integer() for value in series)

    # Vérification pour la colonne "ACC_VERTICAL"
    if is_int_series(df["ACC_VERTICAL"]):
        cmin = df["ACC_VERTICAL"].min()
        cmax = df["ACC_VERTICAL"].max()
        df["ACC_VERTICAL"] = ((df["ACC_VERTICAL"] - cmin) / (cmax - cmin)) * 2 - 1

    # Vérification pour la colonne "ACC_HORIZONTAL"
    if is_int_series(df["ACC_HORIZONTAL"]):
        cmin = df["ACC_HORIZONTAL"].min()
        cmax = df["ACC_HORIZONTAL"].max()
        df["ACC_HORIZONTAL"] = ((df["ACC_HORIZONTAL"] - cmin) / (cmax - cmin)) * 2 - 1
        
    return df

    

def getJson(params):
    url = "https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
    }
    url = url + params
    response = requests.get(url, headers=headers)

    data = response.json()

    # Créez une liste pour stocker les informations des séquences
    sequence_info_list = []

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
            sequence_info_list.append(sequence_info)

            sequence_structure = sequence["sequenceStructure"]
            sequence_data = sequence["data"]

            # Créez un dictionnaire de données pour le DataFrame
            data_dict = {column_name: [row[i] for row in sequence_data] for i, column_name in enumerate(sequence_structure)}

            # Créez un DataFrame à partir du dictionnaire de données
            df = pd.DataFrame(data_dict)
            df=accelerometre_convert(df)

            #Affiche le DataFrame et la moyenne
            print(f"DataFrame pour la séquence {sequence['sequenceId']} de la session {session_id}:")
            print(df)
            print("\n")

    #df.to_csv('datagret.csv', index=False)

    # Créez un DataFrame à partir de la liste d'informations de séquence
    info_df = pd.DataFrame(sequence_info_list)
    df['TIME'] = (df['INDEX']) / (info_df["sequenceSamplingRate"][0])  # modifier en fréquence

    # Affiche le DataFrame avec les informations extraites
    #print("DataFrame avec les informations de séquence:")
    #print(info_df)
    # print(type(df))
    # print(type(info_df))
    return df,info_df



df,info_df =getJson("/E9/S1/3")
    
