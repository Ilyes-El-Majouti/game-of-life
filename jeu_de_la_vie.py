import random
import time

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
        grille = ""
        for ligne in self.monde:
            for colonne in ligne:
                if colonne:
                    grille = grille + "#"
                else:
                    grille = grille + "."
            grille = grille + "\n"
        return grille

    def get_grille(self, l, i):
        if (0 <= i < self.ligne) and (0 <= l < self.colonne):
            return self.monde[l][i]
        else:
            return False

    def evolution_cell(self, ligne, colonne):
        vivante = self.get_grille(ligne, colonne)
        totale = sum(self.get_grille(ligne + ii, colonne + jj)
                    for ii in [-1, 0, 1]
                    for jj in [-1, 0, 1]
                    if (ii, jj) != (0, 0))

        if totale == 3:
            celluleFutur = 1
        elif totale < 2 or totale > 3:
            celluleFutur = 0
        else:
            celluleFutur = vivante 
        return celluleFutur

    def evolution_jeu(self):
        self.monde = [[self.evolution_cell(y, x) for x in range(self.colonne)] for y in range(self.ligne)]

if __name__ == '__main__':
    #Instanciation de l'objet grille avec 10 lignes et 10 colonnes
    grille = JeuVie(10,10)
    print(grille)
    rep = 0
    #repeter 20 fois
    while rep <= 20:
        print("Répétition= ",rep)
        #appliquer une évolution du jeu à l'objet grille
        grille.evolution_jeu()
        time.sleep(0.2)
        print(grille)
        #Incrémenter la variable locale x
        rep = rep + 1