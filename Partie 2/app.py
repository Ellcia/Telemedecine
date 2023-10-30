from flask import Flask, render_template, request, send_file
import pandas as pd
from getLib import getJson
from post_processing import post_processing, overview, acceleration

app = Flask(__name__)

# Créez un DataFrame vide par défaut
default_dataframe = pd.DataFrame()

@app.route('/', methods=['GET', 'POST'])
def index():
    df_stats_thorax = default_dataframe
    df_stats_abdomen = default_dataframe  # Initialisez df_stats_abdomen
    info_df = default_dataframe
    df_acc = default_dataframe
    image_path_thorax = ""
    image_path_abdomen = ""
    image_path_overview = ""
    image_path_acc = ""

    if request.method == 'POST':
        part1 = request.form.get('part1')
        part2 = request.form.get('part2')
        part3 = request.form.get('part3')

        # Concaténez les trois parties pour obtenir le paramètre complet
        params = "/" + part1 + "/" + part2 + "/" + part3
        name = params[1:].replace("/", "_")
        df, info_df = getJson(params)
        
        # Vérifiez si df existe
        if not isinstance(df, pd.DataFrame):
            # Si le DataFrame est vide, renvoyez un message d'erreur
            return "La séquence demandée n'existe pas."
        
        df_stats_thorax = post_processing(name, df, "THORAX")
        image_path_thorax = name + "_THORAX.png"

        df_stats_abdomen = post_processing(name, df, "ABDOMEN")
        image_path_abdomen = name + "_ABDOMEN.png"

        overview(name, df)
        image_path_overview = name + "_OVERVIEW.png"

        df_acc = acceleration(name, df)
        image_path_acc = name + "_ACC.png"

    return render_template('index.html', dataframe_thorax=df_stats_thorax, dataframe_abdomen=df_stats_abdomen, dataframe_info=info_df, dataframe_acc=df_acc,
                           image_path_thorax=image_path_thorax, image_path_abdomen=image_path_abdomen, image_path_overview=image_path_overview, image_path_acc=image_path_acc)

if __name__ == '__main__':
    app.run()
