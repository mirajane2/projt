import Planchette

print(Planchette.Epaisseur)

p = Planchette.cree(10, 2)
print('p=' + str(p))

l = Planchette.longueur(p)
print('longueur=' + str(l))

m = Planchette.marge(p)
print('marge=' + str(m))

n = Planchette.numero(p)
print('numero=' + str(n))


