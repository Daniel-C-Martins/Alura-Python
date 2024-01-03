import os

def exibir_nome_do_programa():
  print(""""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
  print("1. Cadastrar restaurantes")
  print("2. Listar restaurantes")
  print("3. Ativar restaurante")
  print("4. Sair \n") 

def finalizar_app(): #Funcao
  os.system("cls") #Limpa o terminal
  print("Encerrando App \n")

def escolher_opcao():
  opcao_escolhida = int(input("Escolha uma opção: "))
  # print(type(opcao_escolhida))

  #match poderia ser usado, match é o switch sem break
  if opcao_escolhida == 1:
      print("Cadastrar restaurantes")
  elif opcao_escolhida == 2:
    print("Listar restaurantes")
  elif opcao_escolhida == 3:
    print("Ativar restaurantes")
  else: 
    finalizar_app()

def main():
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

if __name__ == "__main__":
  main()
