# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:55:36 2023

@author: alice
"""
import pandas as pd
import json

import pandas as pd
import json

def dataSequence2jsonFormat(dataFileName, deviceId, contexte, resolution, samplingRate, description, structure):
    output = dict()
    fields = dataFileName.split("_")
    print(fields)
    data = pd.read_csv("datacsv/" + dataFileName + ".csv", header=None)  # Pas de nom de colonne

    # Ajouter une colonne 'index' avec les index de chaque ligne
    data.insert(0, 'index', range(len(data)))

    data = data.values.tolist()

    output.update({"deviceId": deviceId, "sequenceContext": contexte, "sequenceResolution": resolution,
                   "sequenceSamplingRate": samplingRate, "sequenceDescription": description, "sequenceStructure": structure,
                   "studentId": fields[0], "sessionId": fields[1], "sequenceId": int(fields[2]),
                   "sequenceStartDateTime": fields[3] + " " + fields[4].replace("-", ":"), "data": data})
    output = json.dumps(output)
    return output

    


dataFileName="95476D_S1_4_2023-09-22_10-42-11"
data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","REPOS",16,50,"Repos",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])
with open(dataFileName+".json", "w") as outfile:
    outfile.write(data)


dataFileName="95476D_S1_2_2023-09-22_10-40-37"
data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","DESCENTE",16,50,"Descente de 4 etages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])
with open(dataFileName+".json", "w") as outfile:
    outfile.write(data)
    
dataFileName="95476D_S1_1_2023-09-22_10-39-22"
data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","MONTEE",16,50,"Montee de 4 etages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])
with open(dataFileName+".json", "w") as outfile:
    outfile.write(data)


dataFileName="95476D_S1_3_2023-09-22_10-41-24"
data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","DESCENTE",16,50,"Descente de 4 etages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])
with open(dataFileName+".json", "w") as outfile:
    outfile.write(data)