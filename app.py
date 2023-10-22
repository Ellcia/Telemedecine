from flask import Flask, render_template, request, send_file
import pandas as pd
from getLib import getJson
from post_processing import post_processing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérez le paramètre entré dans le formulaire
        params = request.form.get('parametre')
        name=params[1:].replace("/","_")
        # Utilisez la fonction getJson pour obtenir le DataFrame
        df = getJson(params)

        # Appel de la fonction post_processing pour générer l'image
        post_processing(name,df)

        # Transformez le DataFrame en HTML pour l'afficher dans la page
        df_html = df.to_html(classes='table table-bordered', index=False)

        # Retournez le modèle HTML en passant le nom du fichier image
        return render_template('index.html', dataframe=df_html, image_path="" + name+".png")

    return render_template('index.html')
