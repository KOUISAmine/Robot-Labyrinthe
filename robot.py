# -*-coding:Utf-8 -*

"""Ce module contient la classe Robot.

Il ne s'agit pas du fichier qu'il faut exécuter pour lancer le jeu (voir
serveur.py).

"""

class Robot:

    """Classe représentant un robot."""

    symbole = "x"
    peut_traverser = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
