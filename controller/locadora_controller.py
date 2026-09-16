from model.veiculo import Veiculo
from view.menu_view import MenuView


class LocadoraController:
    def __init__(self):
        self.veiculos = []
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

        for veiculo in self.veiculos:
            if veiculo.placa.lower() == placa.lower():
                self.view.exibir_mensagem(
                    "Já existe um veículo cadastrado com essa placa."
                )
                return

        self.veiculos.append(Veiculo(modelo, placa, valor_diaria))
        self.view.exibir_mensagem("Veículo cadastrado com sucesso.")

    def _listar_veiculos(self):
        print("===== Veículos cadastrados: =====")
        self.view.exibir_veiculos(self.veiculos)

    def _alugar_veiculo(self):
        veiculo = self._encontrar_por_identificador()
        if veiculo is None:
            self.view.exibir_mensagem("Veículo não encontrado.")
        elif not veiculo.disponivel:
            self.view.exibir_mensagem("Esse veículo já está alugado.")
        else:
            veiculo.disponivel = False
            self.view.exibir_mensagem("Veículo alugado com sucesso.")

    def _devolver_veiculo(self):
        veiculo = self._encontrar_por_identificador()
        if veiculo is None:
            self.view.exibir_mensagem("Veículo não encontrado.")
        elif veiculo.disponivel:
            self.view.exibir_mensagem("Esse veículo não está alugado.")
        else:
            veiculo.disponivel = True
            self.view.exibir_mensagem("Veículo devolvido com sucesso.")

    def _encontrar_por_identificador(self):
        identificador = self.view.ler_identificador_veiculo().lower()
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == identificador:
                return veiculo
            if veiculo.placa.lower() == identificador:
                return veiculo

        return None
