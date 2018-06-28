# -*-coding:Utf-8 -*

"""Fichier contenant la base des obstacles."""

class Obstacle:

    """Classe représentant tous les obstacles.

    Les obstacles sont généralement hérités de cette classe. Elle
    définit plusieurs méthodes et attributs qu'il faudra peut-être modifier
    dans les classes filles.

    """

    nom = "obstacle"
    peut_traverser = True
    symbole = ""

