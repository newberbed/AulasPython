#Criando e imprimindo Listas
frutas = ["banana", "maca", "uva"]
print (frutas[0])


#Criando e imprimindo Matriz
matriz = [
    [1,"a",2],
    [3,"b",5]
    ]
print (matriz[1][1])

#imprimindo valores da lista
carros = ["gol", "palio", "celta"]
for indice, carro in enumerate(carros):
    print(f"{indice}:{carros}")


#Adicionando itens na lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

#Limpar lista
#lista.clear()
print(lista)


#Copiando Lista
ls = lista.copy()
print(lista)

#Contar quantidade de vezes um ojeto na lista
print(carros.count("gol"))

#Incluir uma lista na lista
linguagens = ["Python","Java", "C"]
print(linguagens)

linguagens.extend("js", "CSharp")
print(linguagens)