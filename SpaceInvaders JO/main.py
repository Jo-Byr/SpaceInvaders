# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 07:55:47 2020

@author: jonat
"""

from tkinter import Tk, Canvas, Button, Label
from aller_retour_vertical import aller_retour_vertical


class SpaceInvaders():
    """
    Classe créant la fenêtre de jeu et ses élements
    """
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x900")
        
        self.label_score = Label(self.window, text="Score : ")
        self.label_score.place(x=10, y=10)
        
        self.label_vies = Label(self.window, text="Vies :")
        self.label_vies.place(x=1130, y=10)
        
        self.button_new = Button(self.window, text="New Game", width=15)
        self.button_new.place(x=400, y=860)
        
        self.button_quit = Button(self.window, text="Quit", width=15, command = lambda:self.window.destroy())
        self.button_quit.place(x=680, y=860)
        
        self.canvas = Canvas(self.window, height = "800", width = "1200", bg='black')
        self.canvas.pack(expand=True)
        
        #Vaisseau et 1er alien
        self.vaisseau = Vaisseau(self.canvas)
        self.alien = Alien(self.canvas,self.window)
        
    
class Alien():
    """
    Classe générant un alien et gérant ses déplacements
    """
    def __init__(self,canvas,window):
        self.canvas = canvas
        self.window = window
        
        self.alien_x = 0
        self.alien_y = 0
        self.direction = 1
        self.alien = self.canvas.create_rectangle(self.alien_x,self.alien_y,self.alien_x+100,self.alien_y+20, fill='white')
    
    def run(self):
        direction = self.direction
        if direction==1:
            if self.alien_x<1100:
                self.alien_x += 1
            else:
                direction = -1
        elif direction == -1:
            if self.alien_x>0:
                self.alien_x -= 1
            else:
                direction = 1
        self.canvas.coords(self.alien,self.alien_x,self.alien_y,self.alien_x+100,self.alien_y+20)
        self.window.after(20,aller_retour_vertical,self.window,self.canvas,self.alien,self.alien_x,self.alien_y,direction)
        #Faut se débarasser de la fonction
    

class Vaisseau():
    """
    Classe générant le vaisseau et gérant ses dépalcements
    """
    def __init__(self,canvas):
        self.canvas = canvas
        
        self.player_x = 0
        self.player = self.canvas.create_rectangle(self.player_x,780,self.player_x+60,802,fill='white')
        
    def event_handler(self,event):
        if event.keysym == 'Right':
            self.move(True)
        elif event.keysym == 'Left':
            self.move(False)
        elif event.keysym == "space":
            self.tir()
            
        
    def move(self,right):
        if right and self.player_x<1140:
            self.player_x += 10
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
        elif not right and self.player_x>0:
            self.player_x -= 10
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
    
    def tir(self):
        self.canvas.create_rectangle(self.player_x+27,760,self.player_x+33,775,fill="white")
     
            
game = SpaceInvaders()
game.alien.run()
game.window.bind("<KeyPress>",game.vaisseau.event_handler) #soit le vaisseau tire, soit il se déplace faut corriger ca
game.window.mainloop()