# -*-coding:Utf-8 -*

"""Ce module contient la classe Joueur.

Un joueur est ici un objet faisant le lien entre le jeu de labyrinthe
et une connexion réseau (socket).

"""

from random import choice

from obstacle.mur import Mur
from obstacle.porte import Porte
from robot import Robot

class Joueur:

    """Classe représentant un joueur.
    """

    def __init__(self, jeu, client):
        self.jeu = jeu
        self.client = client
        self.numero = None
        self.robot = None

    def __repr__(self):
        return "<Joueur connecté sur {}>".format(self.client)

    def envoyer(self, message):
        """Envoie le message au client (socket)."""
        if self.client:
            self.client.send(message.encode())
			
    def placer_robot(self):
        """Place le robot aléatoirement sur la grille."""
        labyrinthe = self.jeu.labyrinthe
        grille = labyrinthe.grille
        libres = []
        x = 0
        y = 0