#Header
"""
But : Fonction qui génère régulièrement des aliens
Auteur : Ankou Pierre-Olivier
Date de maj : 18/12/2020
"""

"""
Cette fonction reçoit la fenêtre et le canvas en paramètre.
Cette fonction procède de la manière suivante:
    1-créer une taille fixe d'alien.
    2-créer une position de départ de l'alien aléatoire en x et fixe en y
    3-donne un direction fixe
    4-créer un objet cAlien dans un intervalle de temps [900,10000]ms.
Cette fonction ne retourne rien.
"""

from random import randint

from tkinter import Tk,Canvas

from classAlien import cAlien

def fgenerateur(window,canvas1):
    x = 30
    y = 30
    rdx = randint(2,1100)
    rdy = 2
    direction = 1

    nb = randint(900,10000)
    alien = canvas1.create_rectangle(x-rdx,y-rdy,rdx,rdy,outline = 'black',fill = 'green')
    cAlien(window,canvas1,alien,x,y,rdx,rdy,direction).fdeplacement()
    window.after(nb,lambda:fgenerateur(window,canvas1))
    return()