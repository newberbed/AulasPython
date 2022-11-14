#Criando uma classe cachorro
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AuAu")

    def dormir(self):
        self.acordado = False
        print("ZzZzzzz...")

#Criando Objeto

cao1 = Cachorro("Chappie","Amarelo", False)
cao2 = Cachorro("Aladim", "branco e preto")

cao1.latir()

print(cao2.acordado)
cao2.dormir()
print(cao2.acordado)
