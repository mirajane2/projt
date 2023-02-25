from datetime import *
def conversion(h,m,s):    
    return(int(h)*3600+int(m)*60+int(s)
def tempsEcoule(conversion1, conversion2):
    return conversion1 - conversion2
a=str(datetime.now().time())
print(a[0:5])
heure = input("saisir une heure :")
minutes = input("saisir des miniutes:")
secondes = input("saisir des secondes :")

heure2 = input("saisir une heure entre 00 et 23 :")
minutes2 = input("saisir des miniutes entre 00 et 59:")
secondes2 = input("saisir des secondes entre 00 et 59 :")
coneversion1=conversion(heure,minutes,seconde)
conversion2=conversion(conversion(heure2,minute2,seconde2)
temps=abs(tempsEcoule(conversion1,conversion2)                       
print
