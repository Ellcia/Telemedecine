import pandas as pd
import json



def dataSequence2jsonFormat(dataFileName, deviceId, contexte, resolution, samplingRate, description, structure):
    # Transforme un fichier csv comprenant les valeurs numérique et des informations en nom, 
    # en un fichier json prêt à être envoyé au serveur
    
    output = dict()
    
    # Séparation des champs présents dans le nom du fichier
    fields = dataFileName.split("_")
    
    # Récupération du fichier csv
    data = pd.read_csv("data_csv_processed/" + dataFileName + ".csv", header=None)

    # Ajout d'une colonne 'index'
    data.insert(0, 'index', range(len(data)))
    
    # Convertion des valeurs de data en liste
    data = data.values.tolist()
    
    # Assignation des paramètres correspondant au dictionnaire, selon le modèle que demande le serveur

    output.update({"deviceId": deviceId, "sequenceContext": contexte, "sequenceResolution": resolution,
                   "sequenceSamplingRate": samplingRate, "sequenceDescription": description, "sequenceStructure": structure,
                   "studentId": fields[0], "sessionId": fields[1], "sequenceId": int(fields[2]),
                   "sequenceStartDateTime": fields[3] + " " + fields[4].replace("-", ":"), "data": data})
    output = json.dumps(output)
    
    # Ecriture du fichier json
    
    with open("data_json/"+dataFileName+".json", "w") as outfile:
        outfile.write(output)
        
    return output

    
