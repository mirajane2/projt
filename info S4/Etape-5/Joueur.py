import Pioche

def cree(numero):
	joueur = [numero,Pioche.nombrePlanchettes]
	return joueur

def numero(joueur):
	num = 1
	return num

def nom(joueur):
	nom = "joueur" + " " + str(numero(joueur))
	return nom

def pioche(joueur):
	pioche = joueur[1]
	return pioche
