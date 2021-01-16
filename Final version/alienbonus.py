# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 06:39:44 2021

@author: jonat
"""

class AlienBonus():
    """
    Class generating an unique bonus alien
    """
    def __init__(self,canvas,window,y):
        """
        This function creates an unique bonus alien on the right edge of the screen.

        Parameters
        ----------
        canvas : tk.Canvas
            Canvas where the bonus alien is created.
        window : tk.Tk
            Window where the canvas is created.
        y : int
            Ordinate of the bonus alien.

        Returns
        -------
        None.

        """
        self.window = window
        self.canvas = canvas
        
        self.bonus = self.canvas.create_rectangle(1130,y,1200,y+15,fill='red')
        self.canvas.addtag_withtag('bonus',self.bonus) #We give the tag 'bonus' to the alien recognize it later
        
        self.run()
        
    def run(self):
        """
        This function makes the bonus alien move as long as it is in the screen and destroys it if it leaves the screen.

        Returns
        -------
        None.

        """
        if self.canvas.coords(self.canvas.find_withtag('bonus'))!=[]:
            if self.canvas.coords(self.bonus)[0]+70>0:
                self.canvas.coords(self.bonus,self.canvas.coords(self.bonus)[0]-2,self.canvas.coords(self.bonus)[1],self.canvas.coords(self.bonus)[2]-2,self.canvas.coords(self.bonus)[3])
                self.window.after(10,self.run)
        else:
            self.canvas.delete(self.bonus)