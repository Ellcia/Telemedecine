import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def post_processing(name,data,loc):
    #data = pd.read_csv('datagret.csv')
    
    rsp = data["RESP_"+loc]
    df_stats = pd.DataFrame()
    
    try:
        signals, info = nk.rsp_process(rsp, sampling_rate=50, report=None)
        nk.rsp_plot(signals, info) 
        plt.gcf().set_size_inches(15, 9)
        plt.savefig("static/"+name+"_"+loc+".png")
        # Extraire les moyennes et écart-types de RSP_Rate et RSP_Amplitude et les arrondir au centième
        mean_rsp_rate = round(signals["RSP_Rate"].mean(), 2)
        std_rsp_rate = round(signals["RSP_Rate"].std(), 2)
        mean_rsp_amplitude = round(signals["RSP_Amplitude"].mean(), 2)
        std_rsp_amplitude = round(signals["RSP_Amplitude"].std(), 2)
        
        # Créer un nouveau DataFrame df_stats
        data = {'Fréquence respiratoire moyenne': [mean_rsp_rate], 'Ecart-type de la fréquence respiratoire': [std_rsp_rate],
                'Amplitude moyenne': [mean_rsp_amplitude], "Ecart-type de l'amplitude'": [std_rsp_amplitude]}
        
        df_stats = pd.DataFrame(data)
    except Exception as e:
        print("ERREUR: Le signal n'a pas pu être traité, il est probablement trop court pour être analysé (aucun cycle respiratoire détectée sur la fenêtre).")
        signals = None
        info = None
    
    return df_stats
    
#signals, info, df_stats=post_processing("E10_S1_1")

def overview(name,df):
    # Liste des colonnes de données (à l'exception de la colonne 'INDEX')
    data_columns = df.columns[1:5]

    # Paramètres du graphique
    sns.set(style="whitegrid")  # Style du graphique
    plt.figure(figsize=(16, 5))  # Taille du graphique

    # Créer un graphique séparé pour chaque colonne de données
    for i, column in enumerate(data_columns):
        plt.subplot(2, 2, i+1)  # 2x2 grid pour 4 graphiques
        sns.lineplot(data=df, x='TIME', y=column)
        plt.title(f'Graphique de {column}')
        plt.xlabel('TIME')
        plt.ylabel('Valeurs')

    # Ajuster l'espacement entre les graphiques
    plt.tight_layout()
    #plt.gcf().set_size_inches(15, 9)
    plt.savefig("static/"+name +"_OVERVIEW.png")
    return

def accelerometre(name,df):
    
    
    

    