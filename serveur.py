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

	
#Connect
clients = []
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind(('localhost', 29408))
connexion.listen(5)
print("On attend les clients.")

# Card choice
labyrinthe = None
while labyrinthe is None:
    choix = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
    try:
        choix = int(choix)
    except ValueError:
        print("Choix invalide : {}".format(choix))

#Disconnect
for client in clients:
    client.send("La partie est finie !".encode())
    client.close()