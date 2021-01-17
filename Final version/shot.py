# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 05:09:03 2021

@author: jonat
"""

from time import time
from end import End
from tkinter import TclError

lost = False #Variable shared with alien.py, when True the game is freezed (enabled on defeat)
timer = 0 #Variable saving the date of the player's last shot
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
            self.shot = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="#ff9900") #Player's shots are orange
            self.canvas.addtag_withtag('shot',self.shot) #We give the tag 'shot' to the element to recognize it later
            self.complete_move() #Collision test
        
        elif self.camp==0:
            self.shot = self.canvas.create_rectangle(self.x,self.y,self.x+6,self.y+15,fill="#4287f5") #Aliens' shots are blue
            self.complete_move() #Collision test
        
    
    def simple_move(self):
        """
        This function makes the initialized shot make an elementary move (5px)

        Returns
        -------
        None.

        """
        if self.camp == 1: #The player's shots go up vertically
            self.y -= 1
        else: #The aliens' shots go down vertically
            self.y += 1
        self.canvas.coords(self.shot,self.x,self.y,self.x+6,self.y+15)
        if (self.camp == 0 and self.y<800) or (self.camp == 1 and self.y>0): #Out of the screen test
            self.complete_move() #Call of the function handling collisions
        else: #If out of the screent he shot is deleted
            self.canvas.delete(self.shot)
    
    def complete_move(self):
        """
        This function tests collisions between the shot and other canvas elements

        Returns
        -------
        None.

        """
        overlap = self.canvas.find_overlapping(self.x,self.y,self.x+6,self.y+15) #Tuple of the canvas ID of the overlapping elements
        if len(overlap)>1: #If there is an overlapping            
            for j in overlap:
                if j in self.canvas.find_withtag('protection'):
                    if self.canvas.itemcget(self.canvas.find_withtag(j), "fill") != self.colorlist[-1]: #If the protection has more than 1 HP, we change its color for the next in the list earlier created
                        self.canvas.itemconfig(self.canvas.find_withtag(j),fill=self.colorlist[self.colorlist.index(self.canvas.itemcget(self.canvas.find_withtag(j), "fill"))+1])
                    
                    else: #If the protection has 1 HP when touched, it's destroyed
                        self.canvas.delete(j)
                    self.canvas.delete(self.shot)
                    break
                elif j in self.canvas.find_withtag('ship'):
                    self.canvas.delete(self.shot)
                    for k in self.window.winfo_children(): #Search for the lives label in all of the window's widgets
                        try:
                            if k['text'][0:8]=="Lives : ":
                                k['text'] = "Lives : " + str(int(k['text'][7:])-1)
                                if int(k['text'][8:])==0:
                                    global lost
                                    lost = True
                                    End(self.window,"Defeat") #If lives fall to 0, a defeat popup is generated
                        except TclError:True
                    break
                else: #Non-protections elements (Aliens and aliens' shots) have 1HP, and so are destroyed when colliding with one of the player's shots
                    if (j in self.canvas.find_withtag('alien') or j in self.canvas.find_withtag('bonus')) and self.camp==1: #If one of the player's shots touch an alien or a bonus alien
                        for k in self.window.winfo_children(): #Search for the score label in all of the window's widgets
                            try:
                                if k['text'][0:8]=="Score : ": #Score incrementation
                                    if j in self.canvas.find_withtag('shooter'):
                                        k['text'] = "Score : " + str(int(k['text'][8:])+25)
                                    elif j in self.canvas.find_withtag('bonus'):
                                        k['text'] = "Score : " + str(int(k['text'][8:])+150)
                                    else:
                                        k['text'] = "Score : " + str(int(k['text'][8:])+10)
                            
                            except TclError:True
                        self.canvas.delete(j) #Deletes the element
                        self.canvas.delete(self.shot) #Deletes the shot
                        if self.canvas.find_withtag('alien')==():
                            lost=True
                            End(self.window,"Victory")
                        break
        if lost==False:
            self.window.after(10, self.simple_move)