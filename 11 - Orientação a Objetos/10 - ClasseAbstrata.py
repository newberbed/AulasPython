from abc import ABC, abstractmethod
#Todos os metodos abstratos devem ser criados também nas classes


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

    def marca(self):
        return "LG"

class controlearcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado.")

    def desligar(self):
        print("Desligando ar condicionado.")

    def marca(self):
        return "Split"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle2 = controlearcondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)