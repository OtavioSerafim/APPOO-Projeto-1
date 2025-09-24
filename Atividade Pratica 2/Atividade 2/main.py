from datetime import date
from cartaoCredito import CartaoCredito
from payPal import PayPal
from transferenciaBancaria import TransferenciaBancaria

def main():    
    cartao = CartaoCredito(150.50, date.today())
    paypal = PayPal(299.99, date.today())
    transferencia = TransferenciaBancaria(1500.00, date.today())
    
    # Processando os pagamentos
    print("\nProcessando pagamentos válidos:")
    cartao.processar_pagamento()
    paypal.processar_pagamento()
    transferencia.processar_pagamento()
    
    # Testando alguns casos de erro (que serão tratados pelas classes)
    print("\nTentando processar pagamentos inválidos:")
    cartao_invalido = CartaoCredito(-100, date.today())  # Valor negativo
    paypal_invalido = PayPal(0, date.today())  # Valor zero
    transferencia_invalida = TransferenciaBancaria("abc", date.today())  # Valor não numérico

    cartao_invalido.processar_pagamento()
    paypal_invalido.processar_pagamento()
    transferencia_invalida.processar_pagamento()

main()