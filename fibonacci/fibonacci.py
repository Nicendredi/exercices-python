from liste import *
# Cette ligne permet à {fibonacci.py} d'accéder aux fonctions de liste.py


# Une suite de Fibonacci est une suite où chaque élément est la somme des deux
# éléments précédents :
# f(0) = 1
# f(1) = 1
# f(2) = 2 = 1 + 1
# f(3) = 3 = 1 + 2
# f(4) = 5 = 2 + 3
# f(5) = 8 = 3 + 5


def combiner(objet1, objet2):
    # Cette fonction sert à être sûr qu'on peut combiner deux objets qu'ils
    # soient deux nombres, deux chqines de carqctère ou deux listes. On pourra
    # rajouter des cas au fur et à mesure
    if not isinstance(objet1, type(objet2)):
        # Beaucoup de languages ont une fonction similaire pour tester le type
        return False

    if isinstance(objet1, type(1)):
        # sont des nombres ?
        return objet1 + objet2
        # Addition

    elif isinstance(objet1, type("")):
        # sont des chaînes de caractère ?
        res = ""
        # Création d'une nouvelle chaîne
        for char in objet1:
            res = res + char
            # On ajoute les caractères de objet1
        for char in objet2:
            res = res + char
            # On ajoute les caractères de objet2
        return res

    elif isinstance(objet1, type([])):
        # sont des listes ?
        res = []
        for valeur in objet1:
            res.append(valeur)
            # On ajoute les valeurs de objet1
        for valeur in objet2:
            res.append(valeur)
            # On ajoute les valeurs de objet2
        return res
    return True


def afficherFibo(n):
    # Affiche la valeur de la suite de fibonacci à la position n et
    # renvoie True.
    # ex : afficherFibo(0) => print(1)
    # afficherFibo(5) => print(8)
    pass

# ----------------
# Les exercices suivants peuvent utiliser les fonctions créées dans {liste.py}
# pour simplifier le code et gagner du temps, mais ce n'est pas obligatoire
#
#   Exemple : Pour verifierFibo(l) : on compare la liste 'l' avec une liste
#             'lfibo' de même taille générée par listeFibo(n)
#
#   compareListes(l, lfibo) -> renvoie vrai si l et lfibo sont identiques
# ----------------


def listeFibo(n):
    # Créé une suite de Fibonacci jusqu'à n, organisé sous la forme d'une
    # liste, puis renvoie cette liste.
    pass


def verifierFibo(l):
    # Vérifie que la liste 'l' est bien une suite de Fibonacci. Renvoie True si
    # bien formée, False sinon
    pass


def elementNonFibo(l):
    # Renvoie le premier élément de la liste qui ne respecte pas la suite de
    # Fibonacci
    pass


# ----------------
# Tests écris à l'avance : vérifier dans la console si les résultats sont
# justes avant de passer à la fonction suivante
# ----------------

if combiner(1, 1):
    print("combiner(3,5) =", combiner(3, 5))
    print('combiner("ABC", "123") =', combiner("ABC", "123"))
    print(
        "combiner(['a', 'b'], ['%', '%', '%']) =",
        combiner(['a', 'b'], ['%', '%', '%']))
    print()

if afficherFibo(0):
    print("afficherFibo(0) =", afficherFibo(0))
    print("afficherFibo(1) =", afficherFibo(1))
    print("afficherFibo(5) =", afficherFibo(5))
    print()

if listeFibo(0):
    print("listeFibo(0) =", listeFibo(0))
    print("listeFibo(5) =", listeFibo(5))
    print("listeFibo(7) =", listeFibo(7))
    print()

if verifierFibo([]):
    print("verifierFibo([1,1,2,3,5]) =", verifierFibo([1, 1, 2, 3, 5]))
    print("verifierFibo([0,1,2,3,5]) =", verifierFibo([0, 1, 2, 3, 5]))
    print("verifierFibo([1,1,2,3,4]) =", verifierFibo([1, 1, 2, 3, 4]))
    print("verifierFibo([8,1,3,2,5,1]) =", verifierFibo([8, 1, 3, 2, 5, 1]))
    print()

if elementNonFibo([]):
    print("elementNonFibo([1,1,2,3,5]) =", elementNonFibo([1, 1, 2, 3, 5]))
    print("elementNonFibo([0,1,2,3,5]) =", elementNonFibo([0, 1, 2, 3, 5]))
    print("elementNonFibo([1,1,2,3,4]) =", elementNonFibo([1, 1, 2, 3, 4]))
    print(
        "elementNonFibo([8,1,3,2,5,1]) =",
        elementNonFibo([8, 1, 3, 2, 5, 1]))
    print()

# ----------------
# Exercices bonus
# ----------------


def estFibo(l):
    # Vérifie que la liste NON-TRIEE 'l' est une suite de Fibonacci. Renvoie
    # True si bien formée, False sinon
    pass

# ----------------
# La fonction print, peut accepter un paramètre spécial "end"
#
# Exemple : le code
# print("premier print", end=" ")
# print("deuxième print")
# print("troisième print")
#
# affiche :
# ==================
# premier print deuxième print
# troisième print
# ==================
# ----------------


def afficheTriangleListeFibo(l):
    # Affiche la liste 'l' (qui est une suite de Fibonacci) de la façon
    # suivante et renvoie True :
    # ==================
    # 1
    # 1 1
    # 1 1 2
    # 1 1 2 3
    # 1 1 2 3 5
    # ...
    # ==================
    pass


def afficheTriangleFibo(n):
    # Afficher la suite de Fibonacci jusqu'à 'n' avec le même visuel que
    # précédement et renvoie True
    pass

# ----------------
# Tests écris à l'avance : vérifier dans la console si les résultats sont
# justes avant de passer à la fonction suivante
# ----------------


if estFibo([]):
    print("estFibo([1,1,2,3,5])", estFibo([1, 1, 2, 3, 5]))
    print("estFibo([0,1,2,3,5])", estFibo([0, 1, 2, 3, 5]))
    print("estFibo([1,1,2,3,4])", estFibo([1, 1, 2, 3, 4]))
    print("estFibo([8,1,3,2,5,1])", estFibo([8, 1, 3, 2, 5, 1]))
    print()


if afficheTriangleListeFibo([]):
    print(
        "afficheTriangleListeFibo([1,1,2,3,5])",
        afficheTriangleListeFibo([1, 1, 2, 3, 5]))
    print(
        "afficheTriangleListeFibo([0,1,2,3,5])",
        afficheTriangleListeFibo([0, 1, 2, 3, 5]))
    print(
        "afficheTriangleListeFibo([1,1,2,3,4])",
        afficheTriangleListeFibo([1, 1, 2, 3, 4]))
    print(
        "afficheTriangleListeFibo([8,1,3,2,5,1])",
        afficheTriangleListeFibo([8, 1, 3, 2, 5, 1]))
    print()


if afficheTriangleFibo(0):
    print("afficheTriangleFibo(0)", afficheTriangleFibo(0))
    print("afficheTriangleFibo(5)", afficheTriangleFibo(5))
    print("afficheTriangleFibo(7)", afficheTriangleFibo(7))
