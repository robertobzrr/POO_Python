class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def alugar(self):
        if not self.disponivel:
            return False
        self.disponivel = False
        return True

    def devolver(self):
        if self.disponivel:
            return False
        self.disponivel = True
        return True

    def exibir_informacoes(self):
        return (
            f"Modelo: {self.modelo} | Placa: {self.placa} | "
            f"Diária: R$ {self.valor_diaria:.2f}"
        )
