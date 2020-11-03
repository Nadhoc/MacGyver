# Projet Help MacGyver to escape !
Elaboration  du programme “Aider MacGyver à s’échapper”  


Programme écrit en Python3 grâce au module Pygame. Utilisation de Virtual Env et Git.

# 1- Préparation du projet :
- Initialisation d’un environnement virtuel de développement : virtual env/
- Initialisation d’un repo Github et initialisation d’un dépôt git en local 
- Création d’un fichier requirements.txt qui contiendra les versions des bibliothèques utilisées par le programme, dans notre cas Pygame.
- Creation de quatres fichiers .py : labyrinthe.py, human.py, constant.py et item.py qui contiendront le programme, les classes, les constantes du programme et un dossier ressources. 
- Création de deux dossiers : Fichiers divers et ressource : Chauns contient des élements images/ diagramme. 

# 2- Gestion des boucles du jeu avec l’affichage des fenêtres du jeu :
- Boucle Main: Initialisation de la fenêtre Pygame.
- Boucle Home: Fenêtre d’accueil du  jeu si on tape “ENTER” on rentre dans le jeu,  le fond d'écran utilisé est “HOME”. Si on lcique sur la croie on cloture la fanêtre de jeu.
- Boucle Game : Fenêtre affichant le labyrinthe, le fond d'écran utilisé est “BACKGROUND”

# 3- Génération de la structure du labyrinthe:

- Le labyrinthe est généré à partir d’une carte sous format .txt , il contient 15 lignes de 15 caractères: "w" = wall, "" = case vide, "a" = arrivée.
- Classe labyrinthe qui a comme attribut une grille vide au début et qui prend en paramètre le fichier .txt.
	- La méthode “generate” génère une liste de listes à partir de la lecture du fichier .txt . Cette liste de listes est mise dans l’attribut “grid” qui sera la matrice du Labyrinthe.
	- La méthode “display” itére sur la liste grid et affiche les sprites “mur” et “arrivée” selon si la cellule contient “w” ou “a” . Elle n’affiche rien pour les cases vides. L’affichage se fera grâce à un système de coordonnées x et y qui sera en pixel (SPRITE_SIZE) une case a une côte de 30*30.
	- La méthode “display” affiche le labyrinthe comme un calque apposé à “BACKGROUND”.
	- On affiche la photo du gardien sur la case “a”.
 	- Au niveau du programme, le labyrinthe est affiché lors de l’entrée dans la boucle jeu 

# 4-Affichage et gestion des déplacements de Macgyver:

- MacGyver est un objet de classe Human . Il a comme attributs ses coordonnées en réel et en pixel pour permettre son affichage et prend en paramètre le labyrinthe pour récupérer la grille  .
- Du programme: le joueur envoi des ordres de déplacement.
-  Ces ordres sont rentrés en paramètre à la méthode “move” de la classe Heroe: pour chacune des directions on modifie les coordonnées de MacGyver. 
- Dans le programme on affiche MacGyver avec ses nouvelles coordonnées.
- Lorsque MacGyver arrive sur la case “a” on a gagné et on sort du jeu pour aller à l’accueil.

# 5- Positionnement aléatoire des objets dans les couloirs du Labyrinthe:

- Création d’une classe item qui prend en attribut un nom, une surface (pour gérer l’affichage) et a comme attribut des coordonnées reelles et pixel. 
	- La méthode “locate_item” liste les coordonnées (cell, ligne) de toutes les cases vides du labyrinthe.
	 Elle met cette liste de tuple dans “position”. 
	 Puis on tire au sort grâce à un random.choice , un couple de coordonnée XY qui seront les coordonnées de l’élément créé.

	- La méthode “pin_items” vient écrire le nom de l’objet à son emplacement dans la matrice “grid” du labyrinthe.

# 6- Ramassage des éléments par MacGyver:
Lorsque MacGyver collecte un objet:

- La méthode display_items prend en paramètre MacGyver
-  Si aux coordonnées de MacGyver il y a le nom de l'élément on le remplace par "0"
-  On ajoute aussi le nom de l’objet à une liste vide TOOLS qui sert de compteur.

# 7- L’affichage des objets se fait de manière conditionnelle :
- display_items” , aux coordonnées de l'élément si il y a le nom dans la grille on l'affiche sinon on ne l'affiche pas.
- affichage du score : on prend en compte la liste TOOLS et on affiche en haut de la fenêtre de jeu l'image de l'élément dont le nom est contenu dans la liste.

# 8- You Win ou You Loose:

Si MacGyver se présente sur “a” avec une liste d’objet TOOLS inférieur à 3 il a perdu sinon il a gagné.

## 9- Amélioration du  programme: 

- Ajout de niveaux possibles
- Ajout de nouveaux éléments possibles( objets)
- Ajout de son 
- Ajout de règle complémentaire de type énigme. 
- Possibilité de déplacer le Gardien en l'instanciant comme un Human.

## 10- point d'amélioration globale

- Choix des images
- qualité des images
- attibuer au jour le changement de profil coordonnant avec la direction. 

