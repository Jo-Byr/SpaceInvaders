# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:37:10 2021

@author: jonat
"""

from time import time

timer = 0 #Variable contenant la mesure de temps du dernier tir effectué
class Shot():
    """
    Class generating a shot from an alien or the player, moves it and handles its collisions
    """
    def __init__(self,x,y,canvas,window,camp):
        """
        This function initializes a shot either from an alien or the player depending on the input camp

        Parameters
        ----------
        x : int
            Abciss of the top-left corner of the shot (rectangle).
        y : int
            Ordinate of the top-left corner of the shot (rectangle)..
        canvas : tkinter.Canvas
            Canvas where the shot is created.
        window : tkinter.Tk
            Window where the canvas is created.
        camp : int (0 or 1)
            Camp of the shot : 1 for Ally and 0 for Alien.

        Returns
        -------
        None.

        """
        
        self.x = x
        self.y = y
        self.camp = camp
        self.canvas = canvas
        self.window = window
        
        global timer
        self.colorlist = ['#00FF00','#A6FF00','#FFFF00','#FF8000','#FF0000'] #List of the colors the protections takes depending on their HP
        if self.camp==1 and time() - timer>2: #Limitation of one shot every 2 seconds for the player
            timer = time()
            self.tir = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="#ff9900") #Player's shots are orange
            self.complete_move()
        
        elif self.camp==0:
            self.tir = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="#4287f5") #Aliens' shots are blue
            self.complete_move()
    
    def simple_move(self):
        """
        This function makes the initialized shot make an elementary move (5px)

        Returns
        -------
        None.

        """
        
        if self.camp == 1:
            self.y -= 5
        else:
            self.y += 5
        self.canvas.coords(self.tir,self.x,self.y,self.x+6,self.y+15)
        if (self.camp == 0 and self.y<800) or (self.camp == 1 and self.y>0):
            self.complete_move() #Call of the function handling collisions
        else:
            self.canvas.delete(self.tir)
    
    def complete_move(self):
        """
        This function tests collisions between the shot and other canvas elements

        Returns
        -------
        None.

        """
       
        self.window.after(50, self.simple_move)
        overlap = self.canvas.find_overlapping(self.x,self.y,self.x+6,self.y+15) #Tuple of the canvas ID of the overlapping elements
        if len(overlap)>1:
            self.canvas.delete(self.tir) #Whenever it touches any element from the canvas, the shot is deleted
            for j in overlap:
                if j in range(7,11): #Elements 7 to 10 (included) are the protections, which have 5 HP
                    if self.canvas.itemcget(self.canvas.find_withtag(j), "fill") != self.colorlist[-1]: #If the protection has more than 1 HP, we change its color for the next in the list earlier
                        self.canvas.itemconfig(self.canvas.find_withtag(j),fill=self.colorlist[self.colorlist.index(self.canvas.itemcget(self.canvas.find_withtag(j), "fill"))+1])
                    else: #If the protection has 1 HP when touched, it's destroyed
                        self.canvas.delete(j)
                else: #Non-protections elements (Aliens and aliens' shots) have 1HP, and so are destroyed when colliding with one of the player's shots
                    self.canvas.delete(j)