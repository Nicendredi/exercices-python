class Dessin():
    """docstring for Dessin."""

    def __init__(self, nom):
        self.nom = nom
        self.liste = []

    def add(self, obj):
        self.liste.append(obj)

    def affiche(self):
        print("===",self.nom,"===")
        for f in self.liste:
            f.affiche()
