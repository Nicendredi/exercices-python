class Voiture():
    """docstring for Voiture."""

    def __init__(self, num, modele):
        self.num = num
        self.modele = modele

    def afficheModele(self):
        print("Mon modèle est", self.modele)
