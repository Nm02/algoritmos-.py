"""Dado un archivo de texto mostrar la cantidad de vocales y consonantes que contiene. Usar las
funciones utilizadas en el TP 1."""
def DesarmarLinea(B):
    caracteres=[]
    ban1=len(B)
    ban2=0
    while ban2<ban1:
        x=B[ban2:ban2+1]
        caracteres.append(x)
        ban2=ban2+1
    return caracteres
def ContarVocales(caracteres,Cvocales):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    
    A=0
    B=len(caracteres)
    D=len(vocales)
    while A<B:
        C=0
        contador=0
        while C<D:
            if caracteres[A]==vocales[C]:
                contador=1
            C=C+1
        if contador==1:
            Cvocales=Cvocales+1
        A=A+1
    return Cvocales
def ContarConsonantes(caracteres,Cconsonantes):
    consonantes=["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","x","y","z"]
    A=0
    B=len(caracteres)
    D=len(consonantes)
    while A<B:
        C=0
        contador=0
        while C<D:
            ban=consonantes[C].lower()
            if caracteres[A]==consonantes[C] or caracteres[A]==ban :
                contador=1
            C=C+1
        if contador==1:
            Cconsonantes=Cconsonantes+1
        A=A+1
    return Cconsonantes

archivo=input("ingrese ubicacion y nombre del archivo:")
archivo=open(archivo,"r")
V=archivo.readlines
lineas=[]
linea=archivo.readline()
while linea!="":
    lineas.append(linea)
    linea=archivo.readline()

vocales=0
consonantes=0
for i in range(0,len(lineas)):
    caracteres=DesarmarLinea(lineas[i])
    vocales=ContarVocales(caracteres,vocales)
    consonantes=ContarConsonantes(caracteres,consonantes)

archivo.close
print("hay ",vocales," vocales")
print("hay ",consonantes," consonantes")

