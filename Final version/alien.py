# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 05:40:36 2021

@author: jonat
"""

from random import randint
from end import End
from shot import Shot
from alienbonus import AlienBonus

class Alien():
    """
    Class generating an alien and handling its moves
    """
    def __init__(self,canvas,window,numberx,numbery):
        """
        This function creates a certain number of aliens depending on the parameters.
        There are to 2 types of aliens : passive ones in grey and shooting ones in white

        Parameters
        ----------
        canvas : tkinter.Canvas
            Canvas where the aliens are created.
        window : tk.Tk
            Window where the canvas is created.
        numberx : int
            Number of aliens per row (It varies depending on the consider row between numberx and numberx-1).
        numbery : int
            Number of rows of aliens.

        Returns
        -------
        None.

        """
        self.canvas = canvas
        self.window = window
        
        self.direction = 1 #Variable commending the direction of the aliens : they head to right for 1 and to left for 0
        self.colorlist = ['#00FF00','#A6FF00','#FFFF00','#FF8000','#FF0000'] #List of the colors the protections takes depending on their HP, used for collisions
        self.bonus_passed = 0 #Variable saying if a bonus alien already passed (cf. alienbonus.py), only one can pass per game
        self.list_aliens_x = [] #List of the abciss of all the aliens. This list is not necessary but makes the code clearer
        self.list_aliens_y = [] #List of the ordinate of all the aliens. This list is not necessary but makes the code clearer
        self.list_aliens = [] #List of all aliens
        self.list_shooters = [] #List of all shooting aliens
        
        for j in range(numbery):
            if j%2==0: #There is numberx aliens on even rows and numberx-1 on odd ones
                nx = numberx
            else:
                nx = numberx-1 
            for k in range(nx):
                if randint(0,4)==0: #Each alien as a 1/4 chance to be a shooter
                    X = self.canvas.create_rectangle((k+1)*(1200-nx*100)/(nx+1)+k*100,40*j,(k+1)*(1200-nx*100)/(nx+1)+(k+1)*100,40*j+20, fill='white') #Repartition regulière des aliens
                    self.list_shooters.append(X)
                    self.list_aliens.append(X)
                else:
                    self.list_aliens.append(self.canvas.create_rectangle((k+1)*(1200-nx*100)/(nx+1)+k*100,40*j,(k+1)*(1200-nx*100)/(nx+1)+(k+1)*100,40*j+20, fill='#6e6e6e'))
                self.list_aliens_x.append((k+1)*(1200-nx*100)/(nx+1)+k*100)
                self.list_aliens_y.append(40*j)
            
        for i in self.list_aliens :
            self.canvas.addtag_withtag('alien',i) #We give the tag 'alien' to each created alien to recognize them later
        
        if len(self.list_shooters)<numbery: #We want at least as much shooters as rows
            for k in range(numbery):
                r = randint(0,len(self.list_aliens)-1)
                while r in self.list_shooters: #Verifying if the chosen alien has not already been transformed in a shooter
                    r = randint(0,len(self.list_aliens)-1)
                self.list_shooters.append(self.list_aliens[r])
                self.canvas.itemconfig(self.canvas.find_withtag(self.list_aliens[r]),fill='white')

        for j in self.list_shooters :
            self.canvas.addtag_withtag('shooter',j) #We give the tag 'shooter' to each created alien to recognize them later
            
    def run(self):
        """
        This function makes every alien make en elementary move (+/-2px horizontally or 20px vertically if on the edge of the screen) every 40ms

        Returns
        -------
        None.

        """
        from shot import lost #Putting that at the beginning of the function doesn't work (even with a global)
        
        self.list_aliens_x = []
        self.list_aliens_y = []
        self.list_aliens = []
        self.list_shooters = []
        
        for k in self.canvas.find_withtag('alien'): #Update of the remaining aliens, shooters and their positions
            if self.canvas.coords(k)!=[]:
                self.list_aliens.append(k)
                self.list_aliens_x.append(self.canvas.coords(self.canvas.find_withtag(k))[0])
                self.list_aliens_y.append(self.canvas.coords(self.canvas.find_withtag(k))[1])
                
                if k in self.canvas.find_withtag('shooter'):
                    self.list_shooters.append(k)
        
        for k in self.canvas.find_withtag('protection'):
            overlap = self.canvas.find_overlapping(self.canvas.coords(k)[0], self.canvas.coords(k)[1], self.canvas.coords(k)[2], self.canvas.coords(k)[3])
            for j in overlap:
                if j in self.canvas.find_withtag('alien'):
                    self.canvas.delete(j)
                    if self.canvas.itemcget(self.canvas.find_withtag(k), "fill") in self.colorlist[0:4]: #If the protection has more than 1 HP, we change its color for the next in the list earlier created
                        self.canvas.itemconfig(self.canvas.find_withtag(k),fill=self.colorlist[self.colorlist.index(self.canvas.itemcget(self.canvas.find_withtag(k), "fill"))+1])
                    else:
                        self.canvas.delete(k)
        
        for k in range(0,900,10): #If there's a large enough shooting window, we create a bonus alien
            if self.canvas.find_overlapping(k,0,k+300,600)==() and self.bonus_passed == 0 and max(self.list_aliens_y)<600:
                AlienBonus(self.canvas,self.window,max(self.list_aliens_y)+100)
                self.bonus_passed = 1
        
        for k in self.list_shooters: #Each shooter has a 1/125 chance of shooting at each movement
            if randint(1,20000000)==1:
                Shot(self.canvas.coords(k)[0]+47,self.canvas.coords(k)[1]+45,self.canvas,self.window,0)
        
        if max(self.list_aliens_y) >= 780 : #Collision test with the row of the player
            End(self.window,"Defeat") #If this row is touched, the game is lost and a popup is created
            
        elif self.direction==1: #Move on the right
            if max(self.list_aliens_x)<1100: #Collision test with the right edge of the screen
                self.list_aliens_x = [k+1 for k in self.list_aliens_x]
            else: #When the right edge is touched, every aliens goes down by 20px
                self.direction = -1
                self.list_aliens_y = [k+20 for k in self.list_aliens_y]
        
        elif self.direction == -1: #Move on the left
            if min(self.list_aliens_x)>0: #Collision test with the left edge of the screen
                self.list_aliens_x = [k-1 for k in self.list_aliens_x]
            else: #When the left edge is touched, every aliens goes down by 20px
                self.direction = 1
                self.list_aliens_y = [k+20 for k in self.list_aliens_y]
        
            
        for k in range(len(self.list_aliens)): #Visual move
            self.canvas.coords(self.list_aliens[k],self.list_aliens_x[k],self.list_aliens_y[k],self.list_aliens_x[k]+100,self.list_aliens_y[k]+20)
        
        if lost==False:
            self.window.after(20,self.run) #Recall of the function after 40ms