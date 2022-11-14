#Criação de classes
class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
       super().voar()

class Avestruz(Passaro):
    def voar(serlf):
        print("Avestruz nao voa!")

class Aviao(Passaro):
    def voar(self):
        print("Voa, mas não é passaro!")

#Criação de metodos
def plano_de_voo(obj):
    obj.voar()

#Instanciando objetos
p1 = Pardal()
p2 = Avestruz()
a1 = Aviao()

#Chamando metodos dos objetos
plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(a1)