from nicendredi.dessin.Figure import Figure

class Cercle(Figure):
    """docstring for Cercle."""

    def __init__(self, nom):
        super(Cercle, self).__init__(nom)
        self.rayon = 10
        self.x = 150
        self.y = 150
