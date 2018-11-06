# -*- coding: utf-8 -*
# Importation du module graphique graphics isn

'''
***Jeu du Morpion***
Réalisé par Lucas AUDENARD & Quentin MANSEY
La bibliothèque utilisé a été fourni par M.REMY
Vérifié au linter Python pour une mise en page correcte : http://pep8online.com/
'''

from graphics_isn import *

#--------------------------------------------------------
# On définit les constantes nécessaires au programme
#--------------------------------------------------------
grille_pas = 100        # espacement des lignes - en nombre de pixels
grille_cellules = 3     # nombre de case par ligne
# tableau dédié a contenir l'élément caractéristique du joueur
grille = []

#--------------------------------------------------------
# Création de la fenêtre graphique
#--------------------------------------------------------
def fenetregraph():
    init_graphic(grille_pas*grille_cellules, grille_pas*grille_cellules)

#--------------------------------------------------------
# Création du quadrillage
#--------------------------------------------------------
def quadrillage():
    a = grille_pas*grille_cellules  # longueur maximal de la fenetre graphique
    x = 0
    y = 0

    # lignes verticales
    while x < a:
        P1 = Point(x, 0)
        P2 = Point(x, a)
        draw_line(P1, P2, white)
        x = x + grille_pas

    # lignes horizontales
    while y < a:
        P3 = Point(0, y)
        P4 = Point(a, y)
        draw_line(P3, P4, white)
        y = y + grille_pas

#--------------------------------------------------------
# Fonction permettant de remplir les listes correspondant au lignes par des None
#--------------------------------------------------------
def init_grille():
    global grille
    for i in range(grille_cellules):        # une liste pour chaque ligne
        ligne = []
        for j in range(grille_cellules):    # On initialise nos trois cases
            ligne.append(None)              # ajoute None a nos listes -> personne a joué

            print(i, " ", j)                # affiche le nbr de case dans chaque ligne
        grille.append(ligne)                # On ajoute nos ligne dans un tableau nommé grille

#--------------------------------------------------------
# Fonction permettant de simplifier les coordonnées
#--------------------------------------------------------
def traiter_clic(tour):
    clic = wait_clic()  # On attend le clic de l'utilisateur
    # On affiche nos coordonées brute
    print("Abcisse : ", clic.x, " ", "Ordonnée : ", clic.y)

    '''On affecte a la variable colonne le résultat entier de notre divison
    de l'abcisse -> permet de nous situé dans le tableau
    ( 0 correspond a la colonne 1, 1 correspond a la colonne 2,
    2 correspond a la colonne 3)
    '''
    colonne = int(clic.x/grille_pas)

    '''
    On affecte a la variable ligne le résulatat entier de notre divison
    de l'ordonné -> permet de nous situé dans le tableau
    ( 0 correspond a la ligne 1, 1 correspond a la ligne 2,
    2 correspond a la lignne 3)
    '''

    ligne = int(clic.y/grille_pas)

    print("Coord: ", colonne, " ", ligne)  # affiche les coordonnées "simplifié"

    '''
    boucle permettant de joué, de testé si la case ou l'on clic a deja été joué
    '''
    if grille[ligne][colonne] is None:

        '''
        boucle permettant de gerer si le joueur 1 ou le jouer 2 joue ->
        si tour%2 = 0 il s'agit du joueur 1,
        tour%2 != 0 il s'agit du joueur 2
        '''
        # Joueur 1
        if tour % 2 == 0:
            grille[ligne][colonne] = 1              # variable propre au joueur 1
            dessiner_la_forme(clic)                 # détermine le centre la forme
            draw_fill_circle(Pp, 50, yellow)        # On dessine la forme du joueur
            verifier_si_gagnant(ligne, colonne, 1)  # fonction permettant de tester si le joueur gagne

            # Joueur 2
        else:
            grille[ligne][colonne] = 2              # On definit la variable propre au joueur 2
            dessiner_la_forme(clic)                 # fonction permettant de déterminer en fonction du clic le centre la forme du joueur
            draw_fill_circle(Pp, 50, green)         # On dessine la forme du joueur
            verifier_si_gagnant(ligne, colonne, 2)  # fonction permettant de tester si le joueur gagne
    else:
        print("case deja jouée")                    # si elle elle est déja jouée on affiche dans la console "case déja jouée"
    return clic

#--------------------------------------------------------
# Fonction permettant de tester si il y a un gagnant sur une ligne
#--------------------------------------------------------
def verifier_si_gagnant_ligne(ligne, joueur):
    for colonne in range(grille_cellules):          # boucle permettant se déplacer sur les différentes colonnes
        if grille[ligne][colonne] != joueur:        # on regarde au niveau de la réunion des lignes et des colonnes si la variable du joueur ne correspond pas a celle indiqué
            return 0                                # si c'est vérifé on ne fait rien
    return 1

