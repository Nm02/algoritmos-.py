class pou():
    energia=5
    hambre=5
    sed=5
    diversion=5
    def __init__(self,energia,hambre,sed,diversion):
        self.energia=energia
        self.hambre=hambre
        self.sed=sed
        self.diversion=diversion
        print("pou creado")
    def dormir(self):
        horas=int(input("¿cuantas horas durme?:"))
        self.energia+=horas
    def comer(self):
        comida=int(input("ingrese cantidad de comida:"))
        self.hambre+=comida
    def beber(self):
        bebida=int(input("ingrese cantidad de vasos de agua que va a beber:"))
        self.sed+=bebida
    def jugar(self):
        if self.energia>0 and self.hambre>0 and self.sed>0:
            self.energia-=1
            self.hambre-=1
            self.sed-=1
            self.diversion+=1
            print("el pou se divierte jugando")
        else:
            print("el pou no quiere jugar")
    def __str__(self) -> str:
        pass
    
arturo=pou(5,5,5,0)
arturo.jugar()
arturo.comer()
arturo.dormir()
arturo.beber()
arturo.__str__()