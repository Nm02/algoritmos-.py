"""19 El camino de un laberinto está almacenado en una matriz compuesta de 0
y 1 (el uno indica que es una posición válida del laberinto). Desarrollar un programa que
permita cargar el camino del laberinto y jugar a encontrarlo."""
def AgregarElementoAlVector(A,b):
  A.append(b)
ban=0
#elegir si crear o seleccionar laberionto:
while ban==0:
  print("por favor elija una de estas opciones (escriba el numero de la opcion para elegirla)")
  print("1. crear un laberinto.")
  print("2. elegir un laberinto ya creado.")
  a=int(input(""))
  if a==1:
    ban=1
  else:
    if a==2:
      ban=1
    else:
      print("la opcion elegida no exista, por favor elija entre 1 y 2")
      ban=0
letras=[]
AgregarElementoAlVector(letras," ")
AgregarElementoAlVector(letras,"a")
AgregarElementoAlVector(letras,"b")
AgregarElementoAlVector(letras,"c")
AgregarElementoAlVector(letras,"d")
AgregarElementoAlVector(letras,"e")
AgregarElementoAlVector(letras,"f")
AgregarElementoAlVector(letras,"g")
AgregarElementoAlVector(letras,"h")
AgregarElementoAlVector(letras,"i")
AgregarElementoAlVector(letras,"j")
#crear laberinto
if a==1:
  colmax=11
  filmax=11
  laberinto = []
  for i in range(0,11):
    laberinto.append([])
    for j in range(0,11):
      X="0"
      laberinto[i].append(X)
  for i in range(0,11):
    laberinto[0][i]=str(i)
  for i in range(0,11):
    laberinto[i][0]=letras[i]
  print("cargar laberinto.")
  print("1. elegir punto de salida.")
  print("las siguientes casillas estan proibidas")
  print("a1")
  print("a10")
  print("j1")
  print("j10")
  for i in range(0,11):
    print(laberinto[i])
  ban2=0
  #Punto de salida:
  while ban2==0:
    columna=int(input("ingrese columna en la que desee empezar:")) 
    fila=input("ingrese fila en la que desee empezar:")
    fila=fila.lower()
    if columna==1 and fila=="a":
        print("coordenadas ingresadas no validas.")
    else:
        if columna==1 and fila=="j":
            print("coordenadas ingresadas no validas.")
        else:
            if columna==10 and fila =="a":
                print("coordenadas ingresadas no validas.")
            else:
                if columna==10 and fila=="j":
                    print("coordenadas ingresadas no validas.")
                else:
                    if columna<11:
                        ban3=0
                        for i in range(1,11):
                            if laberinto[i][0]==fila:
                                ban3=1
                                ban2=1
                                t=i
                                i=11
                        if ban3==0:
                            print("coordenadas ingresadas no validas.")
                    else:
                        print("coordenadas ingresadas no validas.")
  MM=columna
  NN=t
  laberinto[NN][MM]='>'
  print("2. elegir punto de llegada.")
  print("las siguientes zonas entan bloqueadas")
  print("a1")
  print("a10")
  print("j1")
  print("j10")
  print(str(NN)+str(MM))
  for i in range(0,11):
    print(laberinto[i])
  ban2=0
  #punto de llegada
  while ban2==0:
    columna=int(input("ingrese columna en la que desea finalizar:")) 
    fila=input("ingrese fila en la que desee finalizar:")
    fila=fila.lower()
    if columna==1 and fila=="a":
        print("coordenadas ingresadas no validas.")
    else:
        if columna==1 and fila=="j":
            print("coordenadas ingresadas no validas.")
        else:
            if columna==10 and fila =="a":
                print("coordenadas ingresadas no validas.")
            else:
                if columna==10 and fila=="j":
                    print("coordenadas ingresadas no validas.")
                else:
                    if columna<11:
                        ban3=0
                        p=0
                        for i in range(1,11):
                            if laberinto[i][0]==fila:
                                p=i
                                i=11
                        if columna==MM and p==NN:
                            print("coordenadas ingresadas no validas.")
                        else:
                            ban3=1
                            ban2=1
                        if ban3==0:
                            print("coordenadas ingresadas no validas.")       
                    else:
                        print("coordenadas ingresadas no validas.")
  m=columna
  n=p
  laberinto[n][m]='Y'
  print("3. cargar el camino principal")
  print("las siguientes zonas estan bloqueadas:")
  print("fila a")
  print("fila j")
  print("columna 1")
  print("columna 10")
  print(str(NN)+str(MM))
  print(str(p)+str(columna))
  print("ADVERTENCIA:")
  print("si usted crea un camino que este incompleto,")
  print("no podra disfrutar del juego, pues no podra")
  print("completar el laverinto.")
  ban=0
  #cargar casillas transitables del laberinto
  while ban==0:
        #Mostrar laberinto
        for i in range(0,11):
            print(laberinto[i])
        ban4=0
        columna=int(input("ingrese columna de la casilla transitable:"))
        if columna==1 or columna==0 or columna==10 or columna>=11:
            print("esta columna esta bloqueada")
        else:
            fila=input("ingrese fila de la casilla transitable:")
            if fila=="a" or fila=="j":
                print("esta casilla esta bloqueada")
            else:
                ban2=0
                for i in range(1,11):
                    if laberinto[i][0]==fila:
                        t=i
                        ban2=1
                        i=11
                if ban2==0:
                    print("esta esta bloqueada esta disponible.")
                if t==NN and columna==MM:
                    print("esta casilla no esta disponible.")
                else:
                    if t==n and columna==m:
                        print("esta casilla no esta disponible.")
                    else:
                        ban4=1
        if ban4==1:
            laberinto[t][columna]=" "
        ban3=input("(responda si o no) ¿desea ingresar otra casilla transitable?:")
        ban3=ban3.lower()
        if ban3!="si":
            ban=1
