class Hamburgueria:
    def __init__(self, nome: str, tempo: int):
        self.nome = nome
        self.tempoMedio = tempo

    def recebePedido(self, cliente):
        print(f"O pedido {cliente.pedido} de {cliente.nome} será entregue em mais ou menos {self.tempoMedio} minutos")