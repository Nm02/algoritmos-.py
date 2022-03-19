"""Dado un archivo de texto, mostrar en pantalla la línea más larga del archivo (la línea que contiene más
caracteres) y la ubicación dentro del archivo (el número de la línea)"""
def ContarCaracteres(A):
    CantidadDeCaracteres=len(A)
    return CantidadDeCaracteres

archivo=input("ingrese ubicacion y nombre del archivo:")
archivo=open(archivo,"r")
V=archivo.readlines
lineas=[]
linea=archivo.readline()
while linea!="":
    lineas.append(linea)
    linea=archivo.readline()
CPL=[]
CPL.append(ContarCaracteres(lineas[0]))
mayor=CPL[0]
LineaMayor=0
for i in range(1,len(lineas)):
    CPL.append(ContarCaracteres(lineas[i]))
    if mayor<CPL[i]:
        mayor=CPL[i]
        LineaMayor=i
print("La linea con mas caracteres es la linea N° ",LineaMayor,"(se empiesa a contar desde la linea 0).")
print("El contenido de esta linea es:")
print(lineas[LineaMayor])
print("Esta linea tiene",CPL[LineaMayor],"caracteres.")





