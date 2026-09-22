class MenuView:
    def exibir_menu(self):
        print("\n===== LOCADORA DE VEÍCULOS =====")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alugar veículo")
        print("4 - Devolver veículo")
        print("0 - Sair")

    def ler_opcao(self):
        return input("Digite sua opção: ")

    def ler_dados_veiculo(self):
        modelo = input("Digite o modelo do veículo: ")
        placa = input("Digite a placa do veículo: ")
        valor_diaria = float(input("Digite o valor da diária: "))
        return modelo, placa, valor_diaria

    def ler_identificador_veiculo(self):
        return input("Digite a placa do veículo: ")

    def exibir_veiculos(self, veiculos):
        if not veiculos:
            print("Nenhum veículo encontrado.")
            return

        for veiculo in veiculos:
            if veiculo.disponivel:
                situacao = "disponível"
            else:
                situacao = "alugado"
            print(
                f"Modelo: {veiculo.modelo} | Placa: {veiculo.placa} | "
                f"Diária: R$ {veiculo.valor_diaria:.2f} | Situação: {situacao}"
            )

    def exibir_mensagem(self, mensagem):
        print(mensagem)
