from model.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, quantidade_portas):
        super().__init__(modelo, placa, valor_diaria)
        self.quantidade_portas = quantidade_portas

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def exibir_informacoes(self):
        if self.disponivel:
            situacao = "Sim"
        else:
            situacao = "Não"
        return (
            f"Carro - {self.modelo}\n"
            f"Placa: {self.placa}\n"
            f"Diária: R$ {self.valor_diaria:.2f}\n"
            f"Portas: {self.quantidade_portas}\n"
            f"Disponível: {situacao}"
        )
