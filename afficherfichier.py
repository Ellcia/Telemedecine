import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lire le fichier CSV en utilisant pandas
df = pd.read_csv('datagret.csv')

# Liste des colonnes de données (à l'exception de la colonne 'INDEX')
data_columns = df.columns[1:5]

# Paramètres du graphique
sns.set(style="whitegrid")  # Style du graphique
plt.figure(figsize=(12, 8))  # Taille du graphique

# Créer un graphique séparé pour chaque colonne de données
for i, column in enumerate(data_columns):
    plt.subplot(2, 2, i+1)  # 2x2 grid pour 4 graphiques
    sns.lineplot(data=df, x='TIME', y=column)
    plt.title(f'Graphique de {column}')
    plt.xlabel('TIME')
    plt.ylabel('Valeurs')

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher les graphiques
plt.show()

print(df)
duree = df['TIME'].max()
# Obtenir l'amplitude maximale de la colonne 'RESP_THORAX'
amplitude_max_resp_thorax = df['RESP_THORAX'].max()

# Obtenir l'amplitude maximale de la colonne 'RESP_ABDOMEN'
amplitude_max_resp_abdomen = df['RESP_ABDOMEN'].max()


# Supposons que vous avez déjà un DataFrame appelé 'df' avec les colonnes 'TIME' et 'RESP_ABDOMEN'
# Si vous n'avez pas de DataFrame, assurez-vous de le charger avec vos données.

# 1. Calculez la différence entre les temps consécutifs pour obtenir les intervalles de temps
df['Temps_ecoule'] = df['TIME'].diff()

# 2. Trouver le début de chaque cycle respiratoire en utilisant la colonne 'RESP_ABDOMEN'
seuil_detection = 5000 # Choisissez un seuil approprié en fonction de vos données

# Créez une nouvelle colonne pour marquer le début de chaque cycle
df['Debut_cycle_respiratoire'] = (df['RESP_ABDOMEN'] > seuil_detection) & (df['RESP_ABDOMEN'].shift(1) <= seuil_detection)

# 3. Calculez la période en secondes comme la différence entre les temps des points de début des cycles respiratoires.
debut_cycles = df[df['Debut_cycle_respiratoire']]
periodes = debut_cycles['TIME'].diff().dropna()

# 4. Calculez la fréquence respiratoire en cycles par minute
periode_moyenne = df[df['Debut_cycle_respiratoire']]['Temps_ecoule'].mean()  # Période moyenne

# Supposons que vous avez déjà détecté les débuts de chaque cycle respiratoire et avez un DataFrame appelé 'df'
debut_cycles = df[df['Debut_cycle_respiratoire']]

# 1. Comptez le nombre de cycles respiratoires
nombre_cycles = len(debut_cycles)

# 2. Calculez la durée totale en secondes
duree_totale_en_secondes = df['TIME'].max()  # Prend la valeur maximale de 'TIME'

# 3. Calculez la fréquence respiratoire en cycles par minute
frequence_respiratoire = (nombre_cycles / duree_totale_en_secondes) * 60

# Affichez la fréquence respiratoire
print("Fréquence respiratoire (cycles par minute) :", frequence_respiratoire)




