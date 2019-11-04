class Vehicule():
    """docstring for Vehicule."""

    def __init__(self, couleur):
        self.__couleur = couleur

    def afficherCouleur(self):
        print(self.__couleur)

    def __del__(self):
        print("Destructeur Vehicule", self.__couleur)
        self.__couleur = None
