import os
from datetime import datetime

import requests

def get_paris_realtime_bicycle_data():
    
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"
    
    response = requests.request("GET", url)
    
    serialize_data(response.text, "paris_realtime_bicycle_data.json")
    

def get_nantes_realtime_bicycle_data():
    
    url= "https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_stations-velos-libre-service-nantes-metropole-disponibilites/exports/json"
    
    response = requests.request("GET", url)
    
    serialize_data(response.text, "nante_realtime_bicycle_data.json")

def get_toulouse_realtime_bicycle_data():
    url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/api-velo-toulouse-temps-reel/exports/json"
    response = requests.request("GET", url)
    serialize_data(response.text, "toulouse_realtime_bicycle_data.json")



def get_commune_data():
    url = "https://geo.api.gouv.fr/communes"
    
    # Requête GET à l'API sans paramètres
    response = requests.request("GET", url)
    
    # Vérification du statut de la réponse
    if response.status_code == 200:
        serialize_data(response.text, "commune_data.json")
    else:
        print(f"Erreur lors de l'appel à l'API: {response.status_code}")
        print(response.text)

def serialize_data(raw_json: str, file_name: str):
    today_date = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(f"data/raw_data/{today_date}"):
        os.makedirs(f"data/raw_data/{today_date}")
    

    with open(f"data/raw_data/{today_date}/{file_name}", "w") as fd:
        fd.write(raw_json)