from tkinter import *
import random
import time
from PIL import ImageTk
from PIL import Image
import sys

class banana:
    def __init__(self):
        self.x_banana=0
        self.y_banana=0


    def set_x(self,x):
        self.x_banana=x
        print("maeesbanana: ", self.x_banana)

    def get_x(self):
        return self.x_banana

    def set_y(self,y):
        self.y_banana=y
    def get_y(self):
        return self.y_banana

    def dibujar (self,lienzo):
        image_banana=PhotoImage(file="banana.png")
        name1=lienzo.create_image(self.x_banana, self.y_banana, image = image_banana)

        print("entra")
        


def win_aux():
    if(ventana.active):
        ventanaB=Toplevel(ventana)  # crea una ventana secundaria
        ventanaB.title("Code_Monkey")
        ventana.resizable(width=False, height=False)
        ventanaB.geometry("600x300")
        ventanaB.protocol("WM_DELETE_WINDOW", lambda:(toogle(), ventanaB.destroy()))
        toogle()
        next_level= Button(ventanaB,text="Play",command=lambda:[change_level(),toogle(), ventanaB.destroy()],bg="#000",fg="white")
        next_level.place(x=300,y=250)
        next_level.config(width=10, height=2)
        



def change_level():
    ventana.active
    contenedor.destroy()
    new_canvas=Canvas(ventana, width=570,height=560,bg="white") #Tamaño del canvas
    new_canvas.place(x=15,y=15)
    new_canvas.create_text(50,20,fill="darkblue",font="Times 20 italic bold",text="Nivel 2")
    
def toogle(Self=None):
    ventana.active = not ventana.active

    for widget in ventana.winfo_children():
        # only change the state if "state" exists in config and the widget is not Label
        if(widget.config().get("state") and widget.winfo_class() != "Label"):
            widget["state"] = {True:"normal", False:"disabled"}[ventana.active]
    
    
ventana = Tk()
ventana.active=True

ventana.geometry("1200x600")
ventana.title("Code_Monkey")
ventana.resizable(width=False, height=False)



def mover():
    posicion=0
    mensaje=caja.get(1.0 , "end-1c") #En (2.0), el 2 hace referencia a la fila donde se quiere obtener el txt y el 0 la columna hace referen
    print(mensaje)
    posicion= mensaje.find(" ",posicion)
    pasos= int(mensaje[posicion+1:posicion+2])
    mensaje=mensaje[0:posicion]
    
    if mensaje=="turnleft":
        i=0
        while i<pasos:
            x=-35
            y=0
            contenedor.move(monkey,x,y)
            ventana.update()
            time.sleep(0.5)
            i+=1
    elif mensaje=="turnrigh":
        i=0
        while i<pasos:
            x=35
            y=0
            contenedor.move(monkey,x,y)
            ventana.update()
            time.sleep(0.5)
            i+=1
    elif mensaje=="turnup":
        i=0
        while i<pasos:
            x=0
            y=-35
            contenedor.move(monkey,x,y)
            ventana.update()
            time.sleep(0.5)
            i+=1
    elif mensaje=="turndown":
        i=0
        while i<pasos:
            x=0
            y=35
            contenedor.move(monkey,x,y)
            ventana.update()
            time.sleep(0.5)
            i+=1
    win_aux()

def escribirleft():
    caja.delete(1.0, 'end')
    caja.insert('insert', "turnleft")
def escribirrigh():
    caja.delete(1.0, 'end')
    caja.insert('insert', "turnrigh")
def escribirup():
    caja.delete(1.0, 'end')
    caja.insert('insert', "turnup")
def escribirdown():
    caja.delete(1.0, 'end')
    caja.insert('insert', "turndown")

def is_near(lista,x,y):
    for i in range(len(lista)):
        #print("x= ",x, "xbanana= ", lista[i][1])
        #print("y= ",y, "ybanana= " ,lista[i][2])
        xbanana= lista[i].x_banana
        ybanana= lista[i].y_banana
        if ((x<(xbanana-100) or x>(xbanana+100))and (y<(ybanana-100)or y>(ybanana+100))):
            if (i<len(lista)-1):
                print ("verdadero")
            else:
                return False
                break
        else:
            print ("falso")
            return True
            break



