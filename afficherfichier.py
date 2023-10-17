import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lire le fichier CSV en utilisant pandas
data = pd.read_csv('datagret.csv')

# Liste des colonnes de données (à l'exception de la colonne 'INDEX')
data_columns = data.columns[1:]

# Paramètres du graphique
sns.set(style="whitegrid")  # Style du graphique
plt.figure(figsize=(12, 8))  # Taille du graphique

# Créer un graphique séparé pour chaque colonne de données
for i, column in enumerate(data_columns):
    plt.subplot(2, 2, i+1)  # 2x2 grid pour 4 graphiques
    sns.lineplot(data=data, x='INDEX', y=column)
    plt.title(f'Graphique de {column}')
    plt.xlabel('INDEX')
    plt.ylabel('Valeurs')

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher les graphiques
plt.show()


