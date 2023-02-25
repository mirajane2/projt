from statistics import variance
import Exemplaires
import Planchette

def cree():
	pioche = [Exemplaires.cree(181,1),
	Exemplaires.cree(262,2),
	Exemplaires.cree(343,3),
	Exemplaires.cree(282,2),
	Exemplaires.cree(363,3),
	Exemplaires.cree(444,4),
	Exemplaires.cree(383,3),
	Exemplaires.cree(464,4),
	Exemplaires.cree(545,5)]
	return pioche

def nombrePlanchettes(pioche):
	somme = 0
	for ex in pioche:
		somme += Exemplaires.nombre(ex)
	return somme

def versChaine(pioche):
	return None

def recherche(pioche, numero):	
	for ex in pioche:
		if Exemplaires.planchette(ex) == numero:
			return True	
	return -1
def contient(pioche, numero):
	for ex in pioche:
		if Exemplaires.planchette(ex) == numero:
			return True
	return False
def retire(pioche, numero):
	if Exemplaires.planchette ==  True :
		Exemplaires.nombre = -1
	pass