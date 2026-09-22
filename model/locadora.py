class Locadora:
    def __init__(self):
        self.veiculos = []

    def buscar_por_placa(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa.lower() == placa.lower():
                return veiculo

        return None

    def cadastrar_veiculo(self, veiculo):
        if self.buscar_por_placa(veiculo.placa) is not None:
            return False

        self.veiculos.append(veiculo)
        return True

    def listar_veiculos(self):
        return self.veiculos

    def alugar_veiculo(self, placa):
        veiculo = self.buscar_por_placa(placa)

        if veiculo is None:
            return False

        return veiculo.alugar()

    def devolver_veiculo(self, placa):
        veiculo = self.buscar_por_placa(placa)

        if veiculo is None:
            return False

        return veiculo.devolver()