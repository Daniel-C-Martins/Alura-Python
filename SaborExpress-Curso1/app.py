import os

restaurantes = ["Lanchonete do Renan", "Pizaaria do Marcelo"] #ArrayList

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
  exibir_subtitulos("Encerrando App")

def voltar_ao_menu():
  input("\n Digite uma tecla para voltar ao inicio do programa: ")
  main()

def exibir_subtitulos(texto):
  os.system("cls")
  print(texto)
  print()

def opcao_invalida():
  print("Opcão inválida \n")
  voltar_ao_menu()

def cadastrar_novo_restaurante():
  exibir_subtitulos("Cadastro de novos restaurantes")
  nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
  restaurantes.append(nome_do_restaurante) #adiciona no arrayList
  print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
  voltar_ao_menu()

def listar_restaurantes():
  exibir_subtitulos("listando os restaurantes")

  for restaurante in restaurantes:
    print(f"-> {restaurante} \n")
  voltar_ao_menu()
  
def escolher_opcao():
  try:
    opcao_escolhida = int(input("Escolha uma opção:  "))
    # print(type(opcao_escolhida))

    #match poderia ser usado, match é o switch sem break
    if opcao_escolhida == 1:
      cadastrar_novo_restaurante() 
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      print("Ativar restaurantes")
    elif opcao_escolhida == 4:
      finalizar_app()
    else: 
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system("cls")
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == "__main__":
  main()