#Caja de texto
caja = Text(ventana,width=73, height=35)
caja.grid(row=1, column=0,padx=600,pady=15)

contenedor= Canvas(ventana, width=570,height=560,bg="white") #Tamaño del canvas
contenedor.place(x=15,y=15)
contenedor.create_text(50,20,fill="darkblue",font="Times 20 italic bold",text="Nivel 1")

def crear_bananas(cantidad):
    i=0
    while i<cantidad:
        name= "banana" + str(i)
        x_ram=random.randint(30, 500)
        y_ram=random.randint(30, 500)
        if (len(listabanana)==0):
            ban=banana()
            ban.set_x(x_ram)
            ban.set_y(y_ram)
            image_banana=PhotoImage(file="banana.png")
            name1=contenedor.create_image(x_ram, y_ram, image = image_banana)
            lista=[name,ban.x_banana,ban.y_banana]
            listabanana.append(ban)
            i+=1
        else:
            for j in range(len(listabanana)):
                if not is_near(listabanana, x_ram,y_ram):
                    ban=banana()
                    ban.set_x(x_ram)
                    ban.set_y(y_ram)
                    lista=[name,ban.x_banana,ban.y_banana]
                    listabanana.append(ban)
                    i+=1
                

    #poner condicion pra que no choquen las bananas entre si y no pegue con el mono

#insertando Bananas
listabanana=[]
crear_bananas(3)
image_banana=PhotoImage(file="banana.png")
j=0
for i in listabanana:
    xx=listabanana[j].x_banana
    yy=listabanana[j].x_banana
    name1=contenedor.create_image(xx,yy, image = image_banana)
    j+=1

#image_banana=PhotoImage(file="banana.png")
#name1=contenedor.create_image(listabanana[0].x_banana, listabanana[0].y_banana, image = image_banana)






    
#Imagen
#fondo1=PhotoImage(file="pista1.png")
#fondo =Label(ventana, image=fondo1).place(x=0,y=0)
image_monkey=PhotoImage(file="mono.png")
#monkey=contenedor.create_image(200, 200, image = image_monkey)
#monkey=Label(ventana, image=image_monkey).place(x=x,y=y)
im = Image.open("mono.png")
im2=im.rotate(90)
imagep= ImageTk.PhotoImage(im2)
monkey=contenedor.create_image(200, 200, image = imagep)


botonCompi = Button(ventana,text="Compilar",command=mover,bg="#000",fg="white")
botonCompi.place(x=1100,y=530)
botonCompi.config(width=10, height=2)

botonLeft = Button(ventana,text="Turn Left",command=escribirleft,bg="#000",fg="white")
botonLeft.place(x=600,y=530)
botonLeft.config(width=10, height=2)

righ = Image.open('righ.png')
righ = righ.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
righ = ImageTk.PhotoImage(righ)
botonRigh = Button(ventana,image=righ,command=escribirrigh,compound="top")
botonRigh.place(x=700,y=520)
#botonRigh.config(width=10, height=2)

botonUp = Button(ventana,text="Turn up",command=escribirup,bg="#000",fg="white")
botonUp.place(x=800,y=530)
botonUp.config(width=10, height=2)

botonDown = Button(ventana,text="Turn Down",command=escribirdown,bg="#000",fg="white")
botonDown.place(x=900,y=530)
botonDown.config(width=10, height=2)



#idea para cambiar de nivel seria solamente cambiar el canvas

ventana.mainloop()





#codigo para mover objetos dentro de un canvas con teclado
'''
def left(event):
    x=-25
    y=0
    contenedor.move(monkey,x,y)
def right(event):
    x=25
    y=0
    contenedor.move(monkey,x,y)
def up(event):
    x=0
    y=-25
    contenedor.move(monkey,x,y)
def down(event):
    x=0
    y=25
    contenedor.move(monkey,x,y)
    

ventana.bind("<Left>",left)
ventana.bind("<Right>",right)
ventana.bind("<Up>",up)
ventana.bind("<Down>",down)'''