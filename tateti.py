"""Simular el juego del tatetí."""
def jugada(player,tateti,signo):
    print("juega el jugador",player)
    ban=0
    while ban==0:   
        M=int(input("ingrese primer coordenada (1, 2 o 3):"))
        if 0<M and M<4:
            N=input("ingrese segunda coordenada (A, B, o C):")
            N=N.upper()
            for i in range(1,4):
                if N==tateti[i][0]:
                    N=i
                    i=4
            if N!=str(N):
                if tateti[N][M]==" ":
                    tateti[N][M]=signo
                    ban=1
                else:
                    print("Lugar ocupado, por favor elija otro.")
            else:
                print("coordenada no encontrada, por favor elija otra")
        else:
            print("coordenada no encontrada, por favor elija otra")
    for i in range(0,len(tateti)):
        print(tateti[i])
def ganador(tateti,signo):
    ban=0
    if tateti[1][1]==signo:
        if tateti[1][2]==signo:
            if tateti[1][3]==signo:
                ban=1
        if ban==0:
            if tateti[2][1]==signo:
                if tateti[3][1]==signo:
                    ban=1
            if ban==0:
                if tateti[2][2]==signo:
                    if tateti[3][3]==signo:
                        ban=1
    if ban==0:
        if tateti[1][2]==signo:
            if tateti[2][2]==signo:
                if tateti[3][2]==signo:
                    ban=1
        if ban==0:
            if tateti[1][3]==signo:
                if tateti[2][2]==signo:
                    if tateti[3][1]==signo:
                        ban=1
                if ban==0:
                    if tateti[2][3]==signo:
                        if tateti[3][3]==signo:
                            ban=1
            if ban==0:
                if tateti[2][1]==signo:
                    if tateti[2][2]==signo:
                        if tateti[2][3]==signo:
                            ban=1
                if ban==0:
                    if tateti[3][2]==signo:
                        if tateti[3][1]==signo:
                            if tateti[3][3]==signo:
                                ban=1
                    if ban==0:
                        if tateti[2][3]==signo:
                            if tateti[1][3]==signo:
                                if tateti[3][1]==signo:
                                    ban=1
    return ban                 

    

Ban=0
while Ban==0:
    juego=[]
    juego.append([" ","1","2","3"])
    juego.append(["A","O","X","O"])
    juego.append(["B","X","O","X"])
    juego.append(["C","X","O"," "])
    for i in range(0,len(juego)):
        print(juego[i])
    ban=0
    while ban==0:
        player1=1
        signo="X"
        jugada(player1,juego,signo)
        ban=ganador(juego,signo)
        if ban==1:
            print("El jugador 1 gana.")
            R=input("¿Desea volver a jugar?:")
            R=R.lower()
            if R=="si":
                ban=0
                juego[0]=([" ","1","2","3"])
                juego[1]=(["A"," "," "," "])
                juego[2]=(["B"," "," "," "])
                juego[3]=(["C"," "," "," "])
        if ban==0:
            C=0
            for i in range(1,4):
                for j in range(1,4):
                    if juego[i][j]=="X" or juego[i][j]=="O":
                        C=C+1
            if C==9:
                print("No queda casillas libres, EMPATE.")
                R=input("¿Desea volver a jugar?:")
                R=R.lower()
                if R=="si":
                    ban=0
                    juego[0]=([" ","1","2","3"])
                    juego[1]=(["A"," "," "," "])
                    juego[2]=(["B"," "," "," "])
                    juego[3]=(["C"," "," "," "])
        if ban==0:
            player2=2
            signo="O"
            jugada(player2,juego,signo)
            ban=ganador(juego,signo)
            if ban==1:
                print("El jugador 2 gana.")
                R=input("¿Desea volver a jugar?:")
                R=R.lower()
                if R=="si":
                    ban=0
                    juego[0]=([" ","1","2","3"])
                    juego[1]=(["A"," "," "," "])
                    juego[2]=(["B"," "," "," "])
                    juego[3]=(["C"," "," "," "])
        