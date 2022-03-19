"""ejercicio de diagnostico 1"""
V1=[]
cantidad1=0
N="si"
B=2
C=0
print("                                 empiese a cargar el primer vector")
while N=="si":
  x=input("ingrese numero de documento y nombre completo:")
  V1.append(x)
  N=(input("desea ingresar otro usuario?:"))
  cantidad1= cantidad1+1
s=cantidad1
V2=[]
cantidad2=0
N="si"
B=2
C=0
print("                                 empiese a cargar el segundo vector")
while N=="si":
  x=input("ingrese numero de documento y nombre completo:")
  V2.append(x)
  N=input("desea ingresar otro usuario?")
  cantidad2=cantidad2+1
d=cantidad2
V3=[]
A=0
B=0
while A<cantidad1:
  C="No"
  B=0
  while B<cantidad2:
    if V1[A]==V2[B]:
      C="Si"
    B=B+1
  if C=="No":
    V3.append(V1[A])
  A=A+1
A=0
while A<cantidad2:
  C="No"
  B=0
  while B<cantidad1:
    if V2[A]==V1[B]:
      C="Si"
    B=B+1
  if C=="No":
    V3.append(V2[A])
  A=A+1
print("Vector 1=",V1)
print("Vector 2=",V2)
print("vector final =",V3)
