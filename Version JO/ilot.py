# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:38:04 2021

@author: jonat
"""

class Ilot():
    def __init__(self,window,canvas,x,y):
        self.canvas = canvas 
        self.ilot = self.canvas.create_rectangle(x,y,x+100,y+30,fill='#00FF00')
        self.vies = 5