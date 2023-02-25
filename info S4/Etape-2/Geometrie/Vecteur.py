import math

def cree(x, y):
    vecteur=(x,y)
    return vecteur

def x(vecteur):
    coordonne1 = vecteur[0]
    return coordonne1

def y(vecteur):  
    coordonne2 = vecteur[1]
    return coordonne2

# propriété calculée
def norme(vecteur):
    norme = math.sqrt(x(vecteur)**2 + y(vecteur)**2)
    return norme

def somme(vecteur1, vecteur2):
    return cree(x(vecteur1) + x(vecteur2),y(vecteur1) + y(vecteur2))
