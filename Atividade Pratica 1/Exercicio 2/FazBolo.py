class FazBolo:
    def __init__(self, massa: str, recheio: str, cobertura: str ):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura
    
    def assar(self, temperatura: str, tempo: int):
        temperaturas_validas = {"alto", "médio", "baixo"}
        if temperatura not in temperaturas_validas:
            print("Temperatura inválida")
            return
        if tempo <= 0:
            print("Tempo inválido")
            return
        if tempo >= 60:
            print("Tá fazendo carvão? Muito tempo cozinhando")
            return
        print(
            f"""Você está querendo assar o bolo de massa {self.massa} com recheio de {self.recheio} 
e cobertura de {self.cobertura} no fogo {temperatura} por {tempo} minutos""")
        pontos_perfeitos = {"alto": 10, "médio": 30, "baixo": 45}
        tempo_perfeito = pontos_perfeitos[temperatura]
        if tempo < tempo_perfeito:
            print("O bolo ficará cru")
        elif tempo == tempo_perfeito:
            print("O bolo ficará perfeito")
        else:
            print("O bolo irá queimar")