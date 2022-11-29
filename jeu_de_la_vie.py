import random

class JeuVie:
    def __init__(self, ligne, colonne):
        """
            //Création d'une grille 2D avec deux paramètres ligne et colonne.
            Initialisation de la grille avec des valeurs aléatoires
            (1=vivant ou 0=mort)
        """
        """
            verif a faire
        """
        self.ligne = ligne
        self.colonne = colonne
        self.monde=[[random.randint(0,1) for x in range(self.colonne)] for y in range(self.ligne)]
    def __str__(self):
        """
            Affiche la grille avec les symboles graphiques du dictionnaire cells
            >>> grille = JeuVie(5,5)
            >>> grille.monde = [[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[1, 1, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
            >>> print(grille)
            .#...
            ..#..
            ###..
            .....
            .....
        """


x = JeuVie(5,3)
print(x)