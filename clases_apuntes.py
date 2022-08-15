
"""class animal():
    def __init__(self,hambre,sed,sueño):
        self.hambre=hambre
        self.sed=sed
        self.sueño=sueño
    def jugar(self):
        print("El animal juega")


class gato(animal):

    def __init__(self,hambre,sed,sueño,ronroneo):
        self.ronroneo=ronroneo
        super().__init__(hambre,sed,sueño)

    def tomar(self,cantidad):
        self.sed=self.sed+cantidad
        print("El gato tomo agua.")
    
    def dormir(self):
        self.sueño=self.sueño+1
        print("El gato duerme.")
    
    def correr(self):
        self.sueño=self.sueño-1
        self.hambre=self.hambre-1
        self.sed=self.sed-1
        print("El gato corre.")
    

class perro(animal):
    def __init__(self,hambre,sed,sueño,ladrar):
        self.ladrar=ladrar
        super().__init__(hambre,sed,sueño)
    def tomar(self,cantidad):
        self.sed=self.sed+cantidad
        print("El perro toma agua.")

p=perro(1,1,1,False)
g=gato(1,1,1,True)
g.jugar()
p.jugar()
g.tomar(10)
p.tomar(5)




"""




"""class corcho():
    def __init__(self,bodega):
        self.bodega=bodega
    
class botella():
    def __init__(self,corcho=None):
        if corcho!=None:
            self.corcho=corcho.bodega
        else:
            self.corcho=corcho
        print(self.corcho)

c=corcho(111)
b=botella(c)"""






















