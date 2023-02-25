#Programme calcul hauteur escalier
nbMarches = -1
hauteurMarche = 0
try : 
 nbMarches = input("Combien de marches ?") # on demande de saisir le nombre de marches
 if nbMarches<=0:
     raise ErrorMarche
except ErrorMarche:
    print("erreur de saisie de marches,veulliez reesayez")
try:
 nbMarches = int(nbMarches) # On convertit le nombre
except:
    print("erreur de conversion")
try:
 hauteurMarche = int(input("Hauteur d'une marche (cm) ?")) # À présent, on saisit la hauteur d'une marche
except:
    print("type de valuyr non conforme")
resultat = nbMarches * hauteurMarche
print("Pour ", nbMarches , " marches de ", hauteurMarche , " cm, la hauteur est de " , resultat,"cm")
