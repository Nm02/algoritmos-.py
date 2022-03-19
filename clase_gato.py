class Gato():
  energia=0
  hambre=0
  def __init__(self,energia,hambre):
    self.energia=energia
    self.hambre=hambre
    print("se creo un gato")
  def tomar_leche(self,leche_en_litros):
    self.hambre+=leche_en_litros
    print("El gato toma su leche")
  def acariciar(self):
    print("prrrr")
  def jugar(self):
    if self.energia<=0 or self.hambre<=1:
      print("El gano no quere jugar.")
    else:
      self.energia-=1
      self.hambre-=2
      print("Al gato le encanta jugar.")
  def dormir(self,horas):
    self.energia+=horas
    print("el gato tomo una siesta")
  def _str_(self):
    return("El gato tiene "+str(self.energia)+" de energia y "+str(self.hambre)+" de hambre.")

g=Gato(5,5)
g.tomar_leche(5)
g.acariciar()
g.jugar()
g.dormir(5)
g.jugar()
print(g._str_())