from pickle import TRUE
import Planchette
import Empilement

def cree():
	pile = []
	return pile

def estVide(pile):
	len(pile)
	if(len(pile)==0):
		p= True
	else:
		p= False
	return p

def sommet(pile):
	if(len(pile)==0):
		sommet= None
	else:
		sommet= pile[]
	return sommet

def empile(pile, planchette, decalage):
	if(len(pile)==0):
                e1 = empilement.cree(planchette,empilement.centreGravite,decalage)
        else:
                e1 = empilement.cree(planchette, decalage)
	pass

def versChaine(pile):
	return None

def empileEtCalcule(pile, planchette, decalage):
	empile(pile, planchette, decalage)
	calculeCentresGravite(pile)
	calculeEquilibre(pile)

def calculeCentresGravite(pile):
	pass

def calculeEquilibre(pile):
	pass
