class Agencias:

    def __init__(self, nome=""):
        self.nome = nome
        self.agencias = []

    # inserção - OK
    def setDados(self):
        self.agencias.append({
            "nome": self.nome, 
        })

        # FAZER INSERÇÃO NO BLOCO DE NOTAS
        arquivo = open("agencias.txt", "a")
        arquivo.write(f"Nome Agência: {self.nome},\n")
        arquivo.close()
        print("=======================================\n")
        print("Agência cadastrado!!! \n")
        print("=======================================\n")
        
               
    # alteração - OK
    def attDados(self, nome, novo_nome):
        with open("agencias.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("agencias.txt", "w") as arquivo:
            resultados = []
            for linha in linhas:
                if nome in linha:
                    # Atualize a linha com as novas informações
                    nova_linha = f"Nome Agência: {novo_nome},\n"
                    arquivo.write(nova_linha)
                    resultados.append(linha)
                else:
                    arquivo.write(linha)

            if resultados:
                print("Resultados encontrados para a agência: ", nome)
                for resultado in resultados:
                    print(resultado)
                    print("Alteração feita!!! \n")
            else:
                print("=======================================\n")
                print("Nenhum resultado encontrado para a agência: ", nome)
                print("A alteração não foi feita!!! \n")
                print("=======================================\n")

    # consulta - OK
    def getDados(self, nome):
        with open("agencias.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            resultados = []
            for linha in linhas:
                if nome in linha:
                    resultados.append(linha)

        if resultados:
            print("Resultados encontrados para a Agência", nome)
            for resultado in resultados:
                print(resultado)
        else:
            print("=======================================\n")
            print("Nenhum resultado encontrado para o Agência", nome)
            print("=======================================\n")


    # remoção
    def removeDados(self, nome):
        with open("agencias.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        agencia_encontrado = False
        linhas_restantes = []

        for linha in linhas:
            if linha.strip().startswith(f"Nome Agência: {nome},"):
                agencia_encontrado = True
            else:
                linhas_restantes.append(linha)

        if agencia_encontrado:
            with open("agencias.txt", "w") as arquivo:
                arquivo.writelines(linhas_restantes)
            print("=======================================\n")
            print(f"Agência: {nome} removido com sucesso.")
            print("=======================================\n")
        else:
            print("=======================================\n")
            print(f"Agência: {nome} não encontrado.")
            print("=======================================\n")
