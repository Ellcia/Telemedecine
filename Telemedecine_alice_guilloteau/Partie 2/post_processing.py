import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def post_processing(name,data,loc):
    # Réalise le post-traitement des données respiratoire (neurokit2) et crée les graphiques et dataframes associé
    
    #Respiration abdominale ou thorax
    rsp = data["RESP_"+loc]
    
    #Création du dataframe de statistiques
    df_stats = pd.DataFrame()
    
    try:
        # Post-traitement
        signals, info = nk.rsp_process(rsp, sampling_rate=50, report=None)
        
        # Création du graphique
        nk.rsp_plot(signals, info) 
        plt.gcf().set_size_inches(15, 9)
        # Enregistrement du graphique
        plt.savefig("static/"+name+"_"+loc+".png")
        
        # Extraire les moyennes et écart-types de RSP_Rate et RSP_Amplitude et les arrondir au centième
        mean_rsp_rate = round(signals["RSP_Rate"].mean(), 2)
        std_rsp_rate = round(signals["RSP_Rate"].std(), 2)
        mean_rsp_amplitude = round(signals["RSP_Amplitude"].mean(), 2)
        std_rsp_amplitude = round(signals["RSP_Amplitude"].std(), 2)
        
        # Créer un nouveau DataFrame df_stats
        data = {'Fréquence respiratoire moyenne': [mean_rsp_rate], 'Ecart-type de la fréquence respiratoire': [std_rsp_rate],
                'Amplitude moyenne': [mean_rsp_amplitude], "Ecart-type de l'amplitude": [std_rsp_amplitude]}
        
        df_stats = pd.DataFrame(data)
    except Exception as e:
        # Dans le cas ou le signal n'a pas pu être traité par rsp_process (pas assez de cycle respiratoire détecté)
        print("ERREUR: Le signal n'a pas pu être traité, il est probablement trop court pour être analysé (aucun cycle respiratoire détectée sur la fenêtre).")
        signals = None
        info = None
    
    # Citation de la librairie
    nk.cite()
    return df_stats
    


def overview(name,df):
    # Crée un graphique contenant les 4 signaux initiaux
    
    # Liste des colonnes de données (à l'exception de la colonne 'INDEX')
    data_columns = df.columns[1:5]
    
    # Noms des labels y
    
    y_labels = ["Respiration (V)", "Respiration (V)","Accélération (g)","Accélération (g)" ]
    # Paramètres du graphique
    sns.set(style="whitegrid")  # Style du graphique
    plt.figure(figsize=(16, 5))  # Taille du graphique

    # Créer un graphique séparé pour chaque colonne de données
    for i, column in enumerate(data_columns):
        plt.subplot(2, 2, i+1)  # 2x2 grid pour 4 graphiques
        sns.lineplot(data=df, x='TIME', y=column)
        plt.title(f'{column}')
        plt.xlabel('Temps (s)')
        plt.ylabel(y_labels[i])

    # Ajuster l'espacement entre les graphiques
    plt.tight_layout()
    
    # Enregistrement de l'image
    plt.savefig("static/"+name +"_OVERVIEW.png")
    return


def acceleration(name, df):
    # Crée un graphique contenant les signaux d'accélération et renvoie des statistiques dans un dataframe
    
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
    return acc_df
    