"""dado un texto mostrarlo sin vocales"""
texto=input("ingrese el texto:")
B=len(texto)
vocales=["a","e","i","o","u","A","E","I","O","U"]
A=0
Caracteres=[]
while A<B:
  x=texto[A:A+1]
  Caracteres.append(x)
  A=A+1
A=0
C=0
while A<10:
  while C<B:
    if vocales[A]==Caracteres[C]:
      Caracteres[C]=""
    C=C+1
  A=A+1
  C=0
A=0
textoF=""
while A<B:
  textoF=textoF+Caracteres[A]
  A=A+1
print(textoF)
