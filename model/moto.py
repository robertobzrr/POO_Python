from model.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        valor_total = self.valor_diaria * dias
        return valor_total * 0.9

    def exibir_informacoes(self):
        if self.disponivel:
            situacao = "Sim"
        else:
            situacao = "Não"
        return (
            f"Moto - {self.modelo}\n"
            f"Placa: {self.placa}\n"
            f"Diária: R$ {self.valor_diaria:.2f}\n"
            f"Cilindradas: {self.cilindradas}\n"
            f"Disponível: {situacao}"
        )
