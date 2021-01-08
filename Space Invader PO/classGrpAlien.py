#Header
"""
But : Classe qui gère un groupe d'aliens
Auteur : Ankou Pierre-Olivier
Date de maj : 08/01/2021
"""
"""
cGrpAlien est une classe qui définit les gestion d'un groupe d'alien.
La définition d'un objet de cette classe ne requiet aucun paramètre.
La classe possède 2 méthode:
    1- Ajout : Cette méthode prendre un objet en paramètre et l'ajoute à la liste
    attribut de notre objet.
    2- fChangement : Cette méthode prend un nombre en paramètre (-1 ou 1) qui
    est la direction et ne retourne rien. Son rôle est de modifier la direction
    des aliens du même groupe et de leur faire sauter une ligne s'il faut.
"""

class cGrpAlien():
    def __init__(self):
        self.grp = [] #liste d'objets

    def Ajout(self,Alien):
        self.grp.append(Alien)
        return()

    def fChangement(self,pdirection):
        for i in self.grp:
            if pdirection == -1:
                i.direction = pdirection
            else :
                i.direction = pdirection
                i.rdy += 30
                i.y += 30
        return()