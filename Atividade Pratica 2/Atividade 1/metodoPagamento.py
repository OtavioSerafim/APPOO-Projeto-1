from abc import ABC, abstractmethod
from datetime import date
class MetodoPagamento(ABC):
    def __init__(self, valor, data=date.today()):
        try:
            if not type(valor) in (float, int) or isinstance(valor, bool):
                raise ValueError("Valor deve ser um número (int ou float)")
            if valor <= 0:
                raise ValueError("Valor deve ser positivo")
            if not isinstance(data, date):
                raise ValueError("Data inválida")
            self.valor = valor
            self.data = data
        except ValueError as e:
            print(f"Erro ao criar método de pagamento: {e}")
        except:
            print("Erro não esperado na criação da instância!")
            

    @abstractmethod
    def processar_pagamento(self):
        pass