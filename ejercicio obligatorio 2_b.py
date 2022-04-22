"""Dado un archivo de texto (logs.txt) que contiene información de los accesos a Internet de los
empleados de una empresa, se desea obtener, mediante la utilización de módulos, lo siguiente:
a) Listado de páginas visitadas por un usuario dado.
b) La página que tuvo mayor cantidad de visitas
c) Listar las páginas ordenadas según la cantidad total de minutos en el sitio
d) El usuario que más páginas visitó.
e) El usuario que más tiempo navegó en internet
El archivo tiene la siguiente estructura:
Fecha (Desde la posición 1 hasta la 10)
Usuario (Desde la 11 hasta la 20)
Página (Desde la 21 hasta la 40)
Minutos (Desde 41 hasta 43)"""

def Abrir_Archivo_para_lectura(Nombre_Y_Ubnicacion_Del_Archivo):
    archivo = open(Nombre_Y_Ubnicacion_Del_Archivo, "r")
    return archivo
def Cerrar_Archivo(Archivo):
    Archivo.close
def Cargar_las_lineas_en_un_vector(Archivo):
    V=Archivo.readlines()
    return V
def Extraer_informacion_de_una_ubicacion_especifica(Punto_inicial,Punto_final,linea):
    A=linea[Punto_inicial:Punto_final]
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
def EliminarEspacios(palabra):
    while " " in palabra:
        palabra=palabra.replace(" ","")
    return palabra
def Mostrar_listado_de_páginas_visitadas_por_un_usuario_dado(usuarios,paginas):
    usuario=input("ingrese el usuario para revisar que paginas visito:")
    PaginasVisitadasPorElUsuario=[]
    ban1=0
    for i in range(0,len(usuarios)):
        A=0
        if usuarios[i]==usuario:
            for j in range(0,len(PaginasVisitadasPorElUsuario)):
                if paginas[i]!=PaginasVisitadasPorElUsuario[j]:
                    A=A+1
            if A==len(PaginasVisitadasPorElUsuario):
                PaginasVisitadasPorElUsuario.append(paginas[i])
                print(paginas[i])
                ban1=1
    if ban1==0:
      print("Este usuario no visito ninguna pagina")

def BuscarCuantasVecesSeVisitoCadaPagina(paginas):
    PaginasYaTomadas=[]
    for i in range(0,len(paginas)):
        A=0
        for j in range (0,len(PaginasYaTomadas)):
            if PaginasYaTomadas[j][0]!=paginas[i]:
              A=A+1  
            else:
              PaginasYaTomadas[j][1]+=1  
        if A==len(PaginasYaTomadas):
          PaginasYaTomadas.append([])
          PaginasYaTomadas[len(PaginasYaTomadas)-1].append(paginas[i])
          PaginasYaTomadas[len(PaginasYaTomadas)-1].append(1)
    return PaginasYaTomadas

def Mostrar_la_página_que_tuvo_mayor_cantidad_de_visitas_El_usuario_que_mas_navego(PaginasYCantidadDeVisitas,mensaje1,mensaje2,mensaje3):
  MayorCantidad=PaginasYCantidadDeVisitas[0][1]
  MayorPagina=PaginasYCantidadDeVisitas[0][0]
  for i in range(0,len(PaginasYCantidadDeVisitas)):
    if PaginasYCantidadDeVisitas[i][1]>MayorCantidad:
      MayorCantidad=PaginasYCantidadDeVisitas[i][1]
      MayorPagina=PaginasYCantidadDeVisitas[i][0]
  print(mensaje1,MayorPagina,mensaje2,MayorCantidad,mensaje3)

def BuscarCuantoTiempoSeVisitoCadaPagina_NavegoCadaUsuario(paginas,minutos):
    PaginasYaTomadas=[]
    for i in range(0,len(paginas)):
        A=0
        for j in range (0,len(PaginasYaTomadas)):
            if PaginasYaTomadas[j][0]!=paginas[i]:
              A=A+1  
            else:
              PaginasYaTomadas[j][1]=PaginasYaTomadas[j][1]+minutos[i]
        if A==len(PaginasYaTomadas):
          PaginasYaTomadas.append([])
          PaginasYaTomadas[len(PaginasYaTomadas)-1].append(paginas[i])
          PaginasYaTomadas[len(PaginasYaTomadas)-1].append(minutos[i])
    return PaginasYaTomadas
def Ordenar_las_paginas_de_mayor_a_menor_segun_el_tiempo(PaginasYTiempos):
  for i in range(0,len(PaginasYTiempos)):
    for j in range(i,len(PaginasYTiempos)):
      if PaginasYTiempos[j][1]>PaginasYTiempos[i][1]:
        aux=PaginasYTiempos[i][1]
        PaginasYTiempos[i][1]=PaginasYTiempos[j][1]
        PaginasYTiempos[j][1]=aux
        aux=PaginasYTiempos[i][0]
        PaginasYTiempos[i][0]=PaginasYTiempos[j][0]
        PaginasYTiempos[j][0]=aux
  return A
