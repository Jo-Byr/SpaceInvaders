# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:38:12 2021

@author: jonat
"""

from tkinter import Tk,Label,Button,Canvas
from alien import Alien
from ship import Ship
from ilot import Ilot

tir_in_screen = False

window = Tk()
window.geometry("1200x900")
        
label_score = Label(window, text="Score : 0")
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
ship = Ship(canvas,window)
alien = Alien(canvas,window,5)
alien.run()
        
ilot1 = Ilot(window,canvas,100,700)
ilot2 = Ilot(window,canvas,400,700)
ilot3 = Ilot(window,canvas,700,700)
ilot4 = Ilot(window,canvas,1000,700)
            
window.bind("<KeyPress-Right>",ship.right) 
window.bind("<KeyRelease-Right>",ship.stopright)
window.bind("<KeyPress-Left>",ship.left)
window.bind("<KeyRelease-Left>",ship.stopleft)
window.bind("<KeyPress-space>",ship.tir)
window.mainloop()