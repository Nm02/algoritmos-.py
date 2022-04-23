#elimina los espacion en una palabra
from tkinter.filedialog import dialogstates


def EliminarEspacios(palabra):
    while " " in palabra:
        palabra=palabra.replace(" ","")
    return palabra

#abre el archivo, carga sus lineas en un vector y organiza sus filas y columnas en un diccionario bidimencional(matriz).
#Devuelve la matriz
def Leer_Archivo(file):
    matriz={"fecha":[],"usuario":[],"pagina":[],"minutos":[]}
    with open(file,"r") as f:
        Archivo=f.readlines()
        for linea in Archivo:
            matriz["fecha"].append(EliminarEspacios(linea[0:10]))
            matriz["usuario"].append(EliminarEspacios(linea[10:20]))
            matriz["pagina"].append(EliminarEspacios(linea[20:40]))
            matriz["minutos"].append(int(EliminarEspacios(linea[40:43])))
    return matriz

#Se ingres la lista de usuarios y la lista de paginas. busca las paginas que visito el ususario. Si no esta en la lista
#la agrega y se pone un contador en 1, si si esta se aumenta el contador de dicha pagina en 1. luego muestra la lista
#Si no encuentra al usuario en la lista, muestra un mensaje diciendo que no se encontro el usuario.  
def Mostrar_listado_de_páginas_visitadas_por_un_usuario_dado(usuarios,paginas):
    usuario=input("ingrese el usuario para revisar que paginas visito:")
    PaginasVisitadasPorElUsuario=[[],[]]
    ban1=0
    for i in range(0,len(usuarios)):
        A=0
        if usuarios[i]==usuario:
            for j in range(0,len(PaginasVisitadasPorElUsuario[0])):
                if paginas[i]!=PaginasVisitadasPorElUsuario[0][j]:
                    A=A+1
                else:
                    PaginasVisitadasPorElUsuario[1][j]+=1
            if A==len(PaginasVisitadasPorElUsuario[0]):
                PaginasVisitadasPorElUsuario[0].append(paginas[i])
                PaginasVisitadasPorElUsuario[1].append(1)
                ban1=1
    if ban1==0:
        print("Este usuario no visito ninguna pagina")
    else:
        for i in range(0,len(PaginasVisitadasPorElUsuario[0])):
            print(PaginasVisitadasPorElUsuario[0][i]," ",PaginasVisitadasPorElUsuario[1][i]," vaces")

#Se ingresa la lista de las paginas, y se devuelve una lista con las paginas y cuantas veces se visito cada una.
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

#Compara la cantidad de veces que se visito cada pagina, y muestra la pagina mas visitada. 
#Se ingresa la lista de paginas
def Mostrar_pagina_mas_visitada(paginas):
    cantidad=BuscarCuantasVecesSeVisitoCadaPagina(paginas)
    mayor=cantidad[0]
    for pagina in cantidad:
        if pagina[1]>mayor[1]:
            mayor=pagina
    print("La pagina que mas se visito fue ",mayor[0],", con",mayor[1]," visitas")

#Se ingresan las listas de paginas y minutos. se crea una lista para ver cuando se repiten. si se repiten se suma el
#tiempo que se visito segun la lista de minutos. si no esta en la lista, se agrega la pagina los minutos. 
#se devuelve la lista de cada pagina y el total de minutos (PaginasYaTomadas)
def Buscar_tiempo_por_pagina(paginas,minutos):
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
    print(PaginasYaTomadas)
    return PaginasYaTomadas

#Se ingresan las listas de paginas y minutos, se la ordena con el metodo de ordenamiento por seleccion y 
#se la muestra ordenada
def Mostrar_lista_tiempo_ordenada(paginas,minutos):
    list_pag_min=Buscar_tiempo_por_pagina(paginas,minutos)
    for i in range(len(list_pag_min)):
        for j in range(i,len(list_pag_min)):
            if list_pag_min[j][1]>list_pag_min[i][1]:
                aux=list_pag_min[j][0]
                list_pag_min[j][0]=list_pag_min[i][0]
                list_pag_min[i][0]=aux
                aux=list_pag_min[j][1]
                list_pag_min[j][1]=list_pag_min[i][1]
                list_pag_min[i][1]=aux
    for i in range(len(list_pag_min)):
        print(list_pag_min[i][0]," ",list_pag_min[i][1])

#Se ingresa una nueva fecha con el formato que se necesita
def ingrese_fecha():
    while True:
        dia=int(input("ingrese dia:"))
        if dia>0 and dia<32:
            if dia<10:
                dia="0"+str(dia)
            else:
                dia=str(dia)
            while True:
                mes=int(input("ingrese mes:"))
                if mes>0 and mes<13:
                    if mes<10:
                        mes="0"+str(mes)
                    else:
                        mes=str(mes)
                    while True:
                        año=int(input("ingrese año:"))
                        if 2000<año<2050:
                            return dia+"/"+mes+"/"+str(año)
                        else:
                            print("Ingrese un alo valido(ente 2001 y 2049)")
                else:
                    print("ingrese un numero entre 1 y 12.")
        else:
            print("ingrese un numero entre 1 y 31.")

#Ingresa un usuario con el formato necesario
def ingrese_usuario():
    while True:
        usuario=input("ingrese nombre de usuario:")
        if 0<len(usuario)<11:
            for i in range(len(usuario),10):
                usuario+=" "
            return usuario
        else:
            print("Ingrese un nombre de usuario con hasta 10 caracteres")
    

#Se ingresa el nombre de la pagina y se la convierte para darle el formato adecuado
def ingrese_pagina():
    12
    while True:
        pagina=input("Ingrese el nombre de la pagina (no incluya www. ni .com):")
        if 0<len(pagina)<13:
            pagina="www."+pagina+".com"
            for i in range(len(pagina),20):
                pagina+=" "
            return pagina
        else:
            pagina("El nombre debe tener entre 1 y 12 caracteres.")
    

#Se carga el tiepo en minutos.
def ingrese_timepo():
    while True:
        tiempo=int(input("Ingrese el tiempo en minutos:"))
        if 0<tiempo<999:
            tiempo=str(tiempo)
            for i in range(len(tiempo),3):
                tiempo+=" "
            return tiempo
        else:
            print("Ingrese un timepo valido")

#Escribe un nuevo registro de visita de pagina de un usuario
def Agregar_registro(file):
    with open(file,"r+") as f:
        f.readlines()
        f.write("\n")
        f.write(ingrese_fecha())
        f.write(ingrese_usuario())
        f.write(ingrese_pagina())
        f.write(ingrese_timepo())

# file="archivos_de_prueba\\logs.txt"
# tabla=Leer_Archivo(file)
# Mostrar_listado_de_páginas_visitadas_por_un_usuario_dado(tabla["usuario"],tabla["pagina"])
# Mostrar_pagina_mas_visitada(tabla["pagina"])
# Mostrar_lista_tiempo_ordenada(tabla["pagina"],tabla["minutos"])
# Agregar_registro(file)
