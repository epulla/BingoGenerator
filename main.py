from tkinter import *
import matplotlib.pyplot as plt
import tabla as tbl
import generator_table as gt
import sys
import io



def Generate(e1,e2,e3,p,num):
    text = e1+"\n"+e2+"\n"+e3
    #label_stdout.config(text="Generando tablas....\nEspera un momento :p")
    if int(num) == 0:
        label_stdout.config(text="Es necesario que ponga un numero mayor a 0")
        return
    gt.tables_to_pdf(int(num),text,p)
    label_stdout.config(text="ARCHIVO PDF GENERADO CON "+num+" TABLAS :D\nArchivo generado: tablas_imprimir.pdf")



master = Tk()
master.title("Ventanica")
master.geometry("700x700")

#Encabezado 1
Label(master, text='Encabezado 1:',fg="#F60960",font=("Helvetica",16,"bold")).place(x=35,y=87)
e1 = Entry(master,width=40,font=("Helvetica",14,"bold"))
e1.place(x=200,y=90)

#Encabezado 2
Label(master, text='Encabezado 2:',fg="#F60960",font=("Helvetica",16,"bold")).place(x=35,y=127)
e2 = Entry(master,width=40,font=("Helvetica",14,"bold"))
e2.place(x=200,y=130)

#Encabezado 3
Label(master, text='Encabezado 3:',fg="#F60960",font=("Helvetica",16,"bold")).place(x=35,y=167)
e3 = Entry(master,width=40,font=("Helvetica",14,"bold"))
e3.place(x=200,y=170)

#Palabra que forman cada tabla (Maximo 6)
Label(master, text='Frase: ',fg="#F60960",font=("Helvetica",16,"bold")).place(x=35,y=207)
p = Entry(master,width=40,font=("Helvetica",14,"bold"))
p.place(x=200,y=210)

#Numbero de tablas GYE
Label(master, text='Numero tablas: ',fg="#F60960",font=("Helvetica",16,"bold")).place(x=35,y=247)
num = Spinbox(master,from_=0,to=200,width=5)
num.place(x=200,y=250)

#Lo que imprime la consola
label_stdout = Label(master,text="",height=11,width=50,font=("Helvetica",16,"bold"))
label_stdout.place(x=50,y=400)

#Boton de imprimir por consola
button1 = Button(master,text="Obtener Bingo!",width=25,command=lambda: Generate(e1.get(),e2.get(),e3.get(),p.get(),num.get()),
            bg="black",fg="white",font=("Helvetica",14,"bold"))
button1.place(x=200,y=600)
master.mainloop()
