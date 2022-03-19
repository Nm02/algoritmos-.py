'''Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para
un rango de números indicado por un usuario.'''

'''lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista)
lista=[]'''

'''lista=[]

primer= int(input("ingrese desde que numero quiere contar "))
segundo=int(input("ingrese hasta que numero quiere contar"))
x=-1
primer-=1
while x<primer:
    primer+=1
    lista.append(primer)
  
    if primer==segundo:
        print(lista)
        '''
'''2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si
pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50'''

'''i=int(input("ingrese un numero"))
lista=[1*i,2*i,3*i,4*i,5*i,6*i,7*i,8*i,9*i,10*i]
print(lista)'''

'''3)Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
caracteres.'''

'''escrito=input("escribe algo ")
cadena=[]
for i in escrito:
    if(i not in cadena):
        cadena.append(i)
print(cadena)'''

'''4)Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.'''

'''escrito=input("Escribe algo: ")
def letras(cadena):
    lista=[]
   
    for i in cadena:
        lista+=[i]
    for j in lista:
            if j ==" ":
                lista.remove(j)
    return lista

print(letras(escrito))'''

'''5)Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
repite'''

'''t=(1,2,3,3,4,2,5,2,2,7,6,7,9,8,1,9,9,9,9,8,8,8,4,7,7,7)
print("Ingrese numeros de 1 al 9")
x=int(input("Ingresa un numero: "))
if x in t:
    b=t.count(x)
    print(t)
    print("En la tupla se repite",b,"veces el numero",x,",que ingresaste")'''

'''6)Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre
1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra
un mensaje de error. El programa termina cuando el usuario introduce un cero'''
'''
mss=("nomes","Enero","Febrero","Marzo","Abril ","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
x=int(input("Ingrese un numero: "))

if x != 0 and x<=12:
    b=mss[x]
    print("El numero que ingresaste corresponde al mes de",b)
else:
    print("El numero que ingresaste no corresponde a ningun mes,vuelve a ejecutar el programa")'''

'''7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.'''
'''n=(54,67,12,3,79,57,85,38,37,89)
maxn=max(n)
minn=min(n)
print("El valor maximo maximo de la tupla es: ",maxn," el valor minimo de la tupla es: ",minn,)'''

'''8)Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace
hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
'''
diccionario = {}
frase = input("Frase:")
lista_palabras=frase.split(" ")
for palabra in lista_palabras:
	if palabra in diccionario:
		diccionario[palabra]+=1
	else:
		diccionario[palabra]=1	

for campo,valor in diccionario.items():
	print (campo,":",valor,",",end=" ",)

'''9) Escribir un programa que vaya solicitando al usuario que ingrese nombres.
- Si el nombre se encuentra en la agenda (implementada con un diccionario), debe
mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
- Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El
usuario puede utilizar la cadena "*", para salir del programa'''
"""
d={"Mateo":367612146,"Santiago":387123456,"Samira":112987654,"Milagros":132567234,"Sofia":246810212}

while True:
    print("\n")
    print("Puedes presionar 2 para ejecutar el programa")

    
    opcion = int(input("Dime opción:"))
    if opcion == 2:
        nombre = input("Nombre del contacto:")    
        if nombre in d:
            print(nombre,"ya existe su número de teléfono es",d[nombre])
            print("¿Quieres modificar el numero de",nombre,"?")
            opcion = input("Apreta 's' si queres cambiarlo. Y si no presiona 'n'")
            if opcion == "s":
                numero = input("Dame el nuevo número de teléfono:")
                d[nombre]=numero
                break
                if opcion=="n":
                    numero = input("Dame el número de teléfono:")
                    d[nombre]=numero
                    break
        if nombre not in d:
            numero=input("No se encontro en los contactos. Agrega el numero telefonico: ")
            d[nombre]=numero
            print(d)
            break"""

