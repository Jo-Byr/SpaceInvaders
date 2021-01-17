# -*- coding: utf-8 -*-
#Header
"""
But: écran de défaite
Auteur :  Jonathan Bouyer & Pierre-Olivier Ankou
Date de maj : 17/01/2020
"""

from tkinter import Toplevel, Button,Label

class Defeat():
    """
    Class generating a popup when the game is lost
    """
    def __init__(self,window,text):
        """
        This function creates a popup when the game is lost

        Parameters
        ----------
        window : tk.Tk
            Main window from which the popup is created.

        Returns
        -------
        None.

        """

        popup = Toplevel() #Popup above the main window
        popup.geometry("300x150")
        popup.title(text)
        if text=="Defeat":
            label_text = "You have lost!\nYou can launch a new game from the game window"
        elif text=="Victory":
            label_text = "You have won!\nYou can launch a new game from the game window"
        Label(popup,text=label_text).pack()
        Button(popup,text='Close',command=lambda:window.destroy()).pack(padx=10,pady=20)
        Button(popup,text='Return to the game',command=lambda:popup.destroy()).pack(padx=10,pady=3)
        popup.transient(window) #Impossible to reduct
        popup.grab_set() #Impossible to interact with the main window
        window.wait_window(window) #Main window paused

lost = False