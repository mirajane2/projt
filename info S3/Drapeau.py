from tkinter import *
def drapeau_France():
    can.delete(ALL)
    can.create_rectangle(25,75,475,375,width=2,fill='white') 
    can.create_rectangle(25.5,75.5,175,374.2,width=0,fill='blue') 
    can.create_rectangle(325,75.5,474.5,374.5,width=0,fill='red') 
def drapeau_Allemagne():
    can.delete(ALL)
    can.create_rectangle(25,75,475,375,width=2,fill='black') 
    can.create_rectangle(25.5,125,475,225,width=0,fill='red')
    can.create_rectangle(25.5,200,475,225,width=0,fill='yellow')
def drapeau_Italie():
    jcnj
def drapeau_Olympique():
    cnjk

fen1 = Tk()
can = Canvas(fen1,bg='dark grey',height=500,width=500)
can.pack(side=LEFT)
bou1=Button(fen1,text = 'France',command=drapeau_France)
bou1.pack()
bou2=Button(fen1,text = 'Allemagne',command=drapeau_Allemagne)
bou2.pack()
bou3=Button(fen1,text = 'Italie',command=drapeau_Italie)
bou3.pack()
bou4=Button(fen1,text = 'Drapeau_Olympique',command=drapeau_Olympique)
bou4.pack()
bou5=Button(fen1,text = 'Quitter',command=fen1.quit)
bou5.pack(side=BOTTOM)
fen1.mainloop()
