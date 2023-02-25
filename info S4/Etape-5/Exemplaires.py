import Planchette

def cree(planchette, nombre):
        exemplaires = [planchette,nombre]
        return exemplaires

def planchette(exemplaires):
        return exemplaires[0]

def nombre(exemplaires, valeur=None):
        if(valeur !=None):
                exemplaires[1]=valeur
                nombre = valeur
        else:
                nombre = exemplaires[1]
        return nombre

def retireUn(exemplaires):
        suppression = exemplaires[1] - 1
        return suppression

def versChaine(exemplaires):
        resultat = str(nombre(exemplaires)) + "x" + str(Planchette.numero(planchette(exemplaires)))
        return resultat
