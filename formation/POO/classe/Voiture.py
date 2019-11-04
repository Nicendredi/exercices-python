class Voiture():
    """docstring for Voiture."""

    def __init__(self, num, modele):
        self.__num = num
        self.__modele = modele


    def __del__(self):
        print("Destructeur appelé")
        self.__num = None
        self.__modele = None


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
