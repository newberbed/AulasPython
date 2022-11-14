class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    #Metodo de classe
    @classmethod
    def calcula_idade(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    #Metodo estatico
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.calcula_idade(1987, 12, 19, "Newber")
print(p.nome, p.idade)
print(Pessoa.maior_idade(17))
print(Pessoa.maior_idade(p.idade))

