# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:36:43 2021

@author: jonat
"""

from random import randint
from defaite import Defaite
from shot import Shot

class Alien():
    """
    Classe générant un alien et gérant ses déplacements
    """
    def __init__(self,canvas,window,number):
        #Création d'un alien et des variables associées
        self.canvas = canvas
        self.window = window
        
        self.direction = 1
        
        self.liste_aliens_x = []
        self.liste_aliens_y = []
        self.liste_aliens = []
        
        for k in range(number):
            self.liste_aliens.append(self.canvas.create_rectangle(200*k,0,200*k+100,20, fill='white'))
            self.liste_aliens_x.append(200*k)
            self.liste_aliens_y.append(0)
            
    def run(self):
        self.liste_aliens_x = []
        self.liste_aliens_y = []
        self.liste_aliens = []
        for k in range(2,7):
            if self.canvas.coords(k)!=[]:
                self.liste_aliens.append(k)
                self.liste_aliens_x.append(self.canvas.coords(self.canvas.find_withtag(k))[0])
                self.liste_aliens_y.append(self.canvas.coords(self.canvas.find_withtag(k))[1])
        for k in range(len(self.liste_aliens_x)):
            if randint(1,300)==1:
                Shot(self.liste_aliens_x[k]+47,self.liste_aliens_y[k]+45,self.canvas,self.window,0)
        direction = self.direction #Variable disant si l'alien doit aller à droite (1) ou à gauche (0)
        if self.liste_aliens_y[0] >= 780 :
            #Test de collision avec le joueur
            Defaite(self.window)
            
        elif direction==1:
            #Déplacement à droite
            if self.liste_aliens_x[-1]<1100:
                #Test de collision avec le bord de l'écran
                self.liste_aliens_x = [k+4 for k in self.liste_aliens_x]
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = -1
                self.liste_aliens_y = [k+25 for k in self.liste_aliens_y]
        elif direction == -1:
            #Déplacement à gauche
            if self.liste_aliens_x[0]>0:
                #Test de collision avec le bord de l'écran
                self.liste_aliens_x = [k-4 for k in self.liste_aliens_x]
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = 1
                self.liste_aliens_y = [k+25 for k in self.liste_aliens_y]
        
            #Déplacement visuel
        for k in range(len(self.liste_aliens)):
            self.canvas.coords(self.liste_aliens[k],self.liste_aliens_x[k],self.liste_aliens_y[k],self.liste_aliens_x[k]+100,self.liste_aliens_y[k]+20)
        self.window.after(40,self.run)  #La méthode after semble retourner une erreur à 13 chiffres