"""ejercicio 1"""
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
def Mostrar_el_listado_a_alumnos_ordenados_por_apellidos_y_nombres(archivo):
    archivo_ordenado=sorted(archivo)
    print("la lista de nombres, ordenados alfabeticamente pr sus apellidos es:")
    for i in range(0,len(archivo_ordenado)):
        print(archivo_ordenado[i][0],archivo_ordenado[i][1])
def mostrar_alumnos_con_nota_menor_a_6(archivo,ubicaion_de_la_nota):
    print("lista de alumnos desaprobados:")
    for i in range(0,len(archivo)):
        archivo[i][ubicaion_de_la_nota]=float(archivo[i][ubicaion_de_la_nota])
        if archivo[i][ubicaion_de_la_nota]<6:
            print(archivo[i][0],archivo[i][1],"desaprobo con",archivo[i][ubicaion_de_la_nota],"puntos")
def mostrar_promocionados(archivo):
    print("A continuacion ingrese ubicaion donde desea crar el archivo “promocion.txt”:")
    A=input()
    promocion=A+"/promocion.txt"
    promocion=open(promocion,"w")
    promocion.write("la lista de alumnos promocionados es:\n")
    print("la lista de alumnos promocionados es:")
    for i in range(0,len(archivo)):
        archivo[i][2]=int(archivo[i][2])
        if archivo[i][2]>=80:
            archivo[i][3]=float(archivo[i][3])
            if archivo[i][3]>=6:
                archivo[i][4]=float(archivo[i][4])
                if archivo[i][4]>=6:
                    A="El alumno "+archivo[i][0]+" "+archivo[i][1]+" promociono."
                    print(A)
                    A=A+"\n"
                    promocion.write(A)
                    
    promocion.close()


A=input("ingrese nombre, ubicacion, y extencion del archivo 1:")
A=Cargar_las_lineas_en_un_vector(A)
archivo=Separar_por_las_comas(A)
menu=[]
menu.append("salir/finalizar.")
menu.append("Mostrar el listado a alumnos ordenados por apellidos y nombres.")
menu.append("Mostrar los alumnos desaprobaron el primer parcial (obtuvieron\n  nota menor a 6) y deben rendir recuperatorio.")
menu.append("Mostrar los alumnos que desaprobaron en segundo parcial (obtuvieron\n  nota menor a 6) y deben rendir el recuperatorio.")
menu.append("Generar el archivo “promocion.txt” que contenga a los alumnos que\n  lograron promocionar la materia, es decir, que la asistencia sea mayor o\n  igual al 80%, y que hayan aprobado ambos parciales (nota superior o igual a 6)")
accion=1
while accion!=0:
    accion=MostrarMenuYElegirOpcion(menu)
    if accion==1:
        Mostrar_el_listado_a_alumnos_ordenados_por_apellidos_y_nombres(archivo)
    else:
        if accion==2:
            mostrar_alumnos_con_nota_menor_a_6(archivo,3)
        else:
            if accion==3:
                mostrar_alumnos_con_nota_menor_a_6(archivo,4)
            else:
                if accion==4:
                    mostrar_promocionados(archivo)
    if accion!=0:
        input("precione enter para continuar")
print("gracias por usar mi programa.")