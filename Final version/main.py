# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:38:12 2021

@author: jonat
"""

"""
Needed changes (in french):
Le random des tirs ennemis peut faire qu'on a des grosses salves ou quasi rien
Le popup de defaite ne stoppe pas la fenêtre
Il faut un message de victoire
"""

from tkinter import Tk,Label,Button,Canvas
from alien import Alien
from ship import Ship
from protection import Protection
    
window = Tk() #Game window
window.geometry("1200x900")
        
label_score = Label(window, text="Score : 0") #Score label
label_score.place(x=10, y=10) 
        
label_vies = Label(window, text="Lives : 3")#Lives label
label_vies.place(x=1130, y=10)
        
canvas = Canvas(window, height = "800", width = "1200", bg='black') #Canvas where the game is displayed
canvas.pack(expand=True)
        
button_new = Button(window, text="New Game", width=15) #New Game button
button_new.place(x=400, y=860)
        
button_quit = Button(window, text="Quit", width=15, command = lambda:window.destroy()) #Quit button
button_quit.place(x=680, y=860)

        
ship = Ship(canvas,window) #Player's ship
alien = Alien(canvas,window,5,3) #Aliens generation
alien.run() #Aliens' movement intialization

#Protections creation        
protection1 = Protection(canvas,window,100,700) 
protection2 = Protection(canvas,window,400,700)
protection3 = Protection(canvas,window,700,700)
protection4 = Protection(canvas,window,1000,700)
      
#Controls binding      
window.bind("<KeyPress-Right>",ship.right) 
window.bind("<KeyRelease-Right>",ship.stopright)
window.bind("<KeyPress-Left>",ship.left)
window.bind("<KeyRelease-Left>",ship.stopleft)
window.bind("<KeyPress-space>",ship.tir)
window.bind("<KeyRelease-space>",ship.stoptir)
window.mainloop()