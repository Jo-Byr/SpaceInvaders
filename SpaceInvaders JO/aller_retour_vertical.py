# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:06:36 2020

@author: jonat
"""


def aller_retour_vertical(window,canvas,rect,x,y,direction):
    if direction==1:
        if y<780:
            y += 1
        else:
            direction = -1
    elif direction == -1:
        if y>0:
            y -= 1
        else:
            direction = 1
    canvas.coords(rect,x,y,x+100,y+20)
    window.after(20,aller_retour_vertical,window,canvas,rect,x,y,direction)