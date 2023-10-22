from flask import Flask, render_template, request
import pandas as pd
import requests
from getLib import getJson

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérez le paramètre entré dans le formulaire
        params = request.form.get('parametre')

        # Utilisez la fonction getJson pour obtenir le DataFrame
        df = getJson(params)

        # Transformez le DataFrame en HTML pour l'afficher dans la page
        df_html = df.to_html(classes='table table-bordered', index=False)

        return render_template('index.html', dataframe=df_html)

    return render_template('index.html')
