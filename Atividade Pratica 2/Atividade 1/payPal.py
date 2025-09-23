from metodoPagamento import MetodoPagamento

class PayPal(MetodoPagamento):
    def __init__(self, valor, data):
        super().__init__(valor, data)
        
    def processar_pagamento(self):
        print(f"O Pagamento foi processado com o Paypal no valor de {self.valor} na data {self.data}.")