<img src="https://repository-images.githubusercontent.com/572277884/983b8d6b-211b-43e9-b9e1-efad77f254e0" />

## **Jeu de la vie**

##### Le jeu de la vie est une modélisation simpliste de la vie de cellules dans l'espace. Dans le cadre de cet exercice l'espace sera une grille rectangulaire dont chaque case peut contenir au plus une cellule. Chaque case contiendra donc soit 0 soit 1 cellule en vie. 

##### Les voisines prises en compte sont toutes les cases situées immédiatement à gauche, à droite, en haut, en bas ou sur les quatre diagonales, si elles existent. Une case a donc au plus 8 voisines, moins si elle se situe sur un bord de la grille:

##### voisines <br> Les cellules peuvent émerger ou mourir selon des critères précis à réévaluer à chaque nouvelle génération :
* ##### Une cellule émergera dans une case qui possède exactement trois voisines avec une cellule:

##### 3voisins <br> Une cellule disparaît de sa case si elle est entourée par strictement moins de deux cellules vivantes ou strictement plus de trois cellules vivantes:

|  0 voisin  |  1 voisin  |  4 voisin  |  5 voisin  |
| ---------- | ---------- | ---------- | ---------- |
|     0      |     1      |      4     |      5     |
* ##### Les autres cases restent dans leur état:

##### 2 voisins ==> 2

## **Représentation d'une grille**

##### Du point de vue technique une grille du jeu de la vie sera représentée par une liste de listes de nombre entiers. Chaque nombre entier représente le nombre de cellules vivantes dans une case de la grille (0 ou 1). Par exemple la liste :

```
[ [0, 1, 0], [1, 0, 0] ]
```

##### représente une grille de jeu de 6 cases:
* ##### 3 cases en largeur
* ##### 2 cases en hauteur. 

##### Sur la première ligne seule la deuxième case possède une cellule (vie), tandis que sur la deuxième ligne, seule la première case en possède une (vie).

|             |  colonne 1  |  colonne 2  |  colonne 3  |
| ----------- | ----------- | ----------- | ----------- |
|   ligne 1   |      0      |      1      |      0      |
|   ligne 2   |      1      |      0      |      0      |
---

## **I. Implémentation**

## **1. Construction d'une grille aléatoire**

##### Q1. Créez un nouveau fichier jeu_de_la_vie.py dans un dossier* JeuVie* sur votre bureau Ubuntu.

##### Q2. Déclarez une classe JeuVie avec son constructeur:

## **création du constructeur: init()**
* Voici le doc string du constructeur:

```py
"""
Création d'une grille 2D avec deux paramètres ligne et colonne.
Initialisation de la grille avec des valeurs aléatoires
(1=vivant ou 0=mort)
"""
```

* ##### Implémentez votre constructeur afin d'instancier les deux attributs ligne et colonne.

* ##### Ajoutez à votre constructeur un contrôle de paramètres non vide sur les variables ligne et colonne. Vous utiliserez l'instruction assert qui retournera le message d'erreur suivant:

```
'attention aux paramètres ligne colonne non vide'
```

##### On désire à présent compléter le constructeur en ajoutant l'attribut d'instance monde qui correspond à la grille ligne∗colonneligne * colonneligne∗colonne avec des valeurs aléatoires (0 ou1):

##### **exemple1:** grille pour ligne=3 et colonne=2:

```
[[0, 0], [0, 0], [1, 1]]
```

##### **exemple2:** grille pour ligne=5 et colonne=3:

```
[[0, 0, 0], [0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]]
```

* ##### implémenter l'attribut d'instance monde en créant une grille:
    * ##### avec des valeurs aléatoires ("0" ou "1") en utilisant la méthode choice() de la classe **random**;
    * ##### par compréhension avec des relations ligne colonne.
##### **Remarque:** Il est recommandé de réaliser des testes dans le shell avant de l'implémenter dans la classe JeuVie. Vous pourrez également visualiser la construction par compréhension sur [Python Tutor (Python Tutor - Visualize Python, Java, JavaScript, C, C++, Ruby code execution)](http://pythontutor.com/visualize.html#code=table_2D%20%3D%20%5B%5B%200%20for%20x%20in%20range%283%29%5D%20for%20y%20in%20range%285%29%5D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## **2. Affichage de la grille: méthode str()**
##### Q3. Déclarez une méthode **str().**
* ##### Voici le doc string / doc test de la méthode **str:**

