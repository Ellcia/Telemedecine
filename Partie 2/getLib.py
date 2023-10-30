import requests
import json
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns



def accelerometre_convert(df,fe):

    # Fonction pour vérifier si une série contient uniquement des entiers
    # def is_int_series(series):
    #     return all(value.is_integer() for value in series)

    # Vérification pour la colonne "ACC_VERTICAL"

    cmin = df["ACC_VERTICAL"].min()
    cmax = df["ACC_VERTICAL"].max()
    df["ACC_VERTICAL"] = ((df["ACC_VERTICAL"] - cmin) / (cmax - cmin)) * 2 - 1

    # Vérification pour la colonne "ACC_HORIZONTAL"

    cmin = df["ACC_HORIZONTAL"].min()
    cmax = df["ACC_HORIZONTAL"].max()
    df["ACC_HORIZONTAL"] = ((df["ACC_HORIZONTAL"] - cmin) / (cmax - cmin)) * 2 - 1
        
        # Convertissez l'accélération en m/s^2 (1 g = 9.81 m/s^2)
    df["ACC_VERTICAL2"] = df["ACC_VERTICAL"] * 9.81
    
        # Convertissez l'accélération en m/s^2 (1 g = 9.81 m/s^2)
    df["ACC_HORIZONTAL2"] = df["ACC_HORIZONTAL"] * 9.81
    

    adc=df["RESP_THORAX"]
    df["RESP_THORAX"] = (adc/((2**16)-1))*3
    

    adc=df["RESP_ABDOMEN"]
    df["RESP_ABDOMEN"] = (adc/((2**16)-1))*3
    
        

        
    return df

    

def getJson(params):
    url = "https://www.gaalactic.fr/~sev_5106e/ws/physioData"
    headers = {
        "X-Auth": "Basic OTU0NzZEOkpncTdlWDU5QEA=",
    }
    url = url + params
    response = requests.get(url, headers=headers)

    data = response.json()
    if data["code"] != "G00":
        return 0,0

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
            info_df = pd.DataFrame(sequence_info_list)
            # Créez un dictionnaire de données pour le DataFrame
            data_dict = {column_name: [row[i] for row in sequence_data] for i, column_name in enumerate(sequence_structure)}

            # Créez un DataFrame à partir du dictionnaire de données
            df = pd.DataFrame(data_dict)
            df=accelerometre_convert(df,info_df["sequenceSamplingRate"][0])

            #Affiche le DataFrame et la moyenne
            print(f"DataFrame pour la séquence {sequence['sequenceId']} de la session {session_id}:")
            print(df)
            print("\n")

    #df.to_csv('datagret.csv', index=False)

    # Créez un DataFrame à partir de la liste d'informations de séquence

    df['TIME'] = (df['INDEX']) / (info_df["sequenceSamplingRate"][0])  # modifier en fréquence

    # Affiche le DataFrame avec les informations extraites
    #print("DataFrame avec les informations de séquence:")
    #print(info_df)
    # print(type(df))
    # print(type(info_df))
    return df,info_df



#df,info_df =getJson("/E10/S1/4")


def acceleration(name, df):
    # Créer une figure pour les deux graphiques
    plt.figure(figsize=(10, 6))

    # Premier graphique : accélération verticale
    plt.subplot(2, 1, 1)  # Deux lignes, un graphique par colonne, premier graphique
    sns.lineplot(data=df, x="TIME", y="ACC_VERTICAL2")
    plt.xlabel("Temps (s)")
    plt.ylabel("Accélération verticale (m/s^2)")
    plt.title("Accélération verticale en fonction du temps")

    # Deuxième graphique : accélération horizontale
    plt.subplot(2, 1, 2)  # Deux lignes, un graphique par colonne, deuxième graphique
    sns.lineplot(data=df, x="TIME", y="ACC_HORIZONTAL2")
    plt.xlabel("Temps (s)")
    plt.ylabel("Accélération horizontale (m/s^2)")
    plt.title("Accélération horizontale en fonction du temps")

    # Ajuster la mise en page pour éviter les superpositions
    plt.tight_layout()

    # Enregistrer l'image
    plt.savefig("static/" + name + "_ACC.png")

    # Afficher le graphique
    plt.show()
    
    # Calcul des statistiques
    mean_vertical = df["ACC_VERTICAL2"].mean()
    std_vertical = df["ACC_VERTICAL2"].std()
    mean_horizontal = df["ACC_HORIZONTAL2"].mean()
    std_horizontal = df["ACC_HORIZONTAL2"].std()
    
    # Créer un DataFrame pour stocker les statistiques
    acc_df = pd.DataFrame({
        "Accélération verticale moyenne": [mean_vertical],
        "Ecart-type accélération verticale": [std_vertical],
        "Accélération horizontale moyenne": [mean_horizontal],
        "Ecart-type accélération horizontale": [std_horizontal]
    })
    
    # Afficher les statistiques
    print(acc_df)
    return acc_df

# Exemple d'utilisation de la fonction avec un DataFrame 'df'
#a=acceleration("nom", df)
    
    
