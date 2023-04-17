from dotenv import load_dotenv
import requests
import time
import os

load_dotenv() # Charge les variables d'environnement à partir du fichier .env

# Accède à la valeur de la variable d'environnement YOUR_SERVER_ADDRESS
server_address = os.getenv('YOUR_SERVER_ADDRESS')

# Accède à la valeur de la variable d'environnement YOUR_DISCORD_WEBHOOK_URL
discord_url = os.getenv('YOUR_DISCORD_WEBHOOK_URL')

# Initialisation de la variable de cache
prev_online = 0

# URL de l'API
url = "https://api.mcstatus.io/v2/status/java/" + server_address

while True:
    try:
        # Requête GET à l'API
        response = requests.get(url)

        # Récupération du nombre de joueurs en ligne depuis la réponse JSON
        players_online = response.json()["players"]["online"]

        # Récupération du nom du serveur depuis la réponse JSON
        server_name = response.json()["host"]

        # Vérification si le serveur est en ligne et qu'il y a des joueurs connectés
        if players_online > 0:
            # Vérification si la précédente valeur de "online" était égale à 0
            if prev_online == 0:
                # Envoi de la notification sur Discord
                payload = {"content": "Le serveur {} est maintenant en ligne avec {} joueur(s) connecté(s)!".format(server_name, players_online)}
                requests.post(discord_url, json=payload)

        # Mise à jour de la valeur précédente de "online"
        prev_online = players_online

    except Exception as e:
        print("Une erreur est survenue : {}".format(e))

    # Attente d'une minute avant de refaire la vérification
    time.sleep(60)