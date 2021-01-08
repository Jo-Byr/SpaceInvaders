# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:12:26 2021

@author: jonat
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:24:38 2020

@author: bouye
"""

from tkinter import Tk, Canvas, Button, Label, Toplevel
from time import time
from random import randint

"""
Version irrégulière
"""
    
T = [[0,time()],[0,time()]]
RIGHT = False
LEFT = False
TIR = False
PERDU = False
VIES = 3

class SpaceInvaders():
    """
    Classe créant la fenêtre de jeu et ses élements
    """
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x900")
        
        self.label_score = Label(self.window, text="Score : ")
        self.label_score.place(x=10, y=10)
        
        self.label_vies = Label(self.window, text="Vies : 3")
        self.label_vies.place(x=1130, y=10)
        
        self.button_new = Button(self.window, text="New Game", width=15)
        self.button_new.place(x=400, y=860)
        
        self.button_quit = Button(self.window, text="Quit", width=15, command = lambda:self.window.destroy())
        self.button_quit.place(x=680, y=860)
        
        self.canvas = Canvas(self.window, height = "800", width = "1200", bg='black')
        self.canvas.pack(expand=True)
        
        #Vaisseau et 1er alien
        self.vaisseau = Vaisseau(self.canvas,self.window)
        self.alien = Alien(self.canvas,self.window)
        
        self.ilot1 = Ilot(self.window,self.canvas,100,700)
        self.ilot2 = Ilot(self.window,self.canvas,400,700)
        self.ilot3 = Ilot(self.window,self.canvas,700,700)
        self.ilot4 = Ilot(self.window,self.canvas,1000,700)
    
class Alien():
    """
    Classe générant un alien et gérant ses déplacements
    """
    def __init__(self,canvas,window):
        #Création d'un alien et des variables associées
        self.canvas = canvas
        self.window = window
        
        self.dead = 0
        self.alien_x = 0
        self.alien_y = 0
        self.direction = 1
        self.alien = self.canvas.create_rectangle(self.alien_x,self.alien_y,self.alien_x+100,self.alien_y+20, fill='white')
    
    def run(self):
        #Fonction de déplacement
        global PERDU
        if self.dead == 0:
            #Si l'alien n'est pas mort, il tire aléatoirement (2% de chance à chaque déplacement)
            rand_tir = randint(0,49)
            if rand_tir == 0:
                self.tir()
        direction = self.direction #Variable disant si l'alien doit aller à droite (1) ou à gauche (0)
        if self.alien_y >= 780 :
            #Test de collision avec le joueur
            PERDU = True #Décelenche un popup
            Defaite(self.window)
        elif direction==1:
            #Déplacement à droite
            if self.alien_x<1100:
                #Test de collision avec le bord de l'écran
                self.alien_x += 10
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = -1
                self.alien_y += 20
        elif direction == -1:
            #Déplacement à gauche
            if self.alien_x>0:
                #Test de collision avec le bord de l'écran
                self.alien_x -= 10
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = 1
                self.alien_y += 20
        if PERDU == False:
            #Déplacement visuel
            self.canvas.coords(self.alien,self.alien_x,self.alien_y,self.alien_x+100,self.alien_y+20)
            self.window.after(40,self.run)  #La méthode after semble retourner une erreur à 13 chiffres
            
            
    def tir(self):
        #Création d'un tir ennemi
        Tir(self.alien_x+47, self.alien_y + 40, self.canvas, self.window, 0)

class Vaisseau():
    """
    Classe générant le vaisseau et gérant ses déplacements
    """
    def __init__(self,canvas,window):
        self.window = window
        self.canvas = canvas
        
        self.player_x = 0
        self.player = self.canvas.create_rectangle(self.player_x,780,self.player_x+60,802,fill='white')
         
    def right(self,event):
        """
        Cette fonction permet un déplacement à droite et initialise un déplacement continue vers la droite si le bouton est maitnenue
        """
        global RIGHT
        T[0] = T[1]
        T[1] = [event.keysym,time()]
        if (T[0][0] != T[1][0] or RIGHT==False) and self.player_x<1140:
            RIGHT = True
            self.boucle_right()
        
    def boucle_right(self):
        """
        Cette fonction est celle appelée en boucle afin de maintenir le mouvement vers la droite
        """
        if RIGHT == True and self.player_x<1140:
            self.player_x += 5
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
            self.window.after(10,self.boucle_right)
    
    def stopright(self,event):
        """
        Cette fonction premet de cesser le mouvement continu vers la droite lorsque le bouton est relaché
        """
        global RIGHT
        RIGHT = False
        
    def left(self,event):
        """
        Même fonctionnement que la fonction right mais vers la gauche
        """
        global LEFT
        T[0] = T[1]
        T[1] = [event.keysym,time()]
        if (T[0][0] != T[1][0] or LEFT==False) and self.player_x>0:
            LEFT = True
            self.boucle_left()
        
    def boucle_left(self):
        """ 
        Même fonctionnement que la fonction boucle_right mais vers la gauche
        """
        if LEFT == True and self.player_x>0:
            self.player_x -= 5
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
            self.window.after(10,self.boucle_left)
    
    def stopleft(self,event):
        """
        Même fonctionnement que la fonction stopleft mais pour la gauche
        """
        global LEFT
        LEFT = False
        
    def tir(self,event):
        """
        Cette fonction permet un déplacement à droite et initialise un déplacement continue vers la droite si le bouton est maitnenue
        """
        
        global TIR
        T[0] = T[1]
        T[1] = [event.keysym,time()]
        if (T[0][0] != T[1][0] or TIR==False):
            TIR = True
            self.boucle_tir()
        
    def boucle_tir(self):
        """
        Cette fonction est celle appelée en boucle afin de maintenir le mouvement vers la droite
        """
        if TIR == True:
            Tir(self.player_x+27,760,self.canvas,self.window,1)
            self.window.after(150,self.boucle_tir)
    
    def stoptir(self,event):
        """
        Cette fonction premet de cesser le mouvement continu vers la droite lorsque le bouton est relaché
        """
        global TIR
        TIR = False
        
class Tir():
    """
    Classe générant les tirs et gérant leurs déplacements
    """
    def __init__(self,x,y,canvas,window,camp):
        self.x = x
        self.y = y
        self.camp = camp
        self.canvas = canvas
        self.window = window
        
        self.tir = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="white")
        
        self.window.after(100,self.complete_move)
    
    def simple_move(self):
        """
        Cette fonction effectue un "déplacement élementaire" d'un tir
        """
        global PERDU
        if PERDU == False:
            if self.camp == 1:
                self.y -= 1
            else:
                self.y += 1
            self.canvas.coords(self.tir,self.x,self.y,self.x+6,self.y+15)
            self.complete_move() #fonction pseudo récursive
    
    def complete_move(self):
        """
        Cette fonction appelle la fonction simple_move en boucle tant que le bord de l'écran n'est pas atteint et teste les collisions
        """
        if self.x+6>100 and self.x<200 and self.y<730 and self.y+15>700 and game.ilot1.vies!=0:
            #Test de contact de l'ilot 1
            if game.ilot1.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                game.ilot1.vies -= 1
            elif game.ilot1.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                game.ilot1.vies -= 1
                self.canvas.delete(game.ilot1.ilot)
        elif self.x+6>400 and self.x<500 and self.y<730 and self.y+15>700 and game.ilot2.vies!=0:
            #Test de contact de l'ilot 2
            if game.ilot2.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                game.ilot2.vies -= 1
            elif game.ilot2.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                game.ilot2.vies -= 1
                self.canvas.delete(game.ilot2.ilot)
        elif self.x+6>700 and self.x<800 and self.y<730 and self.y+15>700 and game.ilot3.vies!=0:
            #Test de contact de l'ilot 3
            if game.ilot3.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                game.ilot3.vies -= 1
            elif game.ilot3.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                game.ilot3.vies -= 1
                self.canvas.delete(game.ilot3.ilot)
        elif self.x+6>1000 and self.x<1100 and self.y<730 and self.y+15>700 and game.ilot4.vies!=0:
            #Test de contact de l'ilot 4
            if game.ilot4.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                game.ilot4.vies -= 1
            elif game.ilot4.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                game.ilot4.vies -= 1
                self.canvas.delete(game.ilot4.ilot)
        elif self.camp == 1:
            #Tir provenant du vaisseau
            if game.alien.dead == 0 and (self.y<=game.alien.alien_y+20) and (self.y+15>=game.alien.alien_y) and (self.x+6>=game.alien.alien_x) and (self.x<=game.alien.alien_x+100):
                #Test de collision avec l'alien
                self.canvas.delete(self.tir)
                self.canvas.delete(game.alien.alien)
                game.alien.dead = 1
            elif self.y>=-15: #vérification que le bord de l'écran n'est pas atteint
                self.window.after(4, self.simple_move) #minimisation du temps entre deux déplacements
            else: #si l'élement sort du canvas on le supprime afin de ne pas gérer les déplacements d'élements non visibles
                self.canvas.delete(self.tir)
        else :
            #Tir provenant de l'alien
            if (self.y+15>=785) and (self.x +6 >= game.vaisseau.player_x) and (self.x <= game.vaisseau.player_x + 60):
                #Test de collision avec le vaisseau
                self.canvas.delete(self.tir)
                global VIES
                VIES -= 1
                game.label_vies['text'] = "Vies : " + str(VIES)
                if VIES == 0:
                    global PERDU
                    PERDU = True
                    Defaite(self.window)
            elif self.y<=800:
                #Test de sortie d'écran
                self.window.after(4, self.simple_move)
            else:
                self.canvas.delete(self.tir)

class Defaite():
    def __init__(self,window):
        self.window = window
        popup = Toplevel()
        popup.transient(self.window)
        
class Ilot():
    def __init__(self,window,canvas,x,y):
        self.canvas = canvas 
        self.ilot = self.canvas.create_rectangle(x,y,x+100,y+30,fill='white')
        self.vies = 5
        
            
game = SpaceInvaders()
game.alien.run()
game.window.bind("<KeyPress-Right>",game.vaisseau.right) 
game.window.bind("<KeyRelease-Right>",game.vaisseau.stopright)
game.window.bind("<KeyPress-Left>",game.vaisseau.left)
game.window.bind("<KeyRelease-Left>",game.vaisseau.stopleft)
game.window.bind("<KeyPress-space>",game.vaisseau.tir)
game.window.bind("<KeyRelease-space>",game.vaisseau.stoptir)
game.window.mainloop()