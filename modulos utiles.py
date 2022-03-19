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
def cargar_matriz():
  matriz = []
  M=int(input("ingrese cantidad de filas:"))
  #N=columnas
  N=4
  for i in range(0,M):
    matriz.append([])
    for j in range(0,N):
      A=0
      while A==0:
        X=input("ingrese nombre:")
        B=ComprobarSiEsInt(X)
        if B=="si":
          print("debe ingresar un nombre, no un numero.")
        else:
          matriz[i].append(X)
          A=1
  return matriz