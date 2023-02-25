def addition(x,y):
    add = x+y
    return add
def soustraction(x,y):
    sous = x-y  
    return sous
def multiplication(x,y):
    mul = x*y
    return mul
def division(x,y):
    if y >0.0 :        
        div = x*y
    else :
        div = "division impossible"
        return div
re = "o"
while ( re == "o" ) | ( re == "O" ) :
    operation = input("un autre calcul?(O/N)")
    x = int(input("saisir un chiffre 1 :"))
    y = int(input("saisir un chiffre 2 :"))
    typeOperation = input("choisir operation(a,s,m,d):")
    if typeOperation == "a" :
        resultat = addition(x,y)
        print(x,"+",y,"=",resultat)
    elif typeOperation == "s" :
        resultat = soustraction(x,y)
        print(x,"-",y,"=",resultat)
    elif typeOperation == "m" :
        resultat = multiplication(x,y)
        print(x,"*",y,"=",resultat)
    elif typeOperation == "d" :
        resultat = division(x,y)
        print(x,"/",y,"=",resultat)
    else :
        print("erreur de saisie")
    operation = input ("Un autre calcul ? o/n ") 



