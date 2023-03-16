from tkinter import *
from tkinter import ttk
import tkinter as ttk


raiz = Tk()
raiz.title("Ejercicio 3")
raiz.geometry("1255x530")


#-----------Frame Principal-----------
principal=ttk.Frame(raiz,width=600,height=450, bg="black")
principal.grid(column=0,row=1,sticky=(W))

#-----------Frame Azul-----------

Fazul=ttk.Frame(raiz, bg="cyan4")
Fazul.grid(column=0,row=0, sticky=(W))
ttk.Label(Fazul,text="SPAI 4.0", anchor="w",width=150, font=(10),bg="cyan4",foreground="white").grid(column=0, row=0)

#-----------FrameIzq-----------
Fizq=ttk.Frame(principal,background="black")
Fizq.grid(column=0,row=0, sticky=(W),padx=10,pady=5)

#-----------FrameDer-----------
Fder=ttk.Frame(principal,background="black")
Fder.grid(column=1,row=0,sticky=(W,N),pady=13)

#-----------Frame 1Izq-----------
Fizq1=ttk.Frame(Fizq,background="black")
Fizq1.grid(column=0,row=0)

#-----------Frame 2Izq-----------
Fizq2=ttk.Frame(Fizq,background="black")
Fizq2.grid(column=0,row=1, sticky=(W))

#-----------Frame 1Der-----------
Fde1=ttk.Frame(Fder,background="black")
Fde1.grid(column=1,row=0, sticky=(N))

#-----------Iniciadores-----------
Finiciadores=ttk.Frame(Fizq1,width=100,height=100,background="#333333")
Finiciadores.grid(column=0,row=0,padx=5,pady=5)

Inilbl=ttk.Label(Finiciadores,text="Iniciadores Digitales",background="#333333",foreground="cyan4").grid(column=0,row=0)
#verde
liealbl=ttk.Label(Finiciadores,text="Linea 1:",background="#333333",foreground="white").grid(column=0,row=1)
Onlbl=ttk.Label(Finiciadores,text="On:",foreground="white", background="#333333").grid(column=1,row=1)

imgv1 = PhotoImage(file="verde.png")
etqImagen = ttk.Label(Finiciadores,bg="#333333")
etqImagen.grid(column=2,row=1)
etqImagen['image'] = imgv1

liea2lbl=ttk.Label(Finiciadores,text="Linea 2:",background="#333333",foreground="white").grid(column=0,row=2)
Onlbl=ttk.Label(Finiciadores,text="On:",foreground="white", background="#333333").grid(column=1,row=2)

img2 = PhotoImage(file="verde.png")
etqImagen2 = ttk.Label(Finiciadores,bg="#333333")
etqImagen2.grid(column=2,row=2)
etqImagen2['image'] = img2

lieabl=ttk.Label(Finiciadores,text="Linea 1:",background="#333333",foreground="white").grid(column=0,row=3)
Onlbl=ttk.Label(Finiciadores,text="On:",foreground="white", background="#333333").grid(column=1,row=3)

img3 = PhotoImage(file="verde.png")
etqImagen3 = ttk.Label(Finiciadores,bg="#333333")
etqImagen3.grid(column=2,row=3)
etqImagen3['image'] = img3
#rojo
Gablbl=ttk.Label(Finiciadores,text="Gabinete:",background="#333333",foreground="white").grid(column=0,row=4)
Onlbl=ttk.Label(Finiciadores,text="Abierto:",foreground="white", background="#333333").grid(column=1,row=4)

img4 = PhotoImage(file="rojo.png")
etqImagen4 = ttk.Label(Finiciadores,bg="#333333")
etqImagen4.grid(column=2,row=4)
etqImagen4['image'] = img4

Alarlbl=ttk.Label(Finiciadores,text="Alarma:",background="#333333",foreground="white").grid(column=0,row=5)
Onlbl=ttk.Label(Finiciadores,text="On:",foreground="white", background="#333333").grid(column=1,row=5)

img5 = PhotoImage(file="rojo.png")
etqImagen5 = ttk.Label(Finiciadores,bg="#333333")
etqImagen5.grid(column=2,row=5)
etqImagen5['image'] = img5

Alar2lbl=ttk.Label(Finiciadores,text="Alarma:",background="#333333",foreground="white").grid(column=0,row=6)
Onlbl=ttk.Label(Finiciadores,text="Off:",foreground="white", background="#333333").grid(column=1,row=6)

img6 = PhotoImage(file="rojo.png")
etqImagen6 = ttk.Label(Finiciadores,bg="#333333")
etqImagen6.grid(column=2,row=6)
etqImagen6['image'] = img6



#-----------Temperaturas-----------
Ftemp=ttk.Frame(Fizq1,background="#333333")
Ftemp.grid(column=1,row=0)
Ftemp.config(borderwidth=35)
Temp1lbl=ttk.Label(Ftemp,text="Temperatura 1:",background="#333333",foreground="white").grid(column=0,row=0)

imgtemp = PhotoImage(file="temp1.png")
etqTemp = ttk.Label(Ftemp,bg="#333333")
etqTemp.grid(column=0,row=1)
etqTemp['image'] = imgtemp

Temp2lbl=ttk.Label(Ftemp,text="Temperatura 2:",background="#333333",foreground="white").grid(column=1,row=0)

imgtemp2 = PhotoImage(file="temp2.png")
etqTemp2 = ttk.Label(Ftemp,bg="#333333")
etqTemp2.grid(column=1,row=1)
etqTemp2['image'] = imgtemp2

tempAg=ttk.Label(Ftemp,text="Temp.Agua: 58 °C",background="#333333",foreground="white").grid(column=0,row=3)
tempAmb=ttk.Label(Ftemp,text="Temp.Ambiete: 32 °C",background="#333333",foreground="white").grid(column=0,row=4)



#-----------Velocidad-----------
Fvel=ttk.Frame(Fizq2,background="#333333")
Fvel.grid(column=0,row=0,padx=3, sticky=(W))
Fvel.config(borderwidth=35)
Vellbl=ttk.Label(Fvel,text="Velocidad bomba: ",background="#333333",foreground="white", width=30).grid(column=0,row=0)

imgvel= PhotoImage(file="VelBomb.png")
etqvel = ttk.Label(Fvel,bg="#333333")
etqvel.grid(column=0,row=1)
etqvel['image'] = imgvel

#-----------Ntanque-----------
FnTanque=ttk.Frame(Fizq2,background="#333333")
FnTanque.grid(column=1,row=0, sticky=(W))
Ntanquelbl=ttk.Label(FnTanque,text="Nivel Tanque",background="#333333",foreground="cyan3", width=51, anchor="w").grid(column=0,row=0)

imgNT= PhotoImage(file="NivTanq.png")
etqnt = ttk.Label(FnTanque,bg="#333333")
etqnt.grid(column=0,row=1)
etqnt['image'] = imgNT

#-----------Produccion-----------
Fprod=ttk.Frame(Fde1,background="#333333")
Fprod.grid(column=0,row=0,sticky=(W))
Fprod.config(borderwidth=20)

Prodlbl=ttk.Label(Fprod,text="Produccion",background="#333333",foreground="cyan3").grid(column=0,row=0,sticky=(W,N))

img = PhotoImage(file="prod.png")
etqImagen = ttk.Label(Fprod,bg="gray40")
etqImagen.grid(column=0,row=1,sticky=(W,N))
etqImagen['image'] = img

raiz.mainloop()