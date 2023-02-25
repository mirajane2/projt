#Programme Projet  -  Liste de Noël  -  Ian SKRZESZEWSKI

#Importation module "temps"
import time #Importation de time pour fermer le programme

#....
print("Bonjour, voici le programme de gestion de votre liste pour Noël.")
print("----------------------------------------------------------------")
print("") #Espace

# Listes vides pour éléments et index éléments cochés ou non.
liste_Noel = []
liste_Noel_coche = [] #Liste de Noël qui prendra les états des cadeaux (coché ou non coché)


#------------------------------------------------------------------------------------------
#Fonction qui permet de gérer les choix de l'utilisateur :
def demande_utilisateur() :
    print("") #Espace
    commande = input("Commande --> a:ajouter - d:supprimer - c:cocher - l:afficher la liste - q:quitter  ")

    if commande == "a" or commande =="A" : #Commande ajouter
        ajouter()
    if commande == "d" or commande =="D" : #Commande supprimer
        supprimer()
    if commande == "c" or commande =="C" : #Commande cocher
        cocher()
    if commande == "q" or commande =="Q" : #Commande quitter 
        quitter()
    if commande == "l" or commande =="L" : #Commande afficher liste
        affichage_liste()
    else : #Cas ou l'entrée est vide ou ne correspond pas à une des proposition 
        print("Commande invalide, veuillez recommencer")
        demande_utilisateur() #Relance la fonction
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
#Fonction pour ajouter un cadeau :
def ajouter() :
    nouveau_cadeau = input("Quelle cadeau voulez-vous ajouter ?  ")
    #try :
       # nouveau_cadeau = str(nouveau_cadeau)
   # except :
      #  print("Erreur dans la conversion du texte")
      #  nouveau_cadeau = input("Quelle cadeau voulez-vous ajouter ?  ")
    while nouveau_cadeau == "" : #Si saisie vide
        print("Erreur, saisie vide")
        nouveau_cadeau = input("Quelle cadeau voulez-vous ajouter ?  ")
   # while nouveau_cadeau != str :
       # print("Erreur, du texte est attendu")
       # nouveau_cadeau = input("Quelle cadeau voulez-vous ajouter ?  ")
    if nouveau_cadeau in liste_Noel : # On vérifie si l'élément est déjà dans la liste
        choix_ajouter = input("Ce cadeau existe déjà dans la liste, êtes-vous sur de vouloir l’ajouter ? (oui/non) ") #Message
        if choix_ajouter == "oui" or choix_ajouter == "OUI" : #Si utilisateur choisi OUI
            liste_Noel.append(nouveau_cadeau) #Rajout du cadeau dans la liste
            liste_Noel_coche.append("-")
        else : #Si non , on relance les commandes
            demande_utilisateur()

    else :   #Cas ou le cadeau n'est pas déjà dans la liste (pas de changement)
        liste_Noel.append(nouveau_cadeau) #Rajout du cadeau dans la liste
        liste_Noel_coche.append("-")

    #Affichage de la liste
    compteur = 1     
    for elements in liste_Noel : # Elements dans ma liste de Noël
        index_cadeau = compteur - 1
        print(compteur,liste_Noel_coche[index_cadeau],elements) #Afficher : compteur, liste "coché ou non", cadeau
        compteur+=1

    demande_utilisateur() #On relance les choix de l'utilisateur
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
#Fonction pour supprier un cadeau :
def supprimer () :   
    element_a_supprimer = input("Numéro du cadeau à supprimer ?   ") #Demande du numéro
    while element_a_supprimer == "" : #Si saisie vide
        print("Erreur, saisie vide")
        element_a_supprimer = input("Numéro du cadeau à supprimer ?   ")
    try : #Essaye de convertir en int
        element_a_supprimer = int(element_a_supprimer)
        index_cadeau = element_a_supprimer - 1 #On adapte l'index pour Python (liste débute à 0 et pas à 1)
        del liste_Noel[index_cadeau] #On enlève l'élément.
        del liste_Noel_coche[index_cadeau] #On enlève l'élément, coché ou non
    except : #Erreur, str et non int
        print("Erreur inconnue")
    
    
    #Affichage de la liste Une deuxième fois
    compteur = 1     
    for elements in liste_Noel : # Elements dans ma liste de Noël
        index_cadeau = compteur - 1
        print(compteur,liste_Noel_coche[index_cadeau],elements) #Afficher : compteur, liste "coché ou non", cadeau
        compteur+=1
    demande_utilisateur() # On réaffiche les choix pour l'utilisateur
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
def cocher () :
    element_a_cocher = input("Numéro du cadeau à cocher ?   ") #Demande du numéro
    while element_a_cocher == "" : #Si saisie vide
        print("Erreur, saisie vide")
        element_a_cocher = int(input("Numéro du cadeau à cocher ?   "))
    try : #Essaye de convertir en int
        element_a_cocher = int(element_a_cocher) #Conversion en "int"
        index_cadeau = element_a_cocher - 1 #On adapte l'index pour Python (liste débute à 0 et pas à 1)
      
        if liste_Noel_coche[index_cadeau] == "-" : #Si l'élément n'est pas coché, on le coche
            liste_Noel_coche[index_cadeau] = "X"
        
        else :
            if liste_Noel_coche[index_cadeau] == "X" : #Sinon, si l'élément est coché, on le décoche
                liste_Noel_coche[index_cadeau] = "-"
    except : #Si erreur, texte ou autre :
        print("Erreur, du texte est attendu")
        demande_utilisateur()

#Affichage de la liste
    compteur = 1

    for elements in liste_Noel : # Elements dans ma liste de Noël
        index_cadeau = compteur - 1 #On adapte l'index pour Python (liste débute à 0 et pas à 1)
        print(compteur,liste_Noel_coche[index_cadeau],elements) #Afficher : compteur, liste "coché ou non", cadeau
        compteur+=1
    
    demande_utilisateur() # On réaffiche les choix pour l'utilisateur
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
def affichage_liste() :
    #Affichage de la liste
    compteur = 1

    for elements in liste_Noel : # Elements dans ma liste de Noël
        index_cadeau = compteur - 1 #On adapte l'index pour Python (liste débute à 0 et pas à 1)
        print(compteur,liste_Noel_coche[index_cadeau],elements) #Afficher : compteur, liste "coché ou non", cadeau
        compteur+=1
    
    demande_utilisateur() # On réaffiche les choix pour l'utilisateur
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
def quitter () : #fonction poue se barrer <-- phrase de José
    print("Aurevoir! Le programme se fermera dans 5 secondes") #Message
    
    # Sauvegarde de la liste dans le fichier
    Liste_de_Noël = open("Liste de Noël.txt", "w") #Ouerture du fichier - écrase
    Liste_de_Noël.write("**********LISTE DE NOEL**************")
    compteur = 1 #Compteur
    for element in liste_Noel : #Même logique que pour afficher la liste 
        index_cadeau = compteur - 1   
        Liste_de_Noël.write( "\n" + liste_Noel_coche[index_cadeau]+ " " + element)
        compteur+=1
    Liste_de_Noël.close()
    time.sleep(5.0) #Pause de 5s
    exit() #Ferme le programme
 #------------------------------------------------------------------------------------------   
    

#Programme principal :
demande_utilisateur() #On lance la fonction principale