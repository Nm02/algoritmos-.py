from tkinter import *

"""ventanas"""


raiz=Tk()#crear ventana

raiz.title("prueba")#titulo
#raiz.iconbitmap("imagenes/logo para prueba.ico")#cambiar logo en el titulo (necesita un archivo .ico)

raiz.resizable(0,0)#permiso para editar el tamaño de ventana desde el programa (X,Y)
raiz.geometry("650x650")#editar tamaño inicial de la ventana (X x Y). Si no se agrega, la ventana toma el tamaño del frame

raiz.config(bg="green")#cambiar el color de fondo de la ventana

"""frames"""

frame1=Frame()#crear frame
frame1.pack()#agregar el frame a la ventana. 
#si dentro del () se agrega side= se puede anclar el frame a un lado especifico ("left", "rigth","top","bottom")
#se luego del side=, se agrega un anchor= se puede establecer una esquina (n,s,e,w)
#si se escribe fill= se puede hacer que el frame adopte el tamaño de la ventana todo el tiempo (x,y,both,none)
#para que se expanda sobre el eje y se debe agregar el atributo expand=True

# frame1.config(bg="red")#cambiar color del frame
# frame1.config(width=650,height=500)#cambiar tamaño (X,Y)
# frame1.config(relief="groove")#cambiar color del borde
# frame1.config(bd=35)#establece el tamaño del borde
# frame1.config(cursor="pirate")#cambia el cuerosr en el frame

# label = Label(raiz,text="¡Hola Mundo!")
# label.pack()


raiz.mainloop()#bucle para poder usar una ventana
