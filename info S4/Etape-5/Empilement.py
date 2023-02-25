from unicodedata import numeric
import Planchette


def cree(planchette, centre):
        indicateurDesequilibre = "!"
        masse = planchette[0]                  #la masse egale a la longueur de la planche
        centreGeo = centre                     #centre geo egale a l'argument centre
        centreGra = centre
        Numero = Planchette.numero(planchette)    #Numero est egale au resultat de la fonction numero de la planchette  
        empilement = [centreGeo, masse, centreGra, indicateurDesequilibre, Numero]  #cree mon empilement
        return empilement

def planchette(empilement):
	return empilement[1]  #return mon deuxieme argument de empilement

def centreGeometrique(empilement):
	return empilement[0]     #return mon premeir argument de empilement

def masse(empilement, valeur=None):
        if(valeur !=None):
                empilement[1] = valeur   # si la valeur est different de none alors prends la nouvelle valeur
                masse = valeur
        else:
                masse = empilement[1]       # si non prend la valeur de la masse de l'empilement
                
        return masse

def centreGravite(empilement, valeur=None):#meme systeme que masse
        if(valeur !=None):
                empilement[2] = valeur  
                gravite = valeur
        else:
                gravite = empilement[2]
                
        return gravite

def desequilibre(empilement, valeur=None): ##meme systeme que masse
        if(valeur !=None):
                empilement[3] = valeur
                desequilibre = valeur
        else:
                desequilibre = empilement[3]

        return desequilibre

def versChaine(empilement):
        res = " n="+str(empilement[4])  + " m="+str(masse(empilement)) + " c=" + str(centreGeometrique(empilement)) +" g=" + str(centreGravite(empilement)) +  str(desequilibre(empilement))    #affiche les donnés de la planche 
        return res
