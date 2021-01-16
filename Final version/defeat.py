# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:37:53 2021

@author: jonat
"""

from tkinter import Toplevel, Button

class Defeat():
    """
    Class generating a popup when the game is lost
    """
    def __init__(self,window):
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
        self.window = window
        popup = Toplevel() #Popup above the main window
        popup.title('Defeat')
        Button(popup,text='Quitter',command=lambda:self.window.destroy()).pack(padx=10,pady=10)
        popup.transient(self.window) #Impossible to reduct
        popup.grab_set() #Impossible to interact with the main window
        self.window.wait_window(popup) #Main window paused