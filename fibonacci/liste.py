import random


def ajouteDansListe(liste, valeur):
    return liste.append(valeur)


def genererNombreBorne(min, max):
    return random.randrange(min, max)


def genererListeBornee(nb, min, max):
    # Créé une liste de 'nb' éléments tous compris entre 'min' et 'max'
    liste = []
    for i in range(nb):
        ajouteDansListe(liste, genererNombreBorne(min, max))
    return liste


def genererListeUniqueBornee(nb, min, max):
    # Créé une liste de 'nb' éléments tous compris entre 'min' et 'max' sans
    # doublons
    liste = []
    for i in range(nb):
        valeur = genererNombreBorne(min, max)
        unique = False
        while not unique:
            unique = True
            for val in liste:
                if val == valeur:
                    unique = False
                    valeur = genererNombreBorne(min, max)
                    break
        ajouteDansListe(liste, valeur)
    return liste


# -----------------------
# Tests de génération de liste
# -----------------------

print(genererListeBornee(0, 0, 0))
if genererListeBornee(0, 0, 0):
    liste = genererListeBornee(20, 0, 100)
    print("\n")
    print(liste)
    if len(liste) != len(set(liste)):
        print("Doublons trouvés ! Voici la liste ordonnée")
        liste.sort()
        print(liste)


if genererListeUniqueBornee(0, 0, 0):
    liste = genererListeUniqueBornee(20, 0, 100)
    print("\n")
    print(liste)
    if len(liste) != len(set(liste)):
        print("Doublons trouvés ! Voici la liste ordonnée")
        liste.sort()
        print(liste)


# -----------------------
# Fin des tests de génération de liste
# -----------------------


def compareListes(l1, l2):
    # Compare la liste 'l1' à 'l2', renvoie True, si elles sont de même taille
    # ET identiques, False sinon
    pass


def premierElemDiffListes(l1, l2):
    # Compare la liste 'l1' à 'l2' et renvoie le premier élément différent
    pass


def listeTriee(l):
    # Copie la liste 'l', la trie dans l'ordre croissant, puis la renvoie copie
    # triée
    pass


def listeTrieeDesc(l):
    # Copie la liste 'l', la trie dans l'ordre decroissant, puis la renvoie
    # copie triée
    pass

# ----------------
# Exercices bonus
# ----------------


def extraitDebutListe(l, n):
    # Copie les n premiers éléments d'une liste 'l' dans une liste, puis
    # renvoie celle-ci.
    pass


def extraitFinListe(l, n):
    # Copie les n derniers éléments d'une liste 'l' dans une liste, puis
    # renvoie celle-ci.
    pass


def extraitDemiListe(l, n):
    # Copie la première moitié des éléments d'une liste 'l' dans une liste,
    # puis renvoie celle-ci.
    # Pour calculer le milieu de la liste, on utilise la division entière
    pass


def inverseListe(l, n):
    # Copie la liste 'l' en partant de la fin dans une liste, puis renvoie
    # celle-ci.
    pass


def mirroirListe(l, n):
    # Copie la liste 'l' dans une nouvelle liste, ajouter la liste 'l' inversée
    # à cette nouvelle liste, puis renvoie celle-ci
    pass


def symetrieListe(l, n):
    # Copie la moitié de la liste 'l' dans une nouvelle liste, puis ajoute
    # cette même moitié de 'l' mais inversé. Enfin on renvoie la liste
    # ainsi formée
    pass


def sontIdentiquesListes(l1, l2):
    # Compare les listes non triées 'l1'et 'l2', renvoie True, si elles sont de
    # même taille ET identiques, False sinon
    pass


def elemDiffListes(l1, l2):
    # Compare les listes non triées 'l1'et 'l2' et renvoie un élément différent
    pass
