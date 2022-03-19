"""Restar 2 numeros binarios con complemento autentico"""
A=int(input("ingrese A(numero binario al que se le resta)"))
B=int(input("ingrese B(numero binario que se resta)"))
a=[]
b=[]
CA=0
CB=0
if A==0:
  a.append(0)
  CA=1
else:
  while 0<A:
    i=A%10
    A=A//10
    a.append(i)
    CA=CA+1
while 0<B:
  i=B%10
  B=B//10
  b.append(i)
  CB=CB+1
if len(a)>len(b):
  c=len(a)-len(b)
  for i in range(0,c):
    b.append(0)
print(b)
for i in range(0,len(b)):
  if b[i]==0:
    b[i]=1
  else:
    b[i]=0
b.append(0)
j=1
print(b)
for i in range(0,len(b)):
  if j==0:
    i=len(b)
  else:
    if b[i]==0:
      b[i]=1
      j=0
    else:
      b[i]=0
      j=1
print(b)
if len(a)>=len(b):
  C=len(a)
else:
  c=len(b)-len(a)
  for i in range(0,c):
    a.append(0)
  C=len(b)
ban=0
final=[]
for i in range(0,C):
  if a[i]==0:
    if b[i]==0:
      if ban==0:
        final.append(0)
      else:
        final.append(1)
        ban=0
    else:
      if ban==0:
        final.append(1)
      else:
        final.append(0)
        ban=1
  else:
    if b[i]==0:
      if ban==0:
        final.append(1)
      if ban==1:
        final.append(0)
        ban=1
    else:
      if ban==0:
        final.append(0)
        ban=1  
      else:
        final.append(1)
        ban==0
for i in range(0,len(final)):
  final[i]=str(final[i])
if final[len(final)-1]=="1":
  final[len(final)-1]="-"
else:
  final[len(final)-1]=""
FINAL=""
c=len(final)
for i in range(0,len(final)):
  c=c-1
  FINAL=FINAL+final[c]
FINAL=int(FINAL)
print("Resultado:",FINAL)