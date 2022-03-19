"""practica para parcial 1 lenguajes"""
def Cargar_las_lineas_en_un_vector(Nombre_Y_Ubnicacion_Del_Archivo):
    archivo=open(Nombre_Y_Ubnicacion_Del_Archivo,"r")
    V=archivo.readlines()
    archivo.close
    for i in range(0,len(V)):
        while "\n" in V[i]:
            V[i]=V[i].replace("\n","")
    return V
def Separar_por_las_comas(V):
    A=[]
    for i in range(0,len(V)):
        A.append([])
        C=V[i]
        A[i]=C.split(",")
    return A
def Comparacion_de_2_vectores_segun_1_elemento_de_cada_vector(A,B):
    dif=[]
    ig=[]
    for i in range(0,len(A)):
        ban=0
        for j in range(0,len(B)):
            if A[i][0]==B[j][0]:
              ban=1
        if ban==0:
            print("El cliente",A[i][0],"del archivo1 no está en el archivo2.")
            ban2=""
            for i in range(0,len(A[i][0])):
              ban2=ban2+A[i][0]
            ban2=ban2+"esta en el archivo1 pero no está en el archivo2."
            dif.append(ban2)
    for i in range(0,len(B)):
        ban=0
        for j in range(0,len(A)):
            if B[i][0]==A[j][0]:
                ban=1
        if ban==0:
            print("El cliente",B[i][0],"del archivo2 no está en el archivo1.")
            for i in range(0,len(B[i][0])):
              ban2=ban2+B[i][0]
            ban2=ban2+"esta en el archivo1 pero no está en el archivo2."
            dif.append(ban2)
def Comparacion_de_2_vectores_segun_2_elementos_de_cada_vector(A,B):
    dif=[]
    ig=[]
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            if A[i][0]==B[j][0]:
                if A[i][2]!=B[j][2]:
                  ban2=A[i][0]+"esta en  ambos archivos, pero sus saldos son diferentes."
                  dif.append(ban2)
    return dif
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
  print("Menu/opciones:")
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


menu=[]
menu.append("salir/finalizar.")
menu.append("Buscar que clientes que esten en el archivo 1 pero no en el archivo 2.")
menu.append("Buscar clientes que esten en ambos archivos, pero que sus sueldos sean diferentes.")
A=input("ingrese nombre, ubicacion, y extencion del archivo 1:")

A=Cargar_las_lineas_en_un_vector(A)
B=input("ingrese nombre, ubicacion, y extencion del archivo 2:")
B=Cargar_las_lineas_en_un_vector(B)
A=Separar_por_las_comas(A)
B=Separar_por_las_comas(B)
diferencias=[]
diferencias_2=[]
diferencias_1=[]
Accion=1
while Accion!=0:
    Accion=MostrarMenuYElegirOpcion(menu)

    if Accion==1:
        diferencias_1=Comparacion_de_2_vectores_segun_1_elemento_de_cada_vector(A,B)
    else:
        if Accion==2:
            diferencias_2=Comparacion_de_2_vectores_segun_2_elementos_de_cada_vector(A,B)
dif=open(archivo =open("/Users/Usuario00/Documents/Nico/algoritmos/archivos de prueba/dif.txt","w"))
for i in range(0,len(diferencias_1)):
    dif.write(diferencias1[i],"\n")
for i in range(0,len(diferencias_2)):
    dif.write(diferencias_2[i],"\n")
dif.close()
