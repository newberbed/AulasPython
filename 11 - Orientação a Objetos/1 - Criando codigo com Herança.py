class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregando")


moto = Motocicleta("Vermelha", "MBC-1234", 2)
carro = Carro("Branco", "CBC-4567", 4)
caminhao = Caminhao("Roxo", "CCD-4566", 6, False)

print(moto)
print(carro)
print(caminhao)


