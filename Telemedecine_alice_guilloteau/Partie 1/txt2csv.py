import pandas as pd


def txt2csv(filename):
    # Convertit le fichier txt original provenant de biosignalplus, en un fichier csv contenant seulement les valeurs numériques

    # Lecture du fichier texte
    with open("data_txt/"+filename+'.txt', 'r') as file:
        lines = file.readlines()
    
    # Indice de fin de l'entête
    end_of_header = lines.index("# EndOfHeader\n") + 1
    
    # Récupération des données sans l'en tête
    data = [line.strip().split('\t')[1:] for line in lines[end_of_header:]]
    
    # Création d'un dataframe à partir des données
    df = pd.DataFrame(data)
    
    # Enregistrement dans un fichier csv
    df.to_csv("data_csv_raw/"+filename+'.csv', index=False, header=False, sep='\t')
    




