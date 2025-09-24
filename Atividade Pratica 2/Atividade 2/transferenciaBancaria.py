from metodoPagamento import MetodoPagamento
from datetime import date

class TransferenciaBancaria(MetodoPagamento):
    def __init__(self, valor, data=...):
        super().__init__(valor, data)

    def salvar_pagamento(self, valor):
        with open("pagamentos.txt", "a") as f:
            f.write(f"{self.data} - Pagamento de valor {valor:.2f} processado com transferência bancária\n")
        
    def processar_pagamento(self):
        self.salvar_pagamento(self.valor)
        print(f"O Pagamento foi processado com transferência bancaria no valor de {self.valor} na data {self.data}.")