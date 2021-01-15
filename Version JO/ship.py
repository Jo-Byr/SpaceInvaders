# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:36:15 2021

@author: jonat
"""

from time import time
from shot import Shot

class Ship():
    """
    Class generating the ship commended by the player and handling its controls
    """
    def __init__(self,canvas,window):
        """
        This functions creates the ship commended by the player and the linked variables

        Parameters
        ----------
        canvas : tkinter.Canvas
            Canvas where the ship is created.
        window : tkinter.Tk
            Window where the canvas is created.

        Returns
        -------
        None.

        """
        self.window = window
        self.canvas = canvas
        
        self.T = [[0,time()],[0,time()]] #List of the 2 last inputs and the moment they are done
        self.RIGHT = False #Boolean : True while the right arrow is held 
        self.LEFT = False #Boolean : True while the left arrow is held 
        self.player_x = 0 #Abciss of the top-left corner of the ship (a rectangle)
        self.player = self.canvas.create_rectangle(self.player_x,780,self.player_x+60,802,fill='white') #Rectangle standing for the player's ship
         
    def right(self,event):
        """
        This function makes the ship intializes a move on the right (continuous if held, elementary if pressed)

        Parameters
        ----------
        event : tkinter.Event
            Event triggering the function (cf. main function).

        Returns
        -------
        None.

        """
        self.T[0] = self.T[1] #An input is done, the list is updated
        self.T[1] = [event.keysym,time()]
        if self.RIGHT==False and self.player_x<1140:
            self.RIGHT = True
            self.boucle_right()
        
    def boucle_right(self):
        """
        Cette fonction est celle appelée en boucle afin de maintenir le mouvement vers la droite
        """
        if self.RIGHT == True and self.player_x<1140:
            self.player_x += 5
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
            self.window.after(10,self.boucle_right)
    
    def stopright(self,event):
        """
        Cette fonction premet de cesser le mouvement continu vers la droite lorsque le bouton est relaché
        """
        self.RIGHT = False
        
    def left(self,event):
        """
        Même fonctionnement que la fonction right mais vers la gauche
        """
        self.T[0] = self.T[1]
        self.T[1] = [event.keysym,time()]
        if (self.T[0][0] != self.T[1][0] or self.LEFT==False) and self.player_x>0:
            self.LEFT = True
            self.boucle_left()
        
    def boucle_left(self):
        """ 
        Même fonctionnement que la fonction boucle_right mais vers la gauche
        """
        if self.LEFT == True and self.player_x>0:
            self.player_x -= 5
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802)
            self.window.after(10,self.boucle_left)
    
    def stopleft(self,event):
        """
        Même fonctionnement que la fonction stopleft mais pour la gauche
        """
        self.LEFT = False
        
    def tir(self,event):        
        Shot(self.player_x+27,760,self.canvas,self.window,1)