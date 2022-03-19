"""La 3 opcion es ver que documentos hay guardados en la carpeta y
a partir de eso borrarlos leerlos o si quiere modificar los datos esto quieres
decir que en el archivo de .txt se agregaria lo que quiera escribir esa persona 
y lo mismo para el excel"""
from os import remove
remove
def ComprobarSiEsInt(A):
  ban=1
  try:
    A=int(A)
  except:
    ban=0
  if ban==1:
    B="si"
  else:
    B="No"
  return B
def MostrarMenuYElegirOpcion(opciones):
  print("menu:")
  for i in range(0,len(opciones)):
    print(i,opciones[i])
  ban=0
  while ban==0:
    print("A continuacion escriba el numero de la opcion para elegirla:")
    A=input()
    B=ComprobarSiEsInt(A)
    if B=="si":
      A=int(A)
      if A<len(opciones) and -1<A:
        ban=1
      else:
        print("ingrese un numero que este entre las opciones.")
    else:
      print("debe ingresar un numero.")
  return(A)
menu2=[]
menu2.append(". volver al menu principal.")
menu2.append(". Borrar archivo.")
menu2.append(". leer archivo.")
menu2.append(". agregar algo al archivo.")
import os
BanMenu2=0
while BanMenu2==0:
    contenido = os.listdir("/Users/Usuario00/Documents/Nico/algoritmos/prueba")
    print(len(contenido))
    ruta="/Users/Usuario00/Documents/Nico/algoritmos/prueba/"
    print("lista de archivos en la carpeta")
    for i in range(0,len(contenido)):
        print(contenido[i])
    N=MostrarMenuYElegirOpcion(menu2)
    if N==0:
        BanMenu2=1
    else:
        if N==1:
            print("Elija que archivo desa borrar:")
            T=MostrarMenuYElegirOpcion(contenido)
            T=ruta+contenido[T-1]
            remove(T)
        else:
            if N==2:
                print("Elija que archivo leer:")
                T=MostrarMenuYElegirOpcion(contenido)
                T=ruta+contenido[T]
                archivo = open(T, "r")
                print(archivo.read())
                archivo.close() 
            else:
                if N==3:
                    print("Elija el archivo al que desee agregar algo:")
                    T=MostrarMenuYElegirOpcion(contenido)
                    T=ruta+contenido[T]
                    archivo = open(T, "w")
                    text=input("Escriba lo que desee agregar al archivo: ")
                    archivo.write(text)
                    archivo.close() 
    input("pulse enter para continuar.")