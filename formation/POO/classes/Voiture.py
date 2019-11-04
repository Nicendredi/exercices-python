from Vehicule import Vehicule

class Voiture(Vehicule):
    """docstring for Voiture."""

    def __init__(self, num, modele, couleur):
        self.__num = num
        self.__modele = modele
        super().__init__(couleur)


    def __del__(self):
        print("Destructeur Voiture", self.__modele)
        self.__num = None
        self.__modele = None
        super().__del__()


    def getNum(self):
        return self.__num


    def setNum(self, num):
        self.__num = num


    def getModele(self):
        return self.__num


    def setModele(self, mod):
        self.__modele = mod


    def afficheModele(self):
        print("Mon modèle est", self.__modele)
