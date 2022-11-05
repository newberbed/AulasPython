#Função Parte 1
def exibir_mensagem():
    print("Ola Povo!")

def exibir_mensagem2(nome): 
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"): 
    print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem2(nome = "Newber")
# exibir_mensagem3()
# exibir_mensagem3(nome="De novo")


def calcular_valor(numeros):
    antecessor = numeros -1
    sucessor = numeros +1
    return antecessor, sucessor

print(calcular_valor(19))


#args(Lista) e Kwargs(Dicionario)

#Parametros Especiais 
#até / passa valores somente por posição
#até * passar valores nomeados ou não
#depos de * somente valores nomeados
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, 'ABC-1234', marca="Fiat", motor ="1.0", combustivel="gasolina")


#Objetos de primeira classe - Posso passar funções para funções
def somar(a,b):
    return a + b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a}+{b} é {resultado}.")

exibir_resultado(10, 11, somar)