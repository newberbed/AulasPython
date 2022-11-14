opcao = "nada"

while opcao != "Sair":
  opcao = input("esquerda,  direita, nenhuma, ambas /n")
    
  if opcao == "esquerda":
    print("ingles")
  elif opcao == "direita":
      print("frances")
  elif opcao == "nenhuma":
     print("portugues")
  elif opcao == "ambas":
     print("caiu")
     break
    

