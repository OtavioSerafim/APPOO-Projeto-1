from FormaGeometrica import FormaGeometrica

class Quadrado(FormaGeometrica):
    def __init__(self):
        print("Você está instânciando um quadrado, digite o lado\n")
        super().__init__(1)
        super().le_lados()
        
    def calcular_area(self):
        return self.lados[0]**2
    
    def calcular_perimetro(self):
        return self.lados[0]*4