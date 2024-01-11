import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, 
                {"nome":"Pizza Superma", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiano", "ativo":False}] #ArrayList

def exibir_nome_do_programa():
  """
  Essa função imprimi na tela o nome do programa
  """
  print(""""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
  """
  Essa função exibe na tela as opções do programa
  """
  print("1. Cadastrar restaurantes")
  print("2. Listar restaurantes")
  print("3. Alternar estado do restaurante")
  print("4. Sair \n") 

def finalizar_app(): 
  """
  Essa função encerra o programa
  """
  exibir_subtitulos("Encerrando App")

def voltar_ao_menu():
  """
  Essa função é usada para voltar ao menu do programa
  """
  input("\n Digite uma tecla para voltar ao inicio do programa: ")
  main()

def exibir_subtitulos(texto):
  """
  Essa função exibe os subtitulos de cada opção do programa
  """
  os.system("cls")
  linha = "*" * len(texto)
  print(linha)
  print(texto)
  print(linha)
  print()

def opcao_invalida():
  """
  Essa é uma opção usada para mostrar uma opção inválida
  """
  print("Opcão inválida \n")
  voltar_ao_menu()

def cadastrar_novo_restaurante():
  """
  Essa função é responsável por cadastrar um restaurante
  """
  exibir_subtitulos("Cadastro de novos restaurantes")
  nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
  categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:  ")
  dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
  restaurantes.append(dados_do_restaurante)
  print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
  voltar_ao_menu()

def listar_restaurantes():
  """
  Essa função lista todos os restaurantes criados
  """
  exibir_subtitulos("listando os restaurantes")
  print(f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status')
  for restaurante in restaurantes:
    nome_restaurante = restaurante["nome"]
    categoria = restaurante["categoria"]
    ativo = "Ativada" if restaurante["ativo"] else "Desativado"
    print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
  voltar_ao_menu()

def alternar_estado_restaurante():
  """
  Essa função alterna o estado de um restaurante
  """
  exibir_subtitulos("Alternando estado do restaurante ")
  nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o estado:  ")
  restaurante_encontrado = False
  for restaurante in restaurantes:
    if nome_do_restaurante == restaurante["nome"]:
      restaurante_encontrado = True
      restaurante["ativo"] = not restaurante["ativo"]
      mensagem = f"o restaurante {nome_do_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_do_restaurante} foi desativado com sucesseo"
      print(mensagem)
  if not restaurante_encontrado:
    print("O restaurante não foi encontrado")    
  voltar_ao_menu()

def escolher_opcao():
  """
  Essa função é responsável por receber a opção escolhida pelo usuário
  """
  try:
    opcao_escolhida = int(input("Escolha uma opção:  "))
    # print(type(opcao_escolhida))

    #match poderia ser usado, match é o switch sem break
    if opcao_escolhida == 1:
      cadastrar_novo_restaurante() 
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_estado_restaurante()
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
