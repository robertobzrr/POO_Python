from model.veiculo import Veiculo
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
        try:
            modelo, placa, valor_diaria = self.view.ler_dados_veiculo()
        except ValueError:
            self.view.exibir_mensagem("Valor da diária inválido.")
            return

        veiculo = Veiculo(modelo, placa, valor_diaria)
        if self.locadora.cadastrar_veiculo(veiculo):
            self.view.exibir_mensagem("Veículo cadastrado com sucesso.")
        else:
            self.view.exibir_mensagem(
                "Já existe um veículo cadastrado com essa placa."
            )

    def _listar_veiculos(self):
        print("===== Veículos cadastrados: =====")
        self.view.exibir_veiculos(self.locadora.listar_veiculos())

    def _alugar_veiculo(self):
        placa = self.view.ler_identificador_veiculo()
        veiculo = self.locadora.buscar_por_placa(placa)
        if veiculo is None:
            self.view.exibir_mensagem("Veículo não encontrado.")
        elif not veiculo.disponivel:
            self.view.exibir_mensagem("Esse veículo já está alugado.")
        elif self.locadora.alugar_veiculo(placa):
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