```py
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
```

##### Vous remarquerez que:
* ##### les "1" sont représentés par le symbole "#";
* ##### les "0" sont représentés par le symbole "."

##### Q4. Ajoutez à votre classe **JeuVie** un attribut de classe cells de type dictionnaire, qui permettra l'affichage des symboles "#" et ".".

##### Q5. Implémentez votre méthode str afin d'afficher la grille en la parcourant.

## **3. Tester si dans la grille: méthode get_grille()**

##### Il est nécessaire pour la suite de s'avoir si les coordonnées pointées par un numéro de ligne et de colonne appartiennent bien à la grille. Cette méthode retournera:
* ##### la valeur de la case pointée s'il elle est dans la grille;
* ##### la valeur False si la case pointée n'est pas dans la grille.

##### Q6. Implémentez votre méthode *get_grille()* qui prend en paramètres:
* ##### l : (int) correspondant à la ligne pointée
* ##### c:(int) correspondant à la colonne pointée

##### Voici un teste de la méthode *get_grille()*:
```py
>>> grille = JeuVie(4,4)
>>> grille.monde = [[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
>>> grille.get_grille(-1,2)
False
>>> grille.get_grille(2,0)
1
```

## **4. Evolution des cellules: méthode evolution_cell()**

##### Cette méthode revoie le nouvel état de la cellule pointée par sa position (ligne, colonne) en respectant les règles d'évolution du jeu.

##### Q7. Implémentez votre méthode *evolution_cell()* qui prend en paramètre la ligne et la colonne de la cellule pointée.

##### Voici les étapes à respectées pour implémenter votre méthode:
1. ##### Parcourir les cellules voisines et compter le nombre de True (ou "1")
2. ##### Appliquer les règles d'évolution du jeu, en fonction du nombre de True trouvé, pour déterminer le nouvel état de la cellule
3. ##### Retourner la valeur du nouvel état de la cellule pointée

##### Voici un test de la méthode *evolution_cell()*:

```py
>>> grille = JeuVie(4,4)
>>> grille.monde = [[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
>>> grille.evolution_cell(0,2)
False
>>> grille.evolution_cell(2,1)
True
```

## **5. Evolution du jeu: méthode evolution_jeu()**

##### Cette méthode "reconstruit" la grille, par compréhension, avec les nouveaux états des cellules.

##### Q8. Implémentez votre méthode evolution_jeu() qui ne prend aucun paramètre.

##### Voici un test de la méthode evolution_jeu():

```py
>>> grille = JeuVie(4,4)
>>> grille.monde = [[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
>>> grille.evolution_jeu()
>>> grille.monde
[[0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0]]
>>> grille.evolution_jeu()
>>> grille.monde
[[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
```

## **6. Test du programme et de la classe JeuVie**
##### Ajouter à la fin de votre programme le code suivant:

```py
#importer la classe time
import time

if __name__ == '__main__':
    #Instanciation de l'objet grille avec 10 lignes et 10 colonnes
    grille = ..........................
    print(grille)
    rep = 0
    #repeter 20 fois
    while .........:
        print("Répétition= ",rep)
        #appliquer une évolution du jeu à l'objet grille
        ............................
        time.sleep(0.2)
        print(grille)
        #Incrémenter la variable locale x
        rep = .....................
```

##### Q9. En vous aidant des commentaires, complétez puis testez votre code.

# **Motifs récurrents**

##### Quelques motifs récurrents peuvent être obtenus à partir de grilles particulières.

##### Par exemple, un oscillateur à deux états peut être obtenu avec cette grille :

```py
self.monde = [[0, 0, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [0, 1, 0, 0]]
```

##### ou encore celle-ci:

```py
self.monde = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
```

##### Autre exemple avec 15 états différents:

```py
self.monde = [[0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,1,1,1,0,0,0,0],
              [0,0,0,1,1,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,1,1,1,1,0,0,0],
              [0,0,0,0,1,1,1,0,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],]
```

# **Ressources additionnelles**

##### Vous trouverez des motifs plus complexes sur la [page Wikipedia du jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie#Structures), en particulier dans sa [version anglophone](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns). Cette [vidéo didactique](https://www.youtube.com/watch?v=S-W0NX97DB0) de David Louapre présente le jeu de la vie et des structures complexes.