#elegir laberinto predeterminado
if a==2:
    p=[]
    M=[]
    N=[]
    fil=[]
    col=[]
    p.append([])
    p[0].append(["0","0","0","0","0","0","0","0","0","0",">","0","0","0","0"])
    p[0].append(["Y"," "," ","0","0","0","0","0","0","0"," "," "," "," ","0"])
    p[0].append(["0","0"," ","0"," "," "," "," "," "," ","0"," ","0"," ","0"])
    p[0].append(["0","0"," ","0"," ","0","0","0","0"," "," "," "," "," ","0"])
    p[0].append(["0","0"," ","0"," ","0","0","0","0","0"," ","0"," ","0","0"])
    p[0].append(["0","0"," ","0"," ","0","0"," "," "," "," ","0"," "," ","0"])
    p[0].append(["0","0"," ","0"," "," ","0"," ","0","0","0"," ","0"," ","0"])
    p[0].append(["0","0"," "," ","0"," ","0"," ","0","0","0"," ","0"," ","0"])
    p[0].append(["0","0","0"," "," "," ","0"," "," "," "," "," "," "," ","0"])
    p[0].append(["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"])
    M.append(15)
    N.append(10)
    col.append(10)
    fil.append(0)
    p.append([])
    p[1].append(["0","0","0","0","0","0","0","0","0","0"])
    p[1].append(["0"," "," "," ","0"," "," "," ","0","0"])
    p[1].append(["0","0"," ","0","0"," ","0"," "," ","0"])
    p[1].append(["0","0"," "," "," "," ","0","0"," ","0"])
    p[1].append(["0","0"," ","0","0","0","0","0"," ","0"])
    p[1].append(["0","0"," ","0",">"," "," "," "," ","0"])
    p[1].append(["0","0"," ","0","0","0","0"," ","0","0"])
    p[1].append(["0","0"," ","0","0"," "," "," ","0","0"])
    p[1].append(["Y"," "," ","0","0","0","0"," "," ","0"])
    p[1].append(["0","0","0","0","0","0","0","0","0","0"])
    M.append(10)
    N.append(10)
    col.append(4)
    fil.append(5)
    p.append([])
    p[2].append(["0","0","0","0",">","0","0","0","0","0"])
    p[2].append(["0"," ","0","0"," "," ","0","0","0","0"])
    p[2].append(["0"," "," "," "," ","0"," "," "," ","0"])
    p[2].append(["0","0","0","0"," ","0"," ","0"," ","0"])
    p[2].append(["0"," "," "," "," "," "," ","0"," ","0"])
    p[2].append(["0"," ","0","0","0","0","0","0"," ","0"])
    p[2].append(["0"," ","0","0","0","0","0","0"," ","0"])
    p[2].append(["0","0","0","0","0"," "," "," "," ","0"])
    p[2].append(["0","0"," ","0","0"," ","0","0","0","0"])
    p[2].append(["0","0"," ","0","0"," "," "," ","0","0"])
    p[2].append(["0"," "," "," ","0","0","0"," ","0","0"])
    p[2].append(["0"," ","0"," "," "," ","0"," "," ","0"])
    p[2].append(["0"," ","0"," ","0"," ","0","0"," ","0"])
    p[2].append(["0"," ","0"," ","0"," "," "," "," ","0"])
    p[2].append(["0","0","0","Y","0","0","0","0","0","0"])
    M.append(10)
    N.append(15)
    col.append(4)
    fil.append(0)
    ban=0
    #elejir cual labrinto predeterminado jugar
    while ban==0:
        print("Elija uno de los laberintos predeterminados:")
        print("(para seleccionar un laberionto se debe")
        print("escribir el numero de la opcion)")
        for i in range(0,len(p)):
            print("laberinto N°:",i+1)
            for j in range(0,N[i]):
                print(p[i][j])
        ban2=0
        while ban2==0:
            print("¿con que laberinto vas a jugar?")
            x=int(input())
            x=x-1
            if x<len(p):
                jugar=x
                ban=1
                ban2=1
                print("laberinto ",x+1," seleccionado")
                laberinto=p[x]
                MM=col[x]
                NN=fil[x]
                AAA=M[x]
                colmax=AAA
                AAA=N[x]
                filmax=AAA
            else:
                print("laberindo no encontrado, por favor cargue un numero entre ",1," y ",len(p))