#--------------------------------------------------------
# Fonction permettant de tester si il y a un gagnant sur une colonne
#--------------------------------------------------------
def verifier_si_gagnant_colonne(colonne, joueur):
    for ligne in range(grille_cellules):            # boucle permettant se déplacer sur les différentes lignes
        if grille[ligne][colonne] != joueur:        # on regarde au niveau de la réunion des lignes et des colonnes si la variable du joueur ne correspond pas a celle indiqué
            return 0                                # si c'est vérifé on ne fait rien
    return 1

#--------------------------------------------------------
# Fonction permettant de tester si il y a un gagnant sur la diagonales de gauche a droite
#--------------------------------------------------------
def verifier_si_gagnant_diagonale1(joueur):
    for i in range(grille_cellules):                # boucle permettant se déplacer sur les différentes colonnes
        for j in range(grille_cellules):            # boucle permettant se déplacer sur les différentes lignes
            if i == j:                              # on teste si on est sur une case ayant l'abcisse égale a l'ordonné
                if grille[i][j] != joueur:          # on regarde au niveau de la réunion obtenu juste avant des lignes et des colonnes si la variable du joueur ne correspond pas a celle indiqué
                    return 0                        # si c'est vérifé on ne fait rien
    return 1

#--------------------------------------------------------
# Fonction permettant de tester si il y a un gagnant sur la diagonales de droite a gauche
#--------------------------------------------------------
def verifier_si_gagnant_diagonale2(ligne, colonne, joueur):
        for i in range(grille_cellules):            # boucle permettant se déplacer sur les différentes colonnes
            for j in range(grille_cellules):        # boucle permettant se déplacer sur les différentes lignes
                if i + j + 1 == grille_cellules:    # on teste si on se trouve sur la diagonale de droite a gauche
                    if grille[i][j] != joueur:      # on regarde au niveau de la réunion obtenu juste avant des lignes et des colonnes si la variable du joueur ne correspond pas a celle indiqué
                        return 0                    # si c'est vérifé on ne fait rien

        return 1
#--------------------------------------------------------
# fonction appellant les 4 fonctions de test
#--------------------------------------------------------
def verifier_si_gagnant(ligne, colonne, joueur):

    '''
    On lance la vérification des lignes
    '''

    if verifier_si_gagnant_ligne(ligne, joueur):
        print("Joueur ", joueur, "a GAGNE sur la ligne ", ligne)
        wait_escape()
    else:
        print("Pas de gagnant sur la ligne ", ligne)


    '''
    On lance la vérification des colonnes
    '''

    if verifier_si_gagnant_colonne(colonne, joueur):
        print("Joueur ", joueur, "a GAGNE sur la colonne ", colonne)
        wait_escape()
    else:
        print("Pas de gagnant sur la colonne ", colonne)


    '''
    On lance la vérification de la diagonale de gauche a droite
    '''

    if verifier_si_gagnant_diagonale1(joueur):
        print("Joueur ", joueur, "a GAGNE sur la diagonale 1")
        wait_escape()
    else:
        print("Pas de gagnant sur la diagonale 1")


    '''
    On lance la vérification de la diagonale de droite a gauche
    '''
    if verifier_si_gagnant_diagonale2(ligne, colonne, joueur):
        print("Joueur ", joueur, "a GAGNE sur la diagonale 2")
        wait_escape()
    else:
        print("Pas de gagnant sur la diagonale 2")

    print("----------------------------------------------------------------")

#--------------------------------------------------------
# Fonction permettant de déterminé l'ordonnée de la forme
#--------------------------------------------------------
def ordonnees_de_la_forme(ordonnee):
    global clicY
    clicy = int(ordonnee/100)
    # généralisation de la mise au centre des ordonnées
    clicY = grille_pas/2 + (grille_pas/2) * clicy * 2


    global clicY

#--------------------------------------------------------
# Fonction permettant de déterminé l'abcisse de la forme puis le centre exacte de la forme
#--------------------------------------------------------
def dessiner_la_forme(clic):
    clicx = int(clic.x/100)
    # généralisation de la mise au centre des abcisses
    clicX = grille_pas/2 + (grille_pas/2) * clicx * 2
    ordonnees_de_la_forme(clic.y)

    Pp = Point(clicX, clicY)

    global Pp

#--------------------------------------------------------
# Lancer l'exection du programme
#--------------------------------------------------------
def main():
    fenetregraph()
    quadrillage()
    init_grille()
    print(grille)
    for i in range(grille_cellules*grille_cellules):
        traiter_clic(i)
        print(grille)
        print(i+2)
    print(grille)

main()
wait_escape()
