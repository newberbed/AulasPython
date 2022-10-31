nome = "Newber"
idade = 34
profissao = "Analista de Sistemas"
linguagem = "Python"

#Old Style
print("Olá! Me chamo: %s, tenho %d anos de idade, trabalho como %s e faço curso de %s." % (nome, idade, profissao, linguagem))

#Metodo Format
print("Olá! Me chamo {}, tenho {} anos de idade, trabalho como {} e faço curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá! Me chamo {0}, tenho {1} anos de idade, trabalho como {2} e faço curso de {3}.".format(nome, idade, profissao, linguagem))
print("Olá! Me chamo {n}, tenho {i} anos de idade, trabalho como {p} e faço curso de {l}.".format(n=nome, i=idade, p=profissao, l=linguagem))

#Metodo F-string
print(f"Olá! Me chamo {nome}, tenho {idade} anos de idade, trabalho como {profissao} e faço curso de {linguagem}.")