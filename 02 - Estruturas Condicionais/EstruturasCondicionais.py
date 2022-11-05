maior_idade = 18
idade_especial = 17
idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, já pode tirar a CNH.")
elif idade_especial == idade:
    print("Pode fazer fazer aulas teoricas, mas não praticas.")
else:
    print("Ainda não pode tirar a CNH.")

