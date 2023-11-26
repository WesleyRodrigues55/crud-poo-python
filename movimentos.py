class Movimentos:

    def __init__(self, codigo_movimento = "", codigo_agencia = "", tipo_operacao = "", valor_movimento = ""):
        self.codigo_movimento = codigo_movimento
        self.codigo_agencia = codigo_agencia
        self.tipo_operacao = tipo_operacao
        self.valor_movimento = valor_movimento
        self.movimentos = []

    def setDados(self):
        if self.verificar_codigo_agencia_existente() == False:
            print("=======================================\n")
            print("Código da agência não existe!!!")
            print("=======================================\n")
            return  
        else:
            self.movimentos.append({
                "codigo_movimento": self.codigo_movimento,
                "codigo_agencia": self.codigo_agencia, 
                "tipo_operacao": self.tipo_operacao, 
                "valor_movimento": self.valor_movimento, 
            })

            # FAZER INSERÇÃO NO BLOCO DE NOTAS
            arquivo = open("movimentos.txt", "a")
            arquivo.write(
                f"Código do movimento: {self.codigo_movimento}, " +
                f"Código Agência: {self.codigo_agencia}, "+ 
                f"Tipo operação: {self.tipo_operacao}, "+ 
                f"Valor movimento: {self.valor_movimento} "+ 
            "\n")
            arquivo.close()

            

            if self.tipo_operacao == "depósito":
                #soma no tipo conta o saldo
                attDadosTipoConta(self.codigo_agencia, novo_saldo)
                return
            elif self.tipo_operacao == "saque":
                #subtrái no tipo de conta saldo
                return

            print("=======================================\n")
            print("Movimento cadastrado!!! \n")
            print("=======================================\n")

    def verificar_codigo_agencia_existente(self):
        # Verifica se o cliente já existe no arquivo de Clientes
        with open("tipo-de-conta.txt", "r") as arquivo_codigo_agencia:
            tipos_de_contas_existentes = [linha.strip() for linha in arquivo_codigo_agencia]

        return any(self.codigo_agencia in tipo_conta for tipo_conta in tipos_de_contas_existentes)

    def getSaldoTipoConta(self, codigo_agencia):
        with open("tipo-de-conta.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            resultados = []
            for linha in linhas:
                if codigo_agencia in linha:
                    resultados.append(linha)

        if resultados:
            # print("Resultados encontrados para a Código da Agência: ", codigo_agencia)
            armazena_saldo = ""
            for resultado in resultados:
                if resultado.strip().startswith(f"Código Agência: {codigo_agencia},"):
                    partes = linha.split(", ")
                    for j, parte in enumerate(partes):
                            if "Saldo" in parte:
                                print(parte)
                    
        else:
            print("=======================================\n")
            print("Nenhum resultado encontrado para o Código da Agência: ", codigo_agencia)
            print("=======================================\n")
    
    # alteração
    def attDadosTipoConta(self, codigo_agencia, novo_saldo):
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
                            if "Saldo" in parte:
                                partes[j] = f"Saldo: {novo_saldo}"

                        # Junta as partes modificadas de volta em uma linha
                        nova_linha = ", ".join(partes) + "\n"
                        arquivo.write(nova_linha)
                        # print("Alteração feita para o tipo de conta: ", codigo_agencia)
                    else:
                        # Se já encontrou uma correspondência, apenas escreva a linha original
                        arquivo.write(linha)
                else:
                    # Se a linha não contiver a correspondência, apenas escreva a linha original
                    arquivo.write(linha)

            # if not encontrou_resultado:
            #     print("=======================================\n")
            #     print("Nenhum resultado encontrado para o tipo de conta: ", codigo_agencia)
            #     print("A alteração não foi feita!!! \n")
            #     print("=======================================\n")