from Hotel import Hotel
from Cliente import Cliente

def main():
    hotel = Hotel("Hotel Exemplo")
    cliente = Cliente("João", 5, 3)
    
    valorTotal = hotel.determineContaCliente(cliente, 200.0, 50.0)

    print(f"O cliente {cliente.nome} que ficou {cliente.dias_estadia} dias no hotel {hotel.nome_hotel} teve a conta de {valorTotal} reais, considerando {cliente.dias_estadia} dias de hospedagem e {cliente.consumo_restaurante} refeições.")

main()