ban=0
#Jugar
while ban==0:
    tutorial=input("¿Desea leer el tutorial?:")
    tutorial=tutorial.lower()
    #tutorial
    if tutorial=="si":
        print("                    INSTRUCCIONES.")
        print(" 1.Para jugar este juego se utilizan los siguientes controles:")
        print("             arriba=8")    
        print("             abajo=2")
        print("             izquierda=4")
        print("             derecha=6")
        print("             rendirse=5")
        print("  2.Su personje tiene esta forma: >.")
        print("  3.Solo puede moverse arriba, abajo, a la izquieda y a la derecha.")
        print("los movimientos en diagonal no son posibles, y solo es posible")
        print("moverse una casilla a la vez.")
        print("  4.El objetivo del juego es terminar el laberinto. Para eso es ")
        print("necesario encontrar y tomar el trofeo, el cual tiene el siguiente ")
        print("aspecto: Y.")
        print("  5.Debes mover tu personaje por el camino, el cual esta formado de")
        print("casillas en blanco.")
        print("  6.El personaje no puede pasar sobre las paredes, las cuales estan")
        print("formadas por casillas con la forma: 0.")
        print("Ahora que sabes las reglas, solo queda decir:")
        print("¡Que disfrutes de tu juego!")
    ban2=0
    #movimientos
    while ban2==0:
        movimiento=0
        for i in range(0,len(laberinto)):
            print(laberinto[i])
        movimiento=int(input("haga su movimiento:"))
        #arriba
        if movimiento==8:
            if NN-1>-1:
                if laberinto[NN-1][MM]=="0":
                    print("movimiento imposible, realice otro movimiento.")
                else:
                    if laberinto[NN-1][MM]==" ":
                        laberinto[NN][MM]=" "
                        laberinto[NN-1][MM]=">"
                        NN=NN-1
                    else:
                        if laberinto[NN-1][MM]=="Y": 
                            ban2=1
                            ban=1
                            laberinto[NN][MM]=" "
                            laberinto[NN-1][MM]=">"
                            NN=NN-1
                            for i in range(0,len(laberinto)):
                                print(laberinto[i])
                            print("¡FELICIDADES, GANASTE!")
                        else:
                            print("movimiento imposible, realice otro movimiento.")
            else:
                print("movimiento imposible, realice otro movimiento.")
        else:
            #abajo
            if movimiento==2:
                if NN+1<filmax:
                    if laberinto[NN+1][MM]=="0":
                        print("movimiento imposible, realice otro movimiento.")
                    else:
                        if laberinto[NN+1][MM]==" ":
                            laberinto[NN][MM]=" "
                            laberinto[NN+1][MM]=">"
                            NN=NN+1
                        else:
                            if laberinto[NN+1][MM]=="Y":
                                print("FELICIDADES;GANASTE")
                                ban2=1
                                ban=1
                                laberinto[NN][MM]=" "
                                laberinto[NN+1][MM]=">"
                                NN=NN+1
                                for i in range(0,len(laberinto)):
                                    print(laberinto[i])
                            else:
                                print("movimiento imposible, realice otro movimiento.")
                else:
                    print("movimiento imposible, realice otro movimiento.")
            else:
                #izquierda
                if movimiento==4:
                    if MM-1>-1:
                        if laberinto[NN][MM-1]=="0":
                            print("movimiento imposible, realice otro movimiento.")
                        else:
                            if laberinto[NN][MM-1]==" ":
                                laberinto[NN][MM]=" "
                                laberinto[NN][MM-1]=">"
                                MM=MM-1
                            else:
                                if laberinto[NN][MM-1]=="Y":
                                    ban2=1
                                    ban=1
                                    laberinto[NN][MM]=" "
                                    laberinto[NN][MM-1]=">"
                                    MM=MM-1
                                    for i in range(0,len(laberinto)):
                                        print(laberinto[i])
                                    print("¿FELICIDADES, GANASTE!")
                                else:
                                    print("movimiento imposible, realice otro movimiento.")
                    else:
                        print("movimiento imposible, realice otro movimiento.")
                else:
                    #derecha
                    if movimiento==6:
                        print("si")
                        if MM+1<colmax:
                            if laberinto[NN][MM+1]=="0":
                                print("movimiento imposible, realice otro movimiento.")
                                print("2")
                            else:
                                if laberinto[NN][MM+1]==" ":
                                    laberinto[NN][MM]=" "
                                    laberinto[NN][MM+1]=">"
                                    MM=MM+1
                                else:
                                    if laberinto[NN][MM+1]=="Y":
                                        ban2=1
                                        ban=1
                                        laberinto[NN][MM]=" "
                                        laberinto[NN][MM+1]=">"
                                        MM=MM+1
                                        for i in range(0,len(laberinto)):
                                            print(laberinto[i])
                                        print("¡FELICIDADES, GANASTE!")
                                    else:
                                        print("movimiento imposible, realice otro movimiento.")
                        else:
                            print("movimiento imposible, realice otro movimiento.")
                    else:
                        #rendirse
                        if movimiento==5:
                            X=input("¿Seguro que desea rendirse?:")
                            if X=="si":
                                print("Perdiste :(")
                                ban2=1
                        #error
                        else:
                            print("movimiento imposible, realice otro movimiento.")