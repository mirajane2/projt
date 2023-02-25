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
        numero = str(marge(planchette)) + str(longueur(planchette)-2*marge(planchette)
        ) + str(marge(planchette))
        return numero
