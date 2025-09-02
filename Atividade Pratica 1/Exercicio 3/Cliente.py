class Cliente:
    def __init__(self, nome: str, dias_estadia: int, consumo_restaurante: float):
        self.nome = nome
        self.dias_estadia = dias_estadia
        self.consumo_restaurante = consumo_restaurante

    def fornecaValorConta(self, valor_diaria: float, valor_refeicao: float):
        valor_total = (self.dias_estadia * valor_diaria) + (self.consumo_restaurante * valor_refeicao)
        return valor_total
