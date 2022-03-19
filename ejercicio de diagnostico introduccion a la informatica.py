"""ejercicio de diagnostico 1"""
V1=[]
cantidad1=0
N=1
B=2
C=0
while N<B and N>C:
  x=int(input("ingrese numero de documento y nombre completo:"))
  V1.append(x)
  N=int(input("si desea ingresar otro usuario ingrese 1, de lo contrario ingrese 2:"))
  cantidad1= cantidad1+1
s=cantidad1
V2=[]
cantidad2=0
N=1
B=2
C=0
while N<B and N>C:
  x=int(input("ingrese numero de documento y nombre completo:"))
  V2.append(x)
  N=int(input("si desea ingresar otro usuario ingrese 1, de lo contrario ingrese 2:"))
  cantidad2=cantidad2+1
d=cantidad2
V3=[]
for i in range (0,s-1):
  F=0
  for j in range (0,d-1):
    if V1[i]<V2[j] or V1[i]>V2[j]:
      F=F+1
  if F==d:
    V3.append(V1[i])

for i in range (0,d-1):
  F=0
  for j in range (0,s-1):
    if V2[i]<V1[j] or V2[i]>V1[j]:
      F=F+1
  if F==d:
    V3.append(V2[i])
print("V1[0]=",V1[0])
print("Vector 1=",V1)
print("Vector 2=",V2)
print("cantidad 1=",cantidad1)
print("cantidad 2=",cantidad2)
print("vector final =",V3)
