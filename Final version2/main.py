# -*- coding: utf-8 -*-
#Header
"""
But: programme principale
Auteur :  Jonathan Bouyer & Pierre-Olivier Ankou
Date de maj : 17/01/2020
"""

"""
Needed changes (in french):
Une fin de partie par collision avec le bord de l'écran renvoie une erreur (mais le reste fonctionne)
Le bouton New Game fonctionne mais accélère les ennemis ou les freeze
"""

from tkinter import Tk,Label,Button,Canvas,PhotoImage

from alien import Alien
from ship import Ship
from protection import Protection

class SpaceInvaders():
    """
    Class creating the game window and its elements, the game elements and start the game
    """
    def __init__(self):
        """
        This function creates the game window and its elements

        Returns
        -------
        None.

        """
        self.window = Tk()
        self.window.geometry("1200x900")

        self.label_score = Label(self.window, text="Score : 0")
        self.label_score.place(x=10, y=10)

        self.label_vies = Label(self.window, text="Lives : 3")
        self.label_vies.place(x=1130, y=10)

        self.button_new = Button(self.window, text="New Game", width=15,command=lambda:self.restart())
        self.button_new.place(x=400, y=860)

        self.button_quit = Button(self.window, text="Quit", width=15, command = lambda:self.window.destroy())
        self.button_quit.place(x=680, y=860)

        self.canvas = Canvas(self.window, height = "800", width = "1200", bg='black')
        photo = PhotoImage(file = 'image/1438618238-wallhaven-428762.png')
        item = self.canvas.create_image(613,347,image = photo)
        self.canvas.pack(expand=True)

        self.run()

    def run(self):
        """
        This function creates the game elements and start a game

        Returns
        -------
        None.

        """
        self.ship = Ship(self.canvas,self.window)
        self.alien = Alien(self.canvas,self.window,5,4)
        self.alien.run()

        self.protection1 = Protection(self.canvas,self.window,100,700)
        self.protection2 = Protection(self.canvas,self.window,400,700)
        self.protection3 = Protection(self.canvas,self.window,700,700)
        self.protection4 = Protection(self.canvas,self.window,1000,700)

        self.window.bind("<KeyPress-Right>",self.ship.right)
        self.window.bind("<KeyRelease-Right>",self.ship.stopright)
        self.window.bind("<KeyPress-Left>",self.ship.left)
        self.window.bind("<KeyRelease-Left>",self.ship.stopleft)
        self.window.bind("<KeyPress-space>",self.ship.tir)
        self.window.bind("<KeyRelease-space>",self.ship.stoptir)
        self.window.mainloop()

    def restart(self):
        """
        This function reinitialize the position and the number of the aliens, the lives of the player and the protection, and the score

        Returns
        -------
        None.

        """
        self.canvas.delete('all')
        self.run()

SpaceInvaders()