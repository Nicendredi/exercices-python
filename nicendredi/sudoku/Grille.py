from nicendredi.sudoku.Cellule import Cellule

class Grille():
    """docstring for Grille."""

    def __init__(self, nom):
        self.nom = nom
        self.cellules = []
        for c in range(9*9):
            self.cellules.append(Cellule(0))

    def __str__(self):
        separateurH = "|"
        separateurV = "--" * 19 + "\n"
        grille= separateurV
        for l in range(9):
            for c in range(9):
                grille += separateurH + " " + self.cellules[l+c].__str__() + " "
            grille += separateurH + "\n" + separateurV
        return grille

    def affiche(self):
        print(self)
