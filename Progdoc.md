# Le Jeu:
Le Morpion est un jeu à deux joueurs, qui est normalement joué sur une grille 3x3 mais peut-être aussi joué sur un 4x4 ou 5x5. Chaque joueur occupe une case par tour, avec le but de réaliser une des combinaisons gagnantes. Un premier joueur utilisera le ‘X’ comme sa marque, alors que le deuxième joueur utilisera le 'O'.

# Etape 1: Design de la grille

![Image1](https://user-images.githubusercontent.com/76202628/104844202-1b094900-58cf-11eb-86b7-1892568fe02b.jpg)

Quand un joueur veut marquer une case particulière, il doit entrer le numéro correspondant indiqué dans la grille. Supposons que nous souhaitions occuper le bloc central, alors nous entrerons 5 dans le terminal. 

Cette grille peut être générée par le code:

![Capture1](https://user-images.githubusercontent.com/76202628/104844281-ada9e800-58cf-11eb-8340-b80c8d1e4bb8.PNG)

Dans le code ci-dessus, la fonction crée notre jeu selon les valeurs livrées en argument. Ici, l’argument values est une liste contenant le statut de chaque cellule de la grille.

# Etape 2: Créer la table de score

La table de score est stockée sous forme de dictionnaire, où les clés sont les noms des joueurs et les valeurs sont leur nombre de victoires.

![Capture](https://user-images.githubusercontent.com/76202628/104844310-e9dd4880-58cf-11eb-8910-0c484647476c.PNG)

Pour afficher la table de score, nous avons besoin des noms des joueurs. Les clés sont extraites à l’aide de la fonction . keys() puis converti en liste, afin qu’il puisse être indexé lors de l’affichage des scores.

Résultat : ![Image2](https://user-images.githubusercontent.com/76202628/104844332-0e392500-58d0-11eb-87da-5d619231d088.jpg)

# Etape 3: Vérifier si c’est une victoire ou une partie nulle

Après chaque mouvement, nous devons vérifier si un joueur a gagné le jeu ou si c’est une partie nulle.Il peut être vérifié par le code :


![Capture2](https://user-images.githubusercontent.com/76202628/104844371-2b6df380-58d0-11eb-9183-eb3f99836bd5.PNG)



winner3x3() :  La fonction a toutes les combinaisons gagnantes. Tout ce qu’elle fait est de vérifier si l’une des combinaisons gagnantes est satisfaite par les positions du joueur actuel. Si elle le fait, il retourne True. Si aucune des combinaisons n’est satisfaite, alors la fonction retourne False.
draw3x3() : La condition du “draw” est assez simple, si les  neuf positions sont prises c’est une partie nulle ou un Draw.

# Etape 4: Storage d’information

À tout moment, nous avons besoin de deux informations cruciales :

●	État de la grille : Nous devons avoir une structure de données qui stocke l’état de chaque cellule, c’est-à-dire si elle est occupée ou vacante.
●	Mouvements de chaque joueur : Nous devons en quelque sorte connaître les mouvements passés et présents de chaque joueur, c’est-à-dire les positions occupées par « X » et « O ».

![Capture3](https://user-images.githubusercontent.com/76202628/104844408-50fafd00-58d0-11eb-9880-e9c7745b5918.PNG)


Le statut de la grille est géré par une liste de caractères, qui peut avoir trois valeurs possibles: ' ' , 'X' et 'O' .
Les mouvements de chaque joueur sont stockés comme un dictionnaire d’une liste de nombres entiers. Les clés sont 'X' et 'O' pour chaque joueur respectif. Leurs listes correspondantes contiennent les numéros donnés aux cellules de la grille qu’elles occupent.

# Etape 5: Boucle de jeu

Chaque jeu a une sorte de boucle de jeu, qui se déroule jusqu’à ce que certains joueurs gagnent ou le jeu se termine par un draw. Dans morpion, chaque itération de boucle se réfère à un seul mouvement que n’importe quel joueur fait.

![Capture4](https://user-images.githubusercontent.com/76202628/104844431-7556d980-58d0-11eb-881f-bc11906b1492.PNG)

# Etape 6: Vérification des positions

Afin de faire avancer le jeu de morpion, il nous faut vérifier que la position choisie par le joueur est  “correcte”. Pour cela, on a utilisé les blocs suivants :
-	try : lorsque le joueur va choisir sa position et si la position (move) n’est pas correcte, on va envoyer un message d’erreur,
        “ wrong Input! Try Again”.

![Capture5](https://user-images.githubusercontent.com/76202628/104844450-90c1e480-58d0-11eb-9b92-499d81267463.PNG)

Il y a différentes possibilités pour que la position ne soit pas correcte : soit la position n’est pas comprise dans le board ou soit la position a été déjà prise. Pour pallier ce problème, nous avons réalisé des boucles if.

-	Si la position n’est pas comprise dans le board, on renvoie un message d’erreur et on retourne au début de la loop

![Capture6](https://user-images.githubusercontent.com/76202628/104844459-a1725a80-58d0-11eb-9de1-a8fc4c48cf63.PNG)

-	Pour vérifier si la position a déjà été prise, il nous faut vérifier qu’il n’y pas de str dans les values. Dans le cas positif, on renvoie un message d’erreur.

![Capture7](https://user-images.githubusercontent.com/76202628/104844493-d41c5300-58d0-11eb-92f7-27670c8c2615.PNG)

Il nous faut mettre à jour les données de positions à chaque tour, pour cela, nous mettons à jour les variables concernant les positions. 


![Capture8](https://user-images.githubusercontent.com/76202628/104844503-e72f2300-58d0-11eb-905d-aa22d4505650.PNG)

On stocke les positions dans un tableau pour après les comparer aux positions gagnantes.
Pour renvoyer le gagnant, on réalise une condition qui retourne le gagnant, soit le joueur qui vient de mettre sa marque (current player).

![Capture9](https://user-images.githubusercontent.com/76202628/104844521-fa41f300-58d0-11eb-9057-d0140be2ff8e.PNG)

Lors d’une égalité, on va retourner un message qui nous indique que c’est un match nul.


![Capture10](https://user-images.githubusercontent.com/76202628/104844534-09c13c00-58d1-11eb-9727-defe22363648.PNG)


Enfin, il nous faut faire changer de joueur à chaque tour, donc à la fin de la boucle while, on implémente une condition qui fait modifier le joueur actuel.

![Capture11](https://user-images.githubusercontent.com/76202628/104844543-19d91b80-58d1-11eb-8739-89c70beb29e0.PNG)

# Etape 7 : la fonction main

Au départ de la fonction principale, il nous faut mettre en place les noms des joueurs:

![Capture12](https://user-images.githubusercontent.com/76202628/104844563-39704400-58d1-11eb-9ed2-f8f0aa039f7a.PNG)

On va affecter à la variable current_player le joueur 1 :

![Capture13](https://user-images.githubusercontent.com/76202628/104844576-4ee56e00-58d1-11eb-86c3-21b17f8fecc1.PNG)

On va stocker le joueur correspondant à la marque respective (X ou O) dans un dictionnaire :

![Capture14](https://user-images.githubusercontent.com/76202628/104844586-5c9af380-58d1-11eb-8385-307927ea4825.PNG)

On stocke les différentes marques dans un tableau :

![Capture15](https://user-images.githubusercontent.com/76202628/104844606-7ccab280-58d1-11eb-83d3-7873f2b5ce6c.PNG)

On initialise le tableau de score : 

![Capture16](https://user-images.githubusercontent.com/76202628/104844616-92d87300-58d1-11eb-9779-5e4f4e59df12.PNG)

## Plusieurs parties de jeu :

Nous allons faire une boucle pour lancer un round du jeu et d’autres (si choisie) et qui va s’arrêter lorsque les joueurs décideront de quitter le jeu.
Le joueur a 3 different choix au début de la partie : choisir X, choisir O ou bien de quitter le jeu :


![Capture17](https://user-images.githubusercontent.com/76202628/104844653-bdc2c700-58d1-11eb-8667-7b68c1767454.PNG)


Si le joueur ne rentre pas un chiffre correct (i.e ne correspondant pas aux différents choix donné), on envoie un message d’erreur:


![Capture18](https://user-images.githubusercontent.com/76202628/104844660-cddaa680-58d1-11eb-8f48-661ad97658c1.PNG)

Par la suite, il nous suffit de rajouter les conditions selon le choix du joueur :

-	Choix 1 : le joueur veut être X

![Capture19](https://user-images.githubusercontent.com/76202628/104844672-dcc15900-58d1-11eb-8051-ba8ae0c2ac85.PNG)

-	Choix 2 : le joueur veut être O


![Capture20](https://user-images.githubusercontent.com/76202628/104844680-ea76de80-58d1-11eb-8e08-3c67cb0034d4.PNG)


-	Choix 3 : le joueur quitte le jeu :

On renvoie l’historique final des matchs joués :


![Capture21](https://user-images.githubusercontent.com/76202628/104844696-f9f62780-58d1-11eb-8d5b-6703a29d47dc.PNG)

## 7 - 2 : Niveau de difficulté

Le joueur, ayant choisi sa marque (X ou O) a ensuite le choix entre 3 niveaux de difficultés (Easy : grille 3x3; Medium : grille 4x4; Hard : grille 5x5) :

![Capture22](https://user-images.githubusercontent.com/76202628/104844714-198d5000-58d2-11eb-8afb-c4c81f5505d3.PNG)

Lorsque le joueur rentre un mauvais chiffre (i.e différents de 1,2 ou 3), un message d’erreur va s’afficher. On va alors inviter le joueur à essayer une autre fois. 

![Capture23](https://user-images.githubusercontent.com/76202628/104844751-47729480-58d2-11eb-8f53-9f10d82bf028.PNG)

Pour les différents choix, nous allons lancer un rond de morpion, selon 
la difficulté choisie, et enregistrer le vainqueur de la partie :

![Capture24](https://user-images.githubusercontent.com/76202628/104844763-55281a00-58d2-11eb-9d0f-f5474c076534.PNG)

## 7 - 3 : Mise à jour de l’historique 

Lorsqu’il y a eu un vainqueur (pas d’égalité), on incrémente le score du joueur gagnant et on affiche l’historique :

![Capture25](https://user-images.githubusercontent.com/76202628/104844785-78eb6000-58d2-11eb-81d2-c82eb1be964b.PNG)

Enfin, il nous suffit de faire tourner les joueurs, c’est-à-dire, d’inverser les marques X et O :

![Capture26](https://user-images.githubusercontent.com/76202628/104844800-86084f00-58d2-11eb-9e18-776c071f7244.PNG)

# Exemple d’un rond de morpion (3x3):

![Image3](https://user-images.githubusercontent.com/76202628/104844826-a3d5b400-58d2-11eb-8dcd-6af707523656.jpg)


![Image4](https://user-images.githubusercontent.com/76202628/104844834-aa642b80-58d2-11eb-81a1-df4da909ad64.jpg)

![Image5](https://user-images.githubusercontent.com/76202628/104844837-b05a0c80-58d2-11eb-8d9d-95ffb0514939.jpg)


![Image6](https://user-images.githubusercontent.com/76202628/104844846-b9e37480-58d2-11eb-8b4d-7018bc35cc6a.jpg)

![Image7](https://user-images.githubusercontent.com/76202628/104844849-c10a8280-58d2-11eb-861d-0f124a9d2b1f.jpg)

![Image8](https://user-images.githubusercontent.com/76202628/104844854-c962bd80-58d2-11eb-86e5-270e4ffb7982.jpg)

![Image9](https://user-images.githubusercontent.com/76202628/104844861-d089cb80-58d2-11eb-869e-fecc559a1589.jpg)

![Image10](https://user-images.githubusercontent.com/76202628/104844869-dd0e2400-58d2-11eb-9d3d-04d3287c7579.jpg)

# Organigramme général : 

![Image11](https://user-images.githubusercontent.com/76202628/104844899-fa42f280-58d2-11eb-8feb-acb1f8ba4152.png)

# Organigramme fonction one_round3x3 :

![Image12](https://user-images.githubusercontent.com/76202628/104844923-0af36880-58d3-11eb-951b-2926bfa41ec0.png)

# Organigramme fonction one_round4x4 :

![Image13](https://user-images.githubusercontent.com/76202628/104844937-1e9ecf00-58d3-11eb-955c-1408283dac66.png)

# Organigramme fonction one_round5x5 :

![Image14](https://user-images.githubusercontent.com/76202628/104844954-337b6280-58d3-11eb-8b96-7dfe68a33237.png)





