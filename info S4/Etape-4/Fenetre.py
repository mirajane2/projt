from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra'

def cree(largeur, hauteur):
        fen=Tk()
        fenetre =[largeur,hauteur,fen,Canvas(fen,bg='dark grey',height=largeur,width=hauteur)]
        return fenetre 

def toile(fenetre):
        toile=fenetre[3]
        toile.pack()
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
       
        pass 




# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
	pass
		
def afficheMessage(fenetre, message):
	pass

def saisisTexte(fenetre, message):
	return None

def saisisEntier(fenetre, message):
	return None

def saisisFlottant(fenetre, message):
	return None
