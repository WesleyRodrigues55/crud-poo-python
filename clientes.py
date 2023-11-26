class Clientes:

    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.clientes = []
    
    # inserção - OK
    def setDados(self):
        self.clientes.append({
            "nome": self.nome, 
            "email": self.email, 
            "telefone": self.telefone
        })

        # FAZER INSERÇÃO NO BLOCO DE NOTAS
        arquivo = open("clientes.txt", "a")
        arquivo.write(f"Nome cliente: {self.nome}, Email cliente: {self.email} e Telefone cliente: {self.telefone}\n")
        arquivo.close()
        print("=======================================\n")
        print("Cliente cadastrado!!! \n")
        print("=======================================\n")
        
               
    # alteração - OK
    def attDados(self, nome, novo_email, novo_telefone):
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("clientes.txt", "w") as arquivo:
            resultados = []
            for linha in linhas:
                if nome in linha:
                    # Atualize a linha com as novas informações
                    nova_linha = f"Nome cliente: {nome}, Email cliente: {novo_email} e Telefone cliente: {novo_telefone}\n"
                    arquivo.write(nova_linha)
                    resultados.append(linha)
                else:
                    arquivo.write(linha)

            if resultados:
                print("Resultados encontrados para o cliente: ", nome)
                for resultado in resultados:
                    print(resultado)
                    print("Alteração feita!!! \n")
            else:
                print("=======================================\n")
                print("Nenhum resultado encontrado para o cliente: ", nome)
                print("A alteração não foi feita!!! \n")
                print("=======================================\n")

    # consulta - OK
    def getDados(self, nome):
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            resultados = []
            for linha in linhas:
                if nome in linha:
                    resultados.append(linha)

        if resultados:
            print("Resultados encontrados para o cliente", nome)
            for resultado in resultados:
                print(resultado)
        else:
            print("=======================================\n")
            print("Nenhum resultado encontrado para o cliente", nome)
            print("=======================================\n")


    # remoção
    def removeDados(self, nome):
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        cliente_encontrado = False
        linhas_restantes = []

        for linha in linhas:
            if linha.strip().startswith(f"Nome cliente: {nome},"):
                cliente_encontrado = True
            else:
                linhas_restantes.append(linha)

        if cliente_encontrado:
            with open("clientes.txt", "w") as arquivo:
                arquivo.writelines(linhas_restantes)
            print("=======================================\n")
            print(f"Cliente {nome} removido com sucesso.")
            print("=======================================\n")
        else:
            print("=======================================\n")
            print(f"Cliente {nome} não encontrado.")
            print("=======================================\n")






