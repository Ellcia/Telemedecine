import pandas as pd

# Lire le fichier texte en tant que lignes
with open('input2.txt', 'r') as file:
    lines = file.readlines()

# Trouver l'indice où se termine l'en-tête
end_of_header = lines.index("# EndOfHeader\n") + 1

# Lire les données à partir de l'indice de fin de l'en-tête
data = [line.strip().split('\t')[1:] for line in lines[end_of_header:]]

# Créer un DataFrame à partir des données
df = pd.DataFrame(data)

# Enregistrer le DataFrame dans un fichier CSV sans l'en-tête
df.to_csv('output2.csv', index=False, header=False, sep='\t')

print("Fichier CSV créé avec succès.")



