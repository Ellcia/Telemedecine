
import pandas as pd
import json



def dataSequence2jsonFormat(dataFileName, deviceId, contexte, resolution, samplingRate, description, structure):
    output = dict()
    fields = dataFileName.split("_")
    print(fields)
    data = pd.read_csv("data_csv_processed/" + dataFileName + ".csv", header=None)  # Pas de nom de colonne

    # Ajouter une colonne 'index' avec les index de chaque ligne
    data.insert(0, 'index', range(len(data)))

    data = data.values.tolist()

    output.update({"deviceId": deviceId, "sequenceContext": contexte, "sequenceResolution": resolution,
                   "sequenceSamplingRate": samplingRate, "sequenceDescription": description, "sequenceStructure": structure,
                   "studentId": fields[0], "sessionId": fields[1], "sequenceId": int(fields[2]),
                   "sequenceStartDateTime": fields[3] + " " + fields[4].replace("-", ":"), "data": data})
    output = json.dumps(output)
    
    with open("data_json/"+dataFileName+".json", "w") as outfile:
        outfile.write(output)
        
    return output

    
