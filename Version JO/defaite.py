# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:37:53 2021

@author: jonat
"""

from tkinter import Toplevel, Button

class Defaite():
    def __init__(self,window):
        self.window = window
        popup = Toplevel()
        popup.title('Défaite')
        Button(popup,text='Quitter',command=lambda:self.window.destroy()).pack(padx=10,pady=10)
        popup.transient(self.window)
        popup.grab_set()
        self.window.wait_window(popup)