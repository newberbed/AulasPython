class Animal:
    def __init__(self, numPatas, corPelo):
        self.numPatas = numPatas
        self.corPelo = corPelo

class Mamifero(Animal):
    def __init__(self, corPelo, **kw):
        self.corPelo = corPelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, corBico, corPelo, **kw):
        self.corBico = corBico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, corBico, corPelo,numPatas,):
        super().__init__(corPelo, corBico, numPatas)

gato = Gato(numPatas = 4, corPelo = "Preto")
print(gato)

ornitorrinco = Ornitorrinco(numPatas = 2, corPelo ="Cinza", corBico ="Laranja")
print(ornitorrinco)
