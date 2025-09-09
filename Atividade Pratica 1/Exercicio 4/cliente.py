from hamburgueria import Hamburgueria

class Cliente:
    def __init__(self, nome, pedido):
        self.nome = nome
        self.pedido = pedido

    def pedeHamburguer(self, loja: Hamburgueria):
        loja.recebePedido(self)