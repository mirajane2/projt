import Vecteur

def cree(x, y):
	newPoint = {}
	newPoint["x"] = x
	newPoint["y"] = y

	return newPoint


# x(p) => retourne l'abscisse du point p =>lecture
#          point <= p
#          valeur <= None

# x(p, 5) => donne à l'abscisse du point p la valeur 5 => écriture
#          point <= p
#          valeur <= 5

x(p,12) =>écriture


def x(point, valeur=None):
	if (valeur != None):
                # Accès en écriture
                point["x"] = valeur
                resultat= valeur
	else:
                # Accès en lecture
                resultat= point["x"]
	return resultat

def y(point, valeur=None):
	if (valeur != None):
                point["y"] = valeur
                resultat1= valeur  
	else:
                # Accès en lecture
                resultat1= point["x"]
	return resultat1
def vecteur(point):
	return (point["x"], point["y"])

def deplace(point, deplacement):
	pass
