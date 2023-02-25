import Fenetre

print(Fenetre.Titre)

f = Fenetre.cree(1000, 600)
print("f=" + str(f))

print('toile=' + str(Fenetre.toile(f)))
print('largeur=' + str(Fenetre.largeur(f)))
print('hauteur=' + str(Fenetre.hauteur(f)))
print('tk=' + str(Fenetre.tk(f).title()))

Fenetre.toile(f).create_rectangle(10, 10, 100, 200, fill="blue")

Fenetre.affiche(f)
