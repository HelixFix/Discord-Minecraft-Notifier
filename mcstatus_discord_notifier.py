import requests
import time

# Initialisation de la variable de cache
prev_online = 0

# URL de l'API
url = "https://mcstatus.io/api/v1/status?host=YOUR_SERVER_ADDRESS"

# URL du webhook Discord
discord_url = "https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL"

while True:
    try:
        # Requête GET à l'API
        response = requests.get(url)

        # Récupération du nombre de joueurs en ligne depuis la réponse JSON
        players_online = response.json()["players"]["online"]

        # Vérification si le serveur est en ligne et qu'il y a des joueurs connectés
        if players_online > 0:
            # Vérification si la précédente valeur de "online" était égale à 0
            if prev_online == 0:
                # Envoi de la notification sur Discord
                payload = {"content": "Le serveur est maintenant en ligne avec {} joueur(s) connecté(s)!".format(players_online)}
                requests.post(discord_url, json=payload)

        # Mise à jour de la valeur précédente de "online"
        prev_online = players_online

    except Exception as e:
        print("Une erreur est survenue : {}".format(e))

    # Attente d'une minute avant de refaire la vérification
    time.sleep(60)
