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

    def ler_tipo_veiculo(self):
        print("\nEscolha o tipo de veículo:")
        print("1 - Carro")
        print("2 - Moto")
        return input("Digite sua opção: ")

    def ler_dados_basicos(self):
        modelo = input("Digite o modelo do veículo: ")
        placa = input("Digite a placa do veículo: ")
        valor_diaria = float(input("Digite o valor da diária: "))
        return modelo, placa, valor_diaria

    def ler_quantidade_portas(self):
        return int(input("Digite a quantidade de portas: "))

    def ler_cilindradas(self):
        return int(input("Digite a cilindrada da moto: "))

    def ler_identificador_veiculo(self):
        return input("Digite a placa do veículo: ")

    def ler_dias(self):
        return int(input("Digite a quantidade de dias de aluguel: "))

    def exibir_veiculos(self, veiculos):
        if not veiculos: 
            print("Nenhum veículo encontrado.")
            return
        
        for veiculo in veiculos:
            print(veiculo.exibir_informacoes())
            print()

    def exibir_valor_aluguel(self, valor):
        print(f"Valor do aluguel: R$ {valor:.2f}")

    def exibir_mensagem(self, mensagem):
        print(mensagem)
        
