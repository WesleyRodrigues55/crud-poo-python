# from agencias import Agencias

class TipoDeContas():

    def __init__(self, codigo_agencia="", nome_cliente="", nome_agencia="", tipo_de_conta="", saldo=""):
        self.codigo_agencia = codigo_agencia
        self.nome_cliente = nome_cliente
        self.nome_agencia = nome_agencia
        self.tipo_de_conta = tipo_de_conta
        self.saldo = saldo
        self.tipo_de_contas = []

    # inserção - OK
    def setDados(self):
        # Verifica se o cliente já existe no arquivo da ClasseA
        if self.verificar_cliente_existente() == False:
            print("=======================================\n")
            print("Cliente não existe!!!")
            print("=======================================\n")
            return  

        # # Verifica se a agência já existe no arquivo da ClasseB
        if self.verificar_agencia_existente() == False:
            print("=======================================\n")
            print("Agência não existe!!!")
            print("=======================================\n")
            return

        else:
            # Se não existir, faz a inserção
            self.tipo_de_contas.append({
                "codigo_agencia": self.codigo_agencia, 
                "nome_cliente": self.nome_cliente, 
                "nome_agencia": self.nome_agencia, 
                "tipo_de_conta": self.tipo_de_conta, 
                "saldo": self.saldo, 
            })

            # FAZER INSERÇÃO NO BLOCO DE NOTAS
            arquivo = open("tipo-de-conta.txt", "a")
            arquivo.write(
                f"Código Agência: {self.codigo_agencia}, "+ 
                f"Nome Cliente: {self.nome_cliente}, "+ 
                f"Nome Agência: {self.nome_agencia}, "+ 
                f"Tipo de Conta: {self.tipo_de_conta}, "+ 
                f"Saldo: {self.saldo} "+ 
                "\n")
            arquivo.close()
            print("=======================================\n")
            print("Tipo de Conta cadastrado!!! \n")
            print("=======================================\n")

    def verificar_cliente_existente(self):
        # Verifica se o cliente já existe no arquivo de Clientes
        with open("clientes.txt", "r") as arquivo_clientes:
            clientes_existentes = [linha.strip() for linha in arquivo_clientes]

        return any(self.nome_cliente in cliente for cliente in clientes_existentes)

    def verificar_agencia_existente(self):
        # Verifica se a agência já existe no arquivo de Agências
        with open("agencias.txt", "r") as arquivo_agencias:
            agencias_existentes = [linha.strip() for linha in arquivo_agencias]

        return any(self.nome_agencia in agencia for agencia in agencias_existentes)

             
    # alteração - OK
    def attDados(self, codigo_agencia, novo_tipo_de_conta, novo_saldo):
        with open("tipo-de-conta.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("tipo-de-conta.txt", "w") as arquivo:
            encontrou_resultado = False

            for linha in linhas:
                if f"Código Agência: {codigo_agencia}" in linha:
                    if not encontrou_resultado:
                        encontrou_resultado = True
                        # Divide a linha em partes com base nas vírgulas
                        partes = linha.split(", ")

                        # Itera sobre as partes para encontrar e substituir as informações
                        for j, parte in enumerate(partes):
                            if "Tipo de Conta" in parte:
                                partes[j] = f"Tipo de Conta: {novo_tipo_de_conta}"
                            elif "Saldo" in parte:
                                partes[j] = f"Saldo: {novo_saldo}"

                        # Junta as partes modificadas de volta em uma linha
                        nova_linha = ", ".join(partes) + "\n"
                        arquivo.write(nova_linha)
                        print("Alteração feita para o tipo de conta: ", codigo_agencia)
                    else:
                        # Se já encontrou uma correspondência, apenas escreva a linha original
                        arquivo.write(linha)
                else:
                    # Se a linha não contiver a correspondência, apenas escreva a linha original
                    arquivo.write(linha)

            if not encontrou_resultado:
                print("=======================================\n")
                print("Nenhum resultado encontrado para o tipo de conta: ", codigo_agencia)
                print("A alteração não foi feita!!! \n")
                print("=======================================\n")


    # consulta - OK
    def getDados(self, codigo_agencia):
        with open("tipo-de-conta.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            resultados = []
            for linha in linhas:
                if codigo_agencia in linha:
                    resultados.append(linha)

        if resultados:
            print("Resultados encontrados para a Código da Agência: ", codigo_agencia)
            for resultado in resultados:
                if resultado.strip().startswith(f"Código Agência: {codigo_agencia},"):
                    print(resultado)
        else:
            print("=======================================\n")
            print("Nenhum resultado encontrado para o Código da Agência: ", codigo_agencia)
            print("=======================================\n")


    # remoção
    def removeDados(self, codigo_agencia):
        with open("tipo-de-conta.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        agencia_encontrado = False
        linhas_restantes = []

        for linha in linhas:
            if linha.strip().startswith(f"Código Agência: {codigo_agencia},"):
                agencia_encontrado = True
            else:
                linhas_restantes.append(linha)

        if agencia_encontrado:
            with open("tipo-de-conta.txt", "w") as arquivo:
                arquivo.writelines(linhas_restantes)
            print("=======================================\n")
            print(f"Código da Agência: {codigo_agencia} removido com sucesso.")
            print("=======================================\n")
        else:
            print("=======================================\n")
            print(f"Código da Agência: {codigo_agencia} não encontrado.")
            print("=======================================\n")