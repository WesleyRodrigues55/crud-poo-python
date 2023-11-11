from cliente import Clientes
from agencia import Agencias
from movimento import Movimentos

count = 1
while count > 0:
    print("\n===== Sistema de Cadastro de Clientes =====")
    print("1. Adicionar Cliente")
    print("2. Editar Cliente")
    print("3. Buscar Cliente")
    print("4. Remover Cliente")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cliente.nome = input("Digite o nome do cliente a ser cadastrado: ")
        cliente.email = input("Digite o email do cliente a ser cadastrado: ")
        cliente.telefone = input("Digite o telefone do cliente a ser cadastrado: ")
        cliente.setDados()
    elif escolha == "2":
        cliente.nome = input("Digite o nome do cliente a ser Editado: ")
        novo_email = input("Digite o novo email do cliente a ser Editado: ")
        novo_telefone = input("Digite o novo telefone do cliente a ser Editado: ")
        cliente.attDados(cliente.nome, novo_email, novo_telefone)
    elif escolha == "3":
        cliente.nome = input("Digite o nome do cliente a a ser pesquisado: ")
        cliente.getDados(cliente.nome)
    elif escolha == "4":
        cliente.nome = input("Digite o nome do cliente a a ser removido: ")
        cliente.removeDados(cliente.nome)
    elif escolha == "5":
        print("Saindo do sistema. Obrigado!")
        count = 0