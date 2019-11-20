from nicendredi.dessin.Figure import Figure
from nicendredi.dessin.Cercle import Cercle
from nicendredi.dessin.Dessin import Dessin


figure1=Figure("rectangle")
figure2=Cercle("cercle")

figure1.affiche()
figure2.affiche()
print()
dessin1=Dessin("Cercle et rectangle")
dessin1.add(figure1)
dessin1.add(figure2)
dessin1.affiche()
