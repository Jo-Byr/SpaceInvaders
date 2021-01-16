# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:38:04 2021

@author: jonat
"""

class Protection():
    def __init__(self,canvas,window,x,y):
        """
        This function creates a protection for the player : a rectangle with 5HP and a color evoluting with its HP, of given surface 100x30
        5HP : green
        4HP : yellow-green
        3HP : yellow
        2HP : orange
        1HP : red

        Parameters
        ----------
        canvas : tk.Canvas
            Canvas where the protections are created.
        window : tk.Tk
            Window where the canvas is created.
        x : int
            Abciss of the top-left corner of the protection.
        y : int
            Ordinate of the top-left corner of the protection.

        Returns
        -------
        None.

        """
        self.canvas = canvas 
        self.protection = self.canvas.create_rectangle(x,y,x+100,y+30,fill='#00FF00')
        self.canvas.addtag_withtag('protection',self.protection)