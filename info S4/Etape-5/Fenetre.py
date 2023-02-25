from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra'

def cree(largeur, hauteur):
        fen=Tk()
        fenetre =[largeur,hauteur,fen,Canvas(fen,bg='dark grey',height=largeur,width=hauteur)]
        fenetre.pack()
        return fenetre 

def toile(fenetre):
        toile=fenetre[3]
        return toile

def largeur(fenetre):
        largeur=fenetre[0]
        return largeur

def hauteur(fenetre):
        hauteur=fenetre[1]
        return hauteur

def tk(fenetre):
        tk=fenetre[2]  
        return tk

def affiche(fenetre):
       fenetre.mainloop()
         




# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
        fenetre(fenetre).addtag_all(TagGraphiques)
        fenetre(fenetre).delete(TagGraphiques)
	
def quandOuverte(fenetre, fonction, argument):
	def fonctionInterne(e):
		tk(fenetre).unbind('<Map>') 
		fonction(argument)
	tk(fenetre).bind('<Map>', fonctionInterne)

def afficheMessage(fenetre, message):
	pass

def saisisTexte(fenetre, message):
	return None

def saisisEntier(fenetre, message):
	return None

def saisisFlottant(fenetre, message):
	return None

def quitte(fenetre):
	tk(fenetre).quit()