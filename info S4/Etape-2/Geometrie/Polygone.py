import Point

def cree(x1, y1, x2, y2, couleur, epaisseur):
	point1 = Point.cree(x1, y1)
	point2 = Point.cree(x2, y2)

	polygoneParams = {}
	polygoneParams["couleur"] = couleur
	polygoneParams["epaisseur"] = epaisseur

	return ([point1, point2], polygoneParams)

def points(polygone):
	return polygone[0]

def couleur(polygone, valeur=None):
	if (valeur != None):
		polygone[1]["couleur"] = valeur
		return polygone[1]["couleur"]

	return None

def epaisseur(polygone, valeur=None):
	if (valeur != None):
		polygone[1]["epaisseur"] = valeur
		return polygone[1]["epaisseur"]
	
	return None

def ajoute(polygone, x, y):
	newPoint = Point.cree(x, y)
	polygone[0].append(newPoint)
