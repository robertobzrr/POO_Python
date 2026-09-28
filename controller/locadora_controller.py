from model.carro import Carro
from model.moto import Moto
from model.locadora import Locadora
from view.menu_view import MenuView

class LocadoraController:
    def __init__(self):
        self.locadora = Locadora()
        self.view = MenuView()

    def executar(self):
        opcao = ""
        while opcao != "0":
            self.view.exibir_menu()
            opcao = self.view.ler_opcao()
            self._processar_opcao(opcao)

    def _processar_opcao(self, opcao):
        if opcao == "1":
            self._cadastrar_veiculo()
        elif opcao == "2":
            self._listar_veiculos()
        elif opcao == "3":
            self._alugar_veiculo()
        elif opcao == "4":
            self._devolver_veiculo()
        elif opcao == "0":
            self.view.exibir_mensagem("Saindo do sistema...")
        else:
            self.view.exibir_mensagem("Opção inválida. Tente novamente.")

    def _cadastrar_veiculo(self):
        tipo = self.view.ler_tipo_veiculo()

        try:
            modelo, placa, valor_diaria = self.view.ler_dados_basicos()
        except ValueError:
            self.view.exibir_mensagem("Valor da diária inválido.")
            return

        if tipo == "1":
            quantidade_portas = self.view.ler_quantidade_portas()
            veiculo = Carro(modelo, placa, valor_diaria, quantidade_portas)
        elif tipo == "2":
            cilindradas = self.view.ler_cilindradas()
            veiculo = Moto(modelo, placa, valor_diaria, cilindradas)
        else:
            self.view.exibir_mensagem("Tipo de veículo inválido.")
            return

        if self.locadora.cadastrar_veiculo(veiculo):
            self.view.exibir_mensagem("Veículo cadastrado com sucesso.")
        else:
            self.view.exibir_mensagem("Já existe um veículo com essa placa. Cadastro não realizado.")


    def _listar_veiculos(self):
        print("===== Veículos cadastrados: =====")
        self.view.exibir_veiculos(self.locadora.listar_veiculos())

    def _alugar_veiculo(self):
        placa = self.view.ler_identificador_veiculo()
        veiculo = self.locadora.buscar_por_placa(placa)

        if veiculo is None:
            self.view.exibir_mensagem("Veículo não encontrado.")
            return

        if not veiculo.disponivel:
            self.view.exibir_mensagem("Esse veículo já está alugado.")
            return

        dias = self.view.ler_dias()
        valor = veiculo.calcular_aluguel(dias)
        self.view.exibir_valor_aluguel(valor)

        if self.locadora.alugar_veiculo(placa):
            self.view.exibir_mensagem("Veículo alugado com sucesso.")

    def _devolver_veiculo(self):
        placa = self.view.ler_identificador_veiculo()
        veiculo = self.locadora.buscar_por_placa(placa)
        
        if veiculo is None:
            self.view.exibir_mensagem("Veículo não encontrado.")
        elif veiculo.disponivel:
            self.view.exibir_mensagem("Esse veículo não está alugado.")
        elif self.locadora.devolver_veiculo(placa):
            self.view.exibir_mensagem("Veículo devolvido com sucesso.")
