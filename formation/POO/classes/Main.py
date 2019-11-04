from Voiture import Voiture

print("==== Voiture 1 ====")
voiture1 = Voiture(1, "audi A3", "jaune")
voiture1.afficheModele()

voiture1.setModele("Renault R5")
voiture1.afficheModele()

print("\n\n==== Voiture 2 ====")
voiture2 = Voiture(2, "Audi A3", "noir")
voiture2.afficheModele()


# del voiture2


# copie = voiture2
# copie.afficheModele()
# del voiture2
# copie.afficheModele()
