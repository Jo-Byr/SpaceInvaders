#Header
"""
But : classe d'objet Alien
Auteur : Ankou Pierre-Olivier
date de maj : 18/12/2020
"""

"""
Cette classe cAlien définit la GESTION des aliens.
Chaque objet contient un alien avec ses propriétés.
La définition nécessite 8 paramètre (la fenêtre, le canvas, la coordonnée x et y
la deuxième position x et y et la direction).
Il existe 1 méthode pour le moment : le déplacement qui ne prend aucun arguments
et qui ne retourne rien.
"""

from tkinter import Tk,Canvas

class cAlien():
    def __init__(self,window,canvas1,alien,x,y,rdx,rdy,direction):
        self.window = window
        self.canvas = canvas1
        self.alien = alien
        self.x = x
        self.y = y
        self.rdx = rdx
        self.rdy = rdy
        self.direction = direction

    def fdeplacement(self):
        if self.x+self.rdx < 1200 and self.direction == 1:
            self.rdx +=1

        elif self.x+self.rdx == 30 and self.direction == -1:
            self.rdx += 1
            self.rdy += 30
            self.y += 30
            self.direction = 1

        else :
            self.rdx -= 1
            self.direction =- 1

        self.canvas.coords(self.alien,self.x+self.rdx,self.y,self.rdx,self.rdy)
        self.window.after(10,self.fdeplacement)
        return()
