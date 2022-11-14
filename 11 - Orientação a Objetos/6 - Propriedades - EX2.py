class Pessoa:
    def __init__(self, nome, anoNascim):
        self._nome = nome
        self._anoNascim = anoNascim

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        anoAtual = 2022
        return anoAtual - self._anoNascim

pessoa = Pessoa("Newber", 1987)
print(f"O {pessoa.nome} posui {pessoa.idade} anos")