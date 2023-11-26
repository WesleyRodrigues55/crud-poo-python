from clientes import Clientes
from agencias import Agencias
from tipo_de_contas import TipoDeContas
from movimentos import Movimentos


clientes = Clientes()
agencias = Agencias()
tipo_de_contas = TipoDeContas()
movimentos = Movimentos()

count = 1
while count > 0:
    print("\n===== Sistema de Cadastro de Clientes =====")
    print("1. Adicionar Cliente")
    print("2. Editar Cliente")
    print("3. Buscar Cliente")
    print("4. Remover Cliente")

    print("\n===== Sistema de Cadastro de Agências =====")
    print("5. Adicionar Agência")
    print("6. Editar Agência")
    print("7. Buscar Agência")
    print("8. Remover Agência")

    print("\n===== Sistema de Cadastro de Tipo de Conta =====")
    print("9. Adicionar Tipo de conta")
    print("10. Editar Tipo de conta")
    print("11. Buscar Tipo de conta")
    print("12. Remover Tipo de conta")

    print("13. Sair")
    escolha = input("Escolha uma opção: ")

    # CLASSE CLIENTE
    if escolha == "1":
        clientes.nome = input("Digite o nome do cliente a ser cadastrado: ")
        clientes.email = input("Digite o email do cliente a ser cadastrado: ")
        clientes.telefone = input("Digite o telefone do cliente a ser cadastrado: ")
        clientes.setDados()

    elif escolha == "2":
        clientes.nome = input("Digite o nome do cliente a ser Editado: ")
        novo_email = input("Digite o novo email do cliente a ser Editado: ")
        novo_telefone = input("Digite o novo telefone do cliente a ser Editado: ")
        clientes.attDados(clientes.nome, novo_email, novo_telefone)

    elif escolha == "3":
        clientes.nome = input("Digite o nome do cliente a a ser pesquisado: ")
        clientes.getDados(clientes.nome)

    elif escolha == "4":
        clientes.nome = input("Digite o nome do cliente a a ser removido: ")
        clientes.removeDados(clientes.nome)

    # CLASSE AGÊNCIA
    elif escolha == "5":
        agencias.nome = input("Digite o nome da Agência a ser cadastrado: ")
        agencias.setDados()

    elif escolha == "6":
        agencias.nome = input("Digite o nome da Agência a ser Editado: ")
        novo_nome = input("Digite o novo nome da Agência: ")
        agencias.attDados(agencias.nome, novo_nome)

    elif escolha == "7":
        agencias.nome = input("Digite o nome da Agência a ser pesquisado: ")
        agencias.getDados(agencias.nome)

    elif escolha == "8":
        agencias.nome = input("Digite o nome da Agência a ser removido: ")
        agencias.removeDados(agencias.nome)

    # CLASSE TIPO DE CONTA
    elif escolha == "9":
        tipo_de_contas.codigo_agencia = input("Digite o código do tipo de conta a ser cadastrado: ")
        tipo_de_contas.nome_cliente = input("Digite o nome do cliente a ser cadastrado: ")
        tipo_de_contas.nome_agencia = input("Digite o nome da Agência a ser cadastrado: ")
        tipo_de_contas.tipo_de_conta = input("Digite o tipo de conta a ser cadastrado: ")
        tipo_de_contas.saldo = input("Digite o saldo a ser cadastrado: ")
        tipo_de_contas.setDados()

    elif escolha == "10":
        tipo_de_contas.codigo_agencia = input("Digite o código do tipo de conta a ser Editado: ")
        tipo_de_contas.tipo_de_conta = input("Digite o tipo de conta a ser Editado: ")
        tipo_de_contas.saldo = input("Digite o saldo a ser Editado: ")
        tipo_de_contas.attDados(tipo_de_contas.codigo_agencia, tipo_de_contas.tipo_de_conta, tipo_de_contas.saldo)

    elif escolha == "11":
        tipo_de_contas.codigo_agencia = input("Digite o código do tipo de conta a ser pesquisado: ")
        tipo_de_contas.getDados(tipo_de_contas.codigo_agencia)

    elif escolha == "12":
        tipo_de_contas.codigo_agencia = input("Digite o código do tipo de conta a ser removido: ")
        tipo_de_contas.removeDados(tipo_de_contas.codigo_agencia)

    # CLASSE MOVIMENTO
    elif escolha == "13":
        movimentos.codigo_movimento = input("Digite o código do movimento a ser cadastrado: ")
        movimentos.codigo_agencia = input("Digite o código da agência: ")
        movimentos.tipo_operacao = input("Digite o tipo de operação [depósito] ou [saque]: ")
        movimentos.valor_movimento = input(f"Digite o valor do {movimentos.tipo_operacao} R$")
        movimentos.setDados()

    elif escolha == "14":
        print("Saindo do sistema. Obrigado!")
        count = 0