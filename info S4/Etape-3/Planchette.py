# Etape 2

Epaisseur = 1

def cree(longueur, marge):
        planchette = [longueur,marge]
        return planchette

def longueur(planchette):
        longueur = planchette[0]
        return longueur

def marge(planchette):
        marge =planchette[1]
        return marge

def numero(planchette):
        numero = str(planchette[1]) +str(planchette[0]-2*planchette[1]) +str(planchette[1])
        return numero
