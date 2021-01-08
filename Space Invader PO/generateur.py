#Header
"""
But : Fonction qui génère régulièrement des aliens
Auteur : Ankou Pierre-Olivier
Date de maj : 08/01/2021
"""

"""
Cette fonction reçoit la fenêtre et le canvas en paramètre.
Cette fonction procède de la manière suivante:
    1-créer une taille fixe d'alien.
    2-créer une position de départ de l'alien aléatoire en x et fixe en y
    3-donne un direction fixe
    4-créer un objet cAlien dans un intervalle de temps.
    5-Ajoute l'alien dans un objet représentant un groupe d'aliens
    6-calcul des probabilité pour savoir quelles seront les prochains ennemis
    à apparaitre.
Cette fonction ne retourne rien.
"""

from random import randint
from tkinter import Tk,Canvas
from classAlien import cAlien
from classGrpAlien import cGrpAlien



def fgenerateur(window,canvas1,mode,numéro=1):

    if mode == 0:
        #positions
        L = [100,200,300,400,500,600,700,800,900,1000,1100]
        rdy = 2
        #dimensions
        x = 30
        y = 30
        #direction initiale
        direction = 1
        Grp = 'groupe' + str(numéro)
        Grp = cGrpAlien()

        for i in range(randint(4,6)):
            p = randint(0,len(L)-1)
            rdx = L[p]
            L.remove(L[p])

            alien = canvas1.create_rectangle(x-rdx,y-rdy,rdx,rdy,outline = 'black',fill = 'green')
            Alien = cAlien(window,canvas1,alien,x,y,rdx,rdy,direction,Grp)
            Alien.fdeplacementSoft()
            Grp.Ajout(Alien)

        #préparation du deuxième groupe (temps d'appartition, adversaire)
        numéro += 1
        proba_apparition = randint(50,100)/100
        if proba_apparition > 0.50:
            mode = 1
            intervalle = randint(30000,35000)
        else:
            intervalle = randint(20000,30000)

        window.after(intervalle,lambda:fgenerateur(window,canvas1,mode,numéro))
        return()



    elif mode == 1:
         #positions
        L = [200,600,900]
        rdy = 2
        #dimensions
        x = 40
        y = 70
        #direction initiale
        direction = 1
        Grp = 'groupe' + str(numéro)
        Grp = cGrpAlien()

        for i in range(randint(1,3)):
            p = randint(0,len(L)-1)
            rdx = L[p]
            L.remove(L[p])

            alien = canvas1.create_rectangle(x-rdx,y-rdy,rdx,rdy,outline = 'black',fill = 'green')
            Alien = cAlien(window,canvas1,alien,x,y,rdx,rdy,direction,Grp)
            Alien.fdeplacementSoft()
            Grp.Ajout(Alien)

        #préparation du deuxième groupe (temps d'appartition, adversaire)
        numéro += 1
        intervalle = randint(20000,30000)

        proba_apparition = randint(1,50)/100
        if proba_apparition < 0.5:
            mode = 0
            intervalle = randint(20000,30000)
        else:
            intervalle = randint(30000,35000)

        window.after(intervalle,lambda:fgenerateur(window,canvas1,mode,numéro))
        return()