def existe(archivo):
    A=archivo
    archivo=archivo+".txt"
    try:
        F=open(archivo,"r")
        F.close()
        
        F=open(archivo,"a")
        F.write(A+"\n")
        F.close()
    except(Exception):
        F=open(archivo,"w")
        F.write(A+"\n")
        F.close()


banco1="macro"
banco2="rio"
banco3="macro"

existe(banco1)
existe(banco2)
existe(banco3)

print("hola")