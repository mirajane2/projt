operation = input("un autre calcul?(O/N")
typeOpertaion = input("type d\' operation souhaite : (a)ddition, (s)oustration, (m)ultiplication, (d)ivison")
while typeOperation == "a" or "s" or "m" or "d":
    if typeOperation == "a" or typeOperation == "s" or typeOperation == "m" or typeOperation == "d" : 
        variable1 = int(input("saisir un chiffre 1 :"))
        variable2 = int(input("saisir un chiffre 2 :"))
        if typeOpertaion == "a" :
            result = variable1 + variable2
            operateur = "+"
        elif typeOpertaion == "s" :
            result = variable1 - variable2
            operateur = "-"
        elif typeOpertaion == "m" :
            result = variable1 * variable2
            operateur = "*"
        elif typeOpertaion == "d" :
            if varaible2 >0.0 :
                result = variable1 / variable2
                operateur = "/"
            else :
                result = "division impossible"

    print("resultat :", varaible1, operateur, varaible2, "=", result)
else :
    print("Erreur de saisie")
operation = input("un autre calcul?(O/N")
