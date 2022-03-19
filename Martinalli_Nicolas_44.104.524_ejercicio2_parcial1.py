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
def crear_matriz2():
  vocales=["a","e","i","o","u"]
  matriz2=[]
  matriz2.append([])
  ban=0
  for k in range(0,len(vocales)):
    for i in range (0,M):
      for j in range(0,N):
        aux=matriz[i][j]
        aux=aux.lower()
        if aux[0:1]==vocales[k]:
          matriz2[ban].append(aux)
      if len(matriz2[ban])==4:
          ban=ban+1
          matriz2.append([])
    ban=ban+1
    matriz2.append([])  
  return matriz2
def mostrar_una_matriz(matriz):
  for i in range(0,len(matriz)):
    if matriz[i]!=[]:
      print(matriz[i])


matriz=cargar_matriz()
matriz2=crear_matriz2()
mostrar_una_matriz(matriz2)
