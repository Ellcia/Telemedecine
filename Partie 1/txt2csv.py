import pandas as pd


def txt2csv(filename):
    # Convertit le fichier txt original provenant de biosignalplus, en un fichier csv contenant seulement les valeurs numériques

    # Lire le fichier texte
    with open("data_txt/"+filename+'.txt', 'r') as file:
        lines = file.readlines()
    
    # Trouver l'indice où se termine l'en-tête
    end_of_header = lines.index("# EndOfHeader\n") + 1
    
    # Lire les données à partir de l'indice de fin de l'en-tête
    data = [line.strip().split('\t')[1:] for line in lines[end_of_header:]]
    
    # Créer un DataFrame à partir des données
    df = pd.DataFrame(data)
    

    # # Inverser les valeurs des colonnes 3 et 4 (les axes étant inversés dans nos mesures)
    # colonne3 = df.iloc[:, 3].copy()
    # colonne4 = df.iloc[:, 4].copy()
    # df.iloc[:, 3] = colonne4
    # df.iloc[:, 4] = colonne3
    
    # Enregistrer le DataFrame dans un fichier CSV (sans l'en-tête)
    df.to_csv("data_csv_raw/"+filename+'.csv', index=False, header=False, sep='\t')
    




