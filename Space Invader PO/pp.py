#Header
"""
But: crÃ©er une interface graphique
Auteur : Ankou Pierre-Olivier
Date de maj : 18/12/2020
"""

from tkinter import Tk,Button,Label,PhotoImage,Canvas,Menu

from score import fscore as score
from nouvellePartie import fnouvellePartie as new
from generateur import fgenerateur
from classAlien import cAlien



window = Tk()
window.geometry("1200x900")

#boutons
boutonQuitter = Button(window, command = window.destroy, text = "Quitter")
boutonQuitter.pack(side = "bottom")
boutonPartie = Button(window, command = new, text = "Nouvelle Partie")
boutonPartie.pack(side = "bottom")

#label
labelScore = Label(window, text = "Score : ")
labelScore.pack(side = "top")

#image
canvas1 = Canvas(window, width = 1223 ,height = 691, bg = 'blue')
photo = PhotoImage(file = 'image/1438618238-wallhaven-428762.png')
item = canvas1.create_image(613,347,image = photo)
canvas1.pack(side = "left")

#Alien
fgenerateur(window,canvas1)

#menu
menubar = Menu(window)
menuaide = Menu(menubar, tearoff = 0)
window.config(menu=menubar)

window.mainloop()