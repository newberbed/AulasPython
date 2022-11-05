#Criando lista com objeto repetido
frutas = {"maça", "banana", "pera", "maça", "uva"}
#print(frutas)

#1 - Metodos
#1.1 - Union (Todos de ambos)
carros = {"gol", "uno", "celta", "gol"}
print("União")
print(frutas.union(carros))

#1.2 - Interseção (Pretence a ambos ao mesmo tempo)
frutas2 = {"maça", "pera","pera","uva"}
print("Interseção")
print(frutas.intersection(frutas2))

#1.3 - Diferença (Que esta em um e não no outro)
print("Diferença")
print(frutas.difference(frutas2))

#1.4 - Diferença Simetrica 
print("Diferença Simetrica")
print(frutas.symmetric_difference(frutas2))

#1.5 - SubSet(um grupo pertence a de outro)
grupoa = {"1","2","3"}
grupob = {"4","1", "2","5","6","3"}
print("grupo a pertence a grupo b?")
print(grupoa.issubset(grupob))
print("grupo b pertence a grupo a?")
print(grupob.issubset(grupoa))

#1.6 - Issuperset(Todos os elementos de um grupo estão em outro?)
grupoa = {"1","2","3"}
grupob = {"4","1","2","5","6","3"}
print("Todo grupo a pertence a grupo b?")
print(grupoa.issubset(grupob))
print("Todo grupo b pertence a grupo a?")
print(grupob.issuperset(grupoa))

#1.7 - Add = Adicionando elementos caso não exista
sorteio = {"1","2","3"}
print(sorteio)
sorteio.add("25")
print(sorteio)
sorteio.add("42")
print(sorteio)
sorteio.add("25")
print(sorteio)

#1.8 - clear = Limpa a tupla
#sorteio.clear()
print(sorteio)

#1.9 - discard = Elimina um valor
numeros = {1,2,3,4,5,6,7,8,9,10}
print(numeros)
numeros.discard(6)
print(numeros)

#1.10 - pop = Elimina um valor na sequencia
numeros2 = {1,2,3,4,5,6,7,8,9,10}
print(numeros2)
numeros2.pop()
print(numeros2)
numeros2.pop()
print(numeros2)

#1.11 - remove = Elimina um valor, se der erro ele mostra
numeros3 = {1,2,3,4,5,6,7,8,9,10}
print(numeros3)
numeros3.discard(6)
print(numeros3)