# -*-coding:Utf-8 -*

"""Ce fichier contient le code du serveur.

Il faut exécuter ce fichier avant de lancer un ou plusieurs clients.
Les clients sont contenus dans le fichier 'client.py'.

"""

import os
import socket
import select

from carte import Carte
from commande import commandes
from jeu import Jeu

# Create the game
jeu = Jeu(carte)
for i, commande in enumerate(commandes):
    # Commande Instanciation
    commandes[i] = commande(jeu)

	
# On connete le serveur
clients = []
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind(('localhost', 29408))
connexion.listen(5)
print("On attend les clients.")