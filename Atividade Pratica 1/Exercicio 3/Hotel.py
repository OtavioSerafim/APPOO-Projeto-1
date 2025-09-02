from Cliente import Cliente
class Hotel:
    def __init__(self, nome_hotel: str):
        self.nome_hotel = nome_hotel

    def determineContaCliente(self, cliente: Cliente, valor_diaria: float, valor_refeicao: float):
        return cliente.fornecaValorConta(valor_diaria, valor_refeicao)