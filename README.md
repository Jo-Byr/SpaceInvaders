# SpaceInvaders

Projet de programmation d'un Space Invader en Python en orienté objet.

Ce document est en français mais la documentation des fichiers est en anglais pour prendre de bonnes habitudes.

Commentaires sur le jeu:

  1-Pour lancer une partie il faut exécuter le fichier main.py
  
  2-Il n'y a qu'un seul niveau avec 25 aliens (on peut changer leur nombre depuis la ligne 62 de main.py en se référant à la documentation de la classe Alien dans le fichier alien.py)
  
  3-Code couleur : les protections changent de couleur en fonction de leur PV restants (cf. documentation de la classe Protection dans le fichier protection.py 
  
  les aliens pouvant tirer sont blancs, ceux ne le pouvant pas sont gris, leurs tirs sont bleus, ceux du joueur sont oranges
  
  4-Il n'y a pas de notion d'équilibrage : le niveau est potentiellement difficile avec 25 aliens car plus on en tue et plus les restants tirs souvent, l'alien bonus est très difficle à tuer
  
  5-Il y a au moins autant d'alien tireurs que de lignes d'aliens, quand le niveau commence, et la cadence de tirs des tireurs augmente lorsque leur nombre diminue (ligne 119 à 121 de alien.py)
  
  6-Le joueur est limité à 1 tir toutes les 2 secondes (changeable à la ligne 49 de shot.py)


Features manquantes :

  1-Fond d'écran
  
  2-Sprite en images au lieu de formes tkinter
  
  3-A propos


Commentaires :

  1-Nous avons essayé d'intégrer un fond d'écran mais les aliens se supprimaient spontanément. Nous supposons que cela est dû à notre méthode de gestion des collisions (faite avec la méthode overlapping de tkinter)
  
  2-Nous n'avons pas réussi à remplacer les sprites rectangles par des images
  
  3-Dans notre vision des choses, l'option A Propos aurait créer un popup mettant le jeu en pause et donnant des informations à son sujet mais nous n'avons pas réussi à mettre le jeu en pause
  
  
Bugs :

  1-Si le joueur perd car les aliens ont atteint le bas de l'écran, les tirs présents à l'écran continuent leur course
  
  2-Le bouton New Game ne remplit pas correctement son rôle : il réinitialise le jeu (le contenu du canvas) mais le comportement des aliens est inconstant après qu ce bouton ait été pressé : parfois ils fonctionnent comme prévu, parfois ils sont accélérés, parfois ils ne bougent plus, parfois la fenêtre plante


Commentaires :

  1-Ce bug est dû à notre organisation des fichiers qui ne permet pas un partage correct de variables globales, notamment une permettant de mettre le jeu en pause 
  
  2-Nous n'avons pas su trouver la raison de ce bug
  
  
Features que nous aurions voulu implémenter (et pensons savoir comment):

  1-Bonus de vitesse de déplacement ou de tir : les vitesses de tir et de déplacement sont toutes les deux facilement modifiables, respectivement dans shot.py (l.49) et dans ship.py (l.68 et l.117)
  
  2-Ennemis avec plus de 1PV, nous nous serions inspiré du système utilisé pour les protections
  
  3-Système de highscore, il aurait fallu enregistrer le score dans un fichier text sous condition qu'il soit, par exemple, un des 10 meilleurs
  
  4-Cheatcodes. Il aurait suffit de garder en mémoire les inputs du joueur un certains temps et voir s'il respectait un certain ordre. Une fenêtre de temps spécifique à chaque input aurait permis de minimiser les codes non intentionnels
  
  
Commentaire global : 

Etant notre premier projet en Orienté Objet, nous n'avons pas su organiser notre code correctement, et nous sommes retrouvé avec des importations cycliques en fin de dernière séance lorsque nous commencions à implanter les popups de victoire et défaite. Il était alors trop tard pour revoir la structure du code.
