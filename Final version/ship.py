# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:36:15 2021

@author: jonat
"""

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
        self.RIGHT = False #Boolean : True while the right arrow is held 
        self.LEFT = False #Boolean : True while the left arrow is held 
        self.TIR = False
        self.lives = 3
        self.player_x = 0 #Abciss of the top-left corner of the ship (a rectangle)
        self.player = self.canvas.create_rectangle(self.player_x,780,self.player_x+60,802,fill='white') #Rectangle standing for the player's ship
        self.canvas.addtag_withtag('ship', self.player) #We give the tag 'ship' to the player's ship to recognize it later
        
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
        if self.RIGHT==False and self.player_x<1140:
            self.RIGHT = True
            self.boucle_right()
        
    def boucle_right(self):
        """
        This function makes the ship move on the right as long as the key is held, with a minimum if instantly released

        Returns
        -------
        None.

        """
        if self.RIGHT == True and self.player_x<1140: #Test of collision with right edge and keyhold
            self.player_x += 5 #Incrementation of player's abciss
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802) #Movement of the ship (rectangle) on the canvas
            self.window.after(10,self.boucle_right) #Recall of this function after 10ms
    
    def stopright(self,event):
        """
        This function stops the continuous right movement when the right arrow is released

        Parameters
        ----------
        event : tkinter.Event
            Event triggering the function (cf. main function).

        Returns
        -------
        None.

        """
        self.RIGHT = False
        
    def left(self,event):
        """
        This function makes the ship intializes a move on the left (continuous if held, elementary if pressed)

        Parameters
        ----------
        event : tkinter.Event
            Event triggering the function (cf. main function).

        Returns
        -------
        None.

        """
        if self.LEFT==False and self.player_x>0:
            self.LEFT = True
            self.boucle_left()
        
    def boucle_left(self):
        """        
        This function makes the ship move on the left as long as the key is held, with a minimum if instantly released


        Returns
        -------
        None.

        """
        if self.LEFT == True and self.player_x>0:#Test of collision with left edge and keyhold
            self.player_x -= 5 #Decrementation of player's abciss
            self.canvas.coords(self.player,self.player_x,780,self.player_x+60,802) #Movement of the ship (rectangle) on the canvas
            self.window.after(10,self.boucle_left) #Recall of this function after 10ms
    
    def stopleft(self,event):
        """
        This function stops the continuous left movement when the right arrow is released

        Parameters
        ----------
        event : tkinter.Event
            Event triggering the function (cf. main function).

        Returns
        -------
        None.

        """
        self.LEFT = False
        
    def tir(self,event):   
        """
        This function initializes a shot from the ship (continuous if held, single if pressed)

        Parameters
        ----------
        event : tkinter.Event
            Event triggering the function (cf. main function).

        Returns
        -------
        None.

        """
        if self.TIR==False:
            self.TIR = True
            self.boucle_tir()
    
    def boucle_tir(self):
        """
        This function keeps creating shots as long the space bar is held

        Returns
        -------
        None.

        """
        if self.TIR == True:#Test of collision with left edge and keyhold
            Shot(self.player_x+27,760,self.canvas,self.window,1)
        
            self.window.after(10,self.boucle_tir) #Recall of this function after 10ms
        
    def stoptir(self,event):
        """
        This function stops the continuous shooting when the spacebar is released

        Parameters
        ----------
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.TIR = False