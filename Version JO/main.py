# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:24:39 2021

@author: jonat
"""

from tkinter import Tk, Canvas, Button, Label, Toplevel
from time import time
from random import randint

"""
Parfois il est possible de lancer 2 tirs (presque) à la fois
Les aliens ne tirent pas
"""
    
T = [[0,time()],[0,time()]]
RIGHT = False
LEFT = False
tir_in_screen = False
PERDU = False
VIES = 3
 
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
        
        
        Tir(self.player_x+27,760,self.canvas,self.window,1)

liste_aliens = []
liste_aliens_x = []
liste_aliens_y = []
class Alien():
    """
    Classe générant un alien et gérant ses déplacements
    """
    def __init__(self,canvas,window,number):
        #Création d'un alien et des variables associées
        self.canvas = canvas
        self.window = window
        
        self.direction = 1
        
        global liste_aliens_x,liste_aliens_y
        
        for k in range(number):
            liste_aliens.append(self.canvas.create_rectangle(200*k,0,200*k+100,20, fill='white'))
            liste_aliens_x.append(200*k)
            liste_aliens_y.append(0)
            
    def run(self):
        global liste_aliens_x,liste_aliens_y,PERDU
        direction = self.direction #Variable disant si l'alien doit aller à droite (1) ou à gauche (0)
        if liste_aliens_x[0] >= 780 :
            #Test de collision avec le joueur
            PERDU = True #Décelenche un popup
            Defaite(self.window)
        elif direction==1:
            #Déplacement à droite
            if liste_aliens_x[-1]<1100:
                #Test de collision avec le bord de l'écran
                liste_aliens_x = [k+4 for k in liste_aliens_x]
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = -1
                liste_aliens_y = [k+25 for k in liste_aliens_y]
        elif direction == -1:
            #Déplacement à gauche
            if liste_aliens_x[0]>0:
                #Test de collision avec le bord de l'écran
                liste_aliens_x = [k-4 for k in liste_aliens_x]
            else:
                #Au contact du bord de l'écran, l'alien descend d'un cran
                self.direction = 1
                liste_aliens_y = [k+25 for k in liste_aliens_y]
        if PERDU == False:
            #Déplacement visuel
            for k in range(len(liste_aliens)):
                self.canvas.coords(liste_aliens[k],liste_aliens_x[k],liste_aliens_y[k],liste_aliens_x[k]+100,liste_aliens_y[k]+20)
            self.window.after(40,self.run)  #La méthode after semble retourner une erreur à 13 chiffres
            
            
    def tir(self):
        #Création d'un tir ennemi
        Tir(self.alien_x+47, self.alien_y + 40, self.canvas, self.window, 0)


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
        
        global tir_in_screen
        
        if (self.camp==1 and tir_in_screen==False) or self.camp==0:
            tir_in_screen = True
            self.tir = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="white")
        
            self.window.after(100,self.complete_move)
    
    def simple_move(self):
        """
        Cette fonction effectue un "déplacement élementaire" d'un tir
        """
        global PERDU
        if PERDU == False:
            if self.camp == 1:
                self.y -= 5
            else:
                self.y += 5
            self.canvas.coords(self.tir,self.x,self.y,self.x+6,self.y+15)
            self.complete_move() #fonction pseudo récursive
    
    def complete_move(self):
        """
        Cette fonction appelle la fonction simple_move en boucle tant que le bord de l'écran n'est pas atteint et teste les collisions
        """
        
        global tir_in_screen
        global liste_aliens
        if self.x+6>100 and self.x<200 and self.y<730 and self.y+15>700 and ilot1.vies!=0:
            #Test de contact de l'ilot 1
            if ilot1.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot1.vies -= 1
                
                if ilot1.vies == 4:
                    self.canvas.itemconfig(ilot1.ilot,fill='#A6FF00')
                elif ilot1.vies == 3:
                    self.canvas.itemconfig(ilot1.ilot,fill='#FFFF00')
                elif ilot1.vies == 2:
                    self.canvas.itemconfig(ilot1.ilot,fill='#FF8000')
                else:
                    self.canvas.itemconfig(ilot1.ilot,fill='#FF0000')
            elif ilot1.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot1.vies -= 1
                self.canvas.delete(ilot1.ilot)
        elif self.x+6>400 and self.x<500 and self.y<730 and self.y+15>700 and ilot2.vies!=0:
            #Test de contact de l'ilot 2
            if ilot2.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot2.vies -= 1
                
                if ilot2.vies == 4:
                    self.canvas.itemconfig(ilot2.ilot,fill='#A6FF00')
                elif ilot2.vies == 3:
                    self.canvas.itemconfig(ilot2.ilot,fill='#FFFF00')
                elif ilot2.vies == 2:
                    self.canvas.itemconfig(ilot2.ilot,fill='#FF8000')
                else:
                    self.canvas.itemconfig(ilot2.ilot,fill='#FF0000')
            elif ilot2.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot2.vies -= 1
                self.canvas.delete(ilot2.ilot)
        elif self.x+6>700 and self.x<800 and self.y<730 and self.y+15>700 and ilot3.vies!=0:
            #Test de contact de l'ilot 3
            if ilot3.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot3.vies -= 1
                
                if ilot3.vies == 4:
                    self.canvas.itemconfig(ilot3.ilot,fill='#A6FF00')
                elif ilot3.vies == 3:
                    self.canvas.itemconfig(ilot3.ilot,fill='#FFFF00')
                elif ilot3.vies == 2:
                    self.canvas.itemconfig(ilot3.ilot,fill='#FF8000')
                else:
                    self.canvas.itemconfig(ilot3.ilot,fill='#FF0000')
            elif ilot3.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot3.vies -= 1
                self.canvas.delete(ilot3.ilot)
        elif self.x+6>1000 and self.x<1100 and self.y<730 and self.y+15>700 and ilot4.vies!=0:
            #Test de contact de l'ilot 4
            if ilot4.vies>1:
                #Si il ne disparait pas avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot4.vies -= 1
                
                if ilot4.vies == 4:
                    self.canvas.itemconfig(ilot4.ilot,fill='#A6FF00')
                elif ilot4.vies == 3:
                    self.canvas.itemconfig(ilot4.ilot,fill='#FFFF00')
                elif ilot4.vies == 2:
                    self.canvas.itemconfig(ilot4.ilot,fill='#FF8000')
                else:
                    self.canvas.itemconfig(ilot4.ilot,fill='#FF0000')
            elif ilot4.vies == 1:
                #S'il disparaît avec ce coup
                self.canvas.delete(self.tir)
                
                if self.camp==1:
                    tir_in_screen = False
                
                ilot4.vies -= 1
                self.canvas.delete(ilot4.ilot)
        elif self.camp == 1:
            #Tir provenant du vaisseau
            k=0
            while k<len(liste_aliens):
                if self.x+6>=liste_aliens_x[k] and self.x<=liste_aliens_x[k]+100:
                    if self.y+15>=liste_aliens_y[k] and self.y<=liste_aliens_y[k]+20:
                        self.canvas.delete(self.tir)
                        tir_in_screen = False
                        self.canvas.delete(liste_aliens[k])
                        liste_aliens.remove(liste_aliens[k])
                        liste_aliens_x.remove(liste_aliens_x[k])
                        liste_aliens_y.remove(liste_aliens_y[k])
                        break
                k+=1
            if self.y>=-15: #vérification que le bord de l'écran n'est pas atteint
                    self.window.after(50, self.simple_move) #minimisation du temps entre deux déplacements
                     
            else: #si l'élement sort du canvas on le supprime afin de ne pas gérer les déplacements d'élements non visibles
                    self.canvas.delete(self.tir)
                    tir_in_screen = False
        else :
            #Tir provenant de l'alien
            if (self.y+15>=785) and (self.x +6 >= vaisseau.player_x) and (self.x <= vaisseau.player_x + 60):
                #Test de collision avec le vaisseau
                self.canvas.delete(self.tir)
                global VIES
                VIES -= 1
                label_vies['text'] = "Vies : " + str(VIES)
                if VIES == 0:
                    global PERDU
                    PERDU = True
                    Defaite(self.window)
            elif self.y<=800:
                #Test de sortie d'écran
                self.window.after(50, self.simple_move)
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
        self.ilot = self.canvas.create_rectangle(x,y,x+100,y+30,fill='#00FF00')
        self.vies = 5
        
window = Tk()
window.geometry("1200x900")
        
label_score = Label(window, text="Score : ")
label_score.place(x=10, y=10)
        
label_vies = Label(window, text="Vies : 3")
label_vies.place(x=1130, y=10)
        
button_new = Button(window, text="New Game", width=15)
button_new.place(x=400, y=860)
        
button_quit = Button(window, text="Quit", width=15, command = lambda:window.destroy())
button_quit.place(x=680, y=860)
        
canvas = Canvas(window, height = "800", width = "1200", bg='black')
canvas.pack(expand=True)
        
#Vaisseau et 1er alien
vaisseau = Vaisseau(canvas,window)
alien = Alien(canvas,window,5)
alien.run()
        
ilot1 = Ilot(window,canvas,100,700)
ilot2 = Ilot(window,canvas,400,700)
ilot3 = Ilot(window,canvas,700,700)
ilot4 = Ilot(window,canvas,1000,700)
            
window.bind("<KeyPress-Right>",vaisseau.right) 
window.bind("<KeyRelease-Right>",vaisseau.stopright)
window.bind("<KeyPress-Left>",vaisseau.left)
window.bind("<KeyRelease-Left>",vaisseau.stopleft)
window.bind("<KeyPress-space>",vaisseau.tir)
window.mainloop()