def Armar_lista_de_usuarios_sin_repetidos(usuarios):
  UsuariosSinRepetir=[]
  for i in range(0,len(usuarios)):
    A=0
    for j in range(0,len(UsuariosSinRepetir)):
      if usuarios[i]!=UsuariosSinRepetir[j][0]:
        A=A+1
    if A==len(UsuariosSinRepetir):
      UsuariosSinRepetir.append([])
      UsuariosSinRepetir[len(UsuariosSinRepetir)-1].append(usuarios[i])
  return UsuariosSinRepetir
def Mostrar_el_usuario_que_más_páginas_visitó(A,usuarios,paginas):
  for i in range(0,len(A)):
    A[i].append("")
  for i in range(0,len(A)):
    for j in range(0,len(usuarios)):
      if A[i][0]==usuarios[j]:
        if A[i][1]=="":
          A[i][1]=paginas[i]
        else:
          ban=0
          for k in range(0,len(A[i])):
            if A[i][k]==paginas[j]:
              ban=1
              k=len(A[i])
          if ban==0:
            A[i].append(paginas[j])
  mayor=len(A[0])
  mayorU=A[0][0]
  for i in range(1,len(A)):
    if len(A[i])>mayor:
      mayor=len(A[i])
      mayorU=A[i][0]
  print("El usuario que mas paginas visito fue",mayorU,".Este usuario visito",mayor-1,"paginas distintas")


Nombre=input("Ingrese nombre y ubicacion del archivo a tratar:")
Archivo=Abrir_Archivo_para_lectura(Nombre)
V=Cargar_las_lineas_en_un_vector(Archivo)
Cerrar_Archivo(Archivo)
fechas=[]
usuarios=[]
paginas=[]
minutos=[]
for i in range (0,len(V)):
    A=Extraer_informacion_de_una_ubicacion_especifica(0,10,V[i])
    A=EliminarEspacios(A)
    fechas.append(A)
    A=Extraer_informacion_de_una_ubicacion_especifica(10,20,V[i])
    A=EliminarEspacios(A)
    usuarios.append(A)
    A=Extraer_informacion_de_una_ubicacion_especifica(20,40,V[i])
    A=EliminarEspacios(A)
    paginas.append(A)
    A=Extraer_informacion_de_una_ubicacion_especifica(40,43,V[i])
    A=int(A)
    minutos.append(A)
opciones=[]
opciones.append("Finalizar/salir del menu.")
opciones.append("Mostrar el listado de páginas visitadas por un usuario dado.")
opciones.append("Mostrar la página que tuvo mayor cantidad de visitas.")
opciones.append("Listar las páginas ordenadas según la cantidad total de minutos en el sitio.")
opciones.append("Mostrar el usuario que más páginas visitó.")
opciones.append("Mostrar el usuario que más tiempo navegó en internet")
opciones2=[]
banF=0
while banF==0:
    Accion=MostrarMenuYElegirOpcion(opciones)
    if Accion==0:
        banF=1
        print("gracias por utilizar mi algoritmo :)")
    else:
        if Accion==1:
            Mostrar_listado_de_páginas_visitadas_por_un_usuario_dado(usuarios,paginas)
        else:
            if Accion==2:
                A=BuscarCuantasVecesSeVisitoCadaPagina(paginas)
                mensaje1="la pagina con mas visitas fue:"
                mensaje2="con un total de"
                mensaje3="visitas"
                Mostrar_la_página_que_tuvo_mayor_cantidad_de_visitas_El_usuario_que_mas_navego(A,mensaje1,mensaje2,mensaje3)
            else:
              if Accion==3:
                A=BuscarCuantoTiempoSeVisitoCadaPagina_NavegoCadaUsuario(paginas,minutos)
                A=Ordenar_las_paginas_de_mayor_a_menor_segun_el_tiempo(A)
                print("La lista ordenada de mayor a menor segun el tiempo que se uso cada pagina es:")
                for i in range(0,len(A)):
                  print(A[i])
              else:
                if Accion==4:
                  A=Armar_lista_de_usuarios_sin_repetidos(usuarios)
                  Mostrar_el_usuario_que_más_páginas_visitó(A,usuarios,paginas)
                else:
                  if Accion==5:
                    A=BuscarCuantoTiempoSeVisitoCadaPagina_NavegoCadaUsuario(usuarios,minutos)
                    mensaje1="El usuario que mas tiempo navego fue:"
                    mensaje2="con un total de"
                    mensaje3="minutos"
                    Mostrar_la_página_que_tuvo_mayor_cantidad_de_visitas_El_usuario_que_mas_navego(A,mensaje1,mensaje2,mensaje3)

    input("Presione enter para continuar.")
print("Sesion finalizada.")