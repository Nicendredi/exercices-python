import sys

class Figure(object):

    # Variable de classe
    compteur = 0

    # Constructeur
    def __init__(self, nom):
        """ variable d'instance """
        self.nom = nom
        self.couleur = "rouge"
        Figure.compteur += 1

    def affiche(self):
        sys.stdout.write("figure nom="+self.nom+"\n")
