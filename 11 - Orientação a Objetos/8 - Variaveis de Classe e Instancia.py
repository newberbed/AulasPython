class Estudante:
    #Variavel de classe
    escola = "DIO"

    def __init__(self, nome, numero):
        #Variavel de instancia
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"

def mostrar_infos(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Guilherme", 54321)
aluno2 = Estudante("Giovana", 12345)
mostrar_infos(aluno1, aluno2)

aluno1.numero = 56789
mostrar_infos(aluno1, aluno2)

Estudante.escola = "Python"
mostrar_infos(aluno1, aluno2)
