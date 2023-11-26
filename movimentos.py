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

            self.attDadosTipoConta(self.codigo_agencia, self.tipo_operacao, self.valor_movimento)

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
            armazena_saldo = None

            for linha in linhas:
                if codigo_agencia in linha:
                    resultados.append(linha)

            if resultados:
                for resultado in resultados:
                    if resultado.strip().startswith(f"Código Agência: {codigo_agencia},"):
                        partes = resultado.split(", ")  # Alterado aqui para usar a variável resultado
                        for parte in partes:
                            if "Saldo" in parte:
                                print(f"Esse é o saldo atual: {parte.split('Saldo: ')[1].strip()}")
                                armazena_saldo = parte.split("Saldo: ")[1].strip()

        return armazena_saldo


    
    # alteração
    def attDadosTipoConta(self, codigo_agencia, tipo_operacao, novo_saldo):
        saldo_atual = self.getSaldoTipoConta(codigo_agencia)

        with open("tipo-de-conta.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("tipo-de-conta.txt", "w") as arquivo:
            encontrou_resultado = False
            for linha in linhas:
                if f"Código Agência: {codigo_agencia}," in linha:
                    if not encontrou_resultado:
                        encontrou_resultado = True
                        partes = linha.split(", ")

                        for j, parte in enumerate(partes):
                            if "Saldo" in parte:
                                saldo_anterior = float(saldo_atual)
                                novo_saldo = float(novo_saldo)

                                if tipo_operacao == "depósito":
                                    novo_saldo = saldo_anterior + novo_saldo
                                elif tipo_operacao == "saque":
                                    novo_saldo = saldo_anterior - novo_saldo

                                partes[j] = f"Saldo: {novo_saldo:.2f}"

                        nova_linha = ", ".join(partes) + "\n"
                        arquivo.write(nova_linha)
                        print("Alteração feita para o tipo de conta: ", codigo_agencia)
                    else:
                        arquivo.write(linha)
                else:
                    arquivo.write(linha)

            if not encontrou_resultado:
                print("=======================================\n")
                print("Nenhum resultado encontrado para o tipo de conta: ", codigo_agencia)
                print("A alteração não foi feita!!! \n")
                print("=======================================\n")
