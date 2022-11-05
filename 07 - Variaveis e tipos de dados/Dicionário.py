#Dicionários
pessoa = {"nome":"Newber", "idade":"34"}
#Forma alternativa: 
# pessoa = dict(nome="Newber", idade="34")
print(pessoa)

#Aicionando chave:
pessoa["Telefone"] = "3333-3333"
print(pessoa)

#Imprimindo uma chave
print(pessoa["nome"])

#Alterando um valor
pessoa["idade"] = "35"
print(pessoa["idade"])

#Dicionario aninhado 
contatos = {
    "newber@gmail.com":{"nome": "Newber", "telefone":"1111-1111"},
    "gato@gmail.com":{"nome": "Gato", "telefone":"2222-2222"},
    "cachorro@gmail.com":{"nome": "Cachorro", "telefone":"3333-3333"}
}

print(contatos)
print(contatos["gato@gmail.com"]["telefone"])

#Copy - Copia de dicionario
copia = contatos.copy()
copia["newber@gmail.com"] = {"nome" : "New"}

print(contatos)
print(copia)

#Get - VErifica se existe uma chave no dicionário, se não existir traz valor informado
print(contatos.get("dataNascimento", {}))

#Keys - Retorna as chaves do dicionario
print(contatos.keys())

#Pop - Remove uma chave do dicionario
contatos.pop("idade")
print(contatos.keys())

#SetDefault - Se a chave não existir no dicionario ele insere com o valor passado, se existir não altera nada
print("Teste aqui")
contatos.setdefault("dataNascimento", "19/12/1987")
print(contatos["newber@gmail.com"])

#del - Rove uma chave ou um dado da chave do dicionario
contatos = {
    "newber@gmail.com":{"nome": "Newber", "telefone":"1111-1111"},
    "gato@gmail.com":{"nome": "Gato", "telefone":"2222-2222"},
    "cachorro@gmail.com":{"nome": "Cachorro", "telefone":"3333-3333"}
}
#Remove o registro
del contatos["gato@gmail.com"]
#Remove uma informação do registro
del contatos["cachorro@gmail.com"]["telefone"]