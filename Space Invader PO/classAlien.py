#Header
"""
But : classe qui gère un Alien
Auteur : Ankou Pierre-Olivier
date de maj : 08/01/2021
"""

"""
Cette classe cAlien définit les propritété d'un alien.
Chaque objet contient un alien avec ses propriétés.
La définition nécessite 9 paramètres (la fenêtre, le canvas, la coordonnée x et y
la deuxième position x et y, la direction et le groupe auquelle il appartient).
Il existe 1 méthode pour le moment :
    -fdeplacement : Cette méthode ne prend aucun arguments en paramètre
    et ne retourne rien. Son rôle est de déplacer en boucle l'alien dans une
    direction.
"""

from tkinter import Tk,Canvas

from classGrpAlien import cGrpAlien

class cAlien():
    def __init__(self,window,canvas1,alien,x,y,rdx,rdy,direction,groupe):
        self.window = window
        self.canvas = canvas1
        self.alien = alien
        self.x = x
        self.y = y
        self.rdx = rdx
        self.rdy = rdy
        self.direction = direction
        self.groupe = groupe

    def fdeplacementSoft(self):
        if self.x+self.rdx < 1200 and self.direction == 1:
            self.rdx +=1

        elif self.x+self.rdx == 30 and self.direction == -1:
            self.rdx += 1
            self.groupe.fChangement(1)

        else :
            self.rdx -= 1
            self.groupe.fChangement(-1)

        self.canvas.coords(self.alien,self.x+self.rdx,self.y,self.rdx,self.rdy)
        self.window.after(10,self.fdeplacementSoft)
        return()


