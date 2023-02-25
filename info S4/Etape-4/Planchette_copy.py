# Etape 2

Epaisseur = 1
class Planchette_copy :
        planchette =[]
        def __init__(self,longueur, marge):
                self.planchette = [longueur,marge]
                
        def longueur(self):
                return self.planchette[0]

        def marge(self):
                return self.planchette[1]

        def numero(self):
                numero = int(self.marge) + int(self.longueur)-2*int(self.marge) + int(self.longueur)
                return str(numero)


