from pytube  import *
from tkinter import *
import os,time

# >>> COLORS <<<
pink = '#000538'
white = '#ffffff'

# >>> VARIABLES <<<
width=40
height=50
pad=4
width_ = 80
height_ = 3

# >>> OS <<<
localPath = os.getcwd()
downPath = localPath+'\\Download'
imgPath = localPath+'\\IcoImages'

# >>> ROOT <<<
raiz = Tk()
raiz.resizable(0,0)
raiz.config(bg=pink)
raiz.title('YouTube video downloader')
raiz.iconbitmap(imgPath+'\\logo.ico')

# >>> FRAME <<<
miFrame = Frame(raiz,width=width,height=height,bg=pink)
miFrame.pack()
miFrame2 =Frame(raiz,width=40,height=40,bg=pink)
miFrame2.pack()

# >>> LINK <<<
img = PhotoImage(file=imgPath+'\\clear26x26.png')

linkStr = StringVar()

linkBox = Entry(miFrame,bg="#e3e3e3",fg="black",font=("Helvetica",10),borderwidth=5,textvariable=linkStr)
linkBox.grid(row=1,column=1,padx=pad,pady=pad*2,ipadx=width_,ipady=height_)

linkTex2 = Label(miFrame,text="Link del video",bg=pink,fg=white,font=("Helvetica",15),borderwidth=5)
linkTex2.grid(row=0,column=1,padx=pad,ipady=height_)

linkDel = Button(miFrame,image=img,bg="blue",fg=white,borderwidth=1,command=lambda:linkClear())
linkDel.grid(row=1,column=2,padx=pad,pady=pad)

empty1 = Button(miFrame,text="Info",bg="blue",fg=white,borderwidth=1,command=lambda:all())
empty1.grid(row=1,column=0,padx=pad,pady=pad)

def linkClear():
    linkStr.set("")

# >>> CUADRO BLANCO GRANDE <<<

dates=Text(miFrame,width=50,height=20,padx=pad,pady=pad*2*2,cursor="arrow",bd=5)
dates.grid(row=2,column=1)

def datesIns(tex):
    dates.delete("1.0","end")
    dates.insert(INSERT,tex)

# >>> BOTON BUSCAR <<<
searchBut = Button(miFrame2,text="Buscar",bg="blue",fg="white",font=(10),cursor="hand2",command=lambda:linkVideo())
searchBut.grid(row=1,column=1,padx=pad,pady=pad*3)

# >>> BOTON DESCARGAR <<<
downloadBut=Button(miFrame2,text="Descargar",bg="blue",fg="white",font=(10),cursor="hand2",command=lambda:yt.descargar())
downloadBut.grid(row=1,column=0,padx=pad,pady=pad*3)

def ytRta():
    global YT
    link = ""
    link = (linkStr.get())
    linkBool = False
    if ':' in link:
        linkBool = True
    if linkBool == True:
        YT = YouTube(link)
    else: YT = YouTube('https://youtu.be/cfZlfEdMs2U')

def linkVideo():
    global link
    link = ""
    link = (linkStr.get())
    datesIns("Buscando Video... ")
    ytRta()
    datesIns("Video Encontrado !!\n")
    datesIns(f">>> {yt.titulo()} ||| by: {yt.autor()}\nEse es el video que querias?\n")

class Yt():
    def descripcion(self):
        ytRta()
        return YT.description
    def autor      (self):
        ytRta()
        return YT.author
    def titulo     (self):
        ytRta()
        return YT.title
    def duracion   (self):
        segundos = YT.length
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    def descargar  (self):
        link = ""
        link = (linkStr.get())
        ytRta()
        datesIns("Video descargado con exito!\n")
        raiz.after(10)
        YT.streams.first().download(downPath)
        datesIns(f"Archivo descargado en {downPath}")
yt=Yt()
def all():
    datesIns(yt.titulo()+"\n\n"+
             yt.autor()+"\n\n"+
             yt.duracion()+"\n\n"+
             yt.descripcion()+"\n\n")

raiz.mainloop()
