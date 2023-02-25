from tkinter import *

    
def carte():
    can.delete(ALL)
    background= PhotoImage(file="map_france_494x516.gif")
    can.create_image(20,20, anchor = 'nw',image=background)
    #f = open('villes.txt', 'r')                     
    #x = (lon - lon_min) * width / (lon_max - lon_min)               convertion des coordonnes      
    #y = lat_max - (lat - lat_min) * height / (lat_max - lat_min)     
    fen.mainloop()
def carte2():
    can.delete(ALL)
    background= PhotoImage(file="map_france_742x773.gif")
    can.create_image(20,20, anchor = 'nw',image=background)
    fen.mainloop()
def carte3():
    can.delete(ALL)
    background= PhotoImage(file="map_france_989x1031.gif")
    can.create_image(10,10, anchor = 'nw',image=background)
    fen.mainloop()
def selection(event):
    line = liste.curselection()[0]
    item = liste.get(line)
    if(item=="494x516"):
        carte()
    elif(item=="742x773"):
        carte2()
    elif(item=="989x1031"):        
        carte3()

 
fen = Tk()
can = Canvas(fen,bg='dark grey',height=1300,width=1100)
can.pack(side=LEFT)
liste=Listbox(fen,bg="beige",height=100,width=300)
liste.insert(0,"494x516")
liste.insert(1,"742x773")
liste.insert(2,"989x1031")
liste.pack(side=LEFT)
liste.bind("<<ListboxSelect>>", selection) 
fen.mainloop()




