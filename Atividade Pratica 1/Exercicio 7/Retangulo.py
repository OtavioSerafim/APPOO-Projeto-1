from FormaGeometrica import FormaGeometrica

class Retangulo(FormaGeometrica):
    def __init__(self):
        print("Você está instânciando um retângulo. Digite a base e altura:\n")
        super().__init__(2)
        super().le_lados()

    def calcular_perimetro(self):
        soma = 0
        for lado in self.lados:
            soma = soma + lado*2
        
        return soma
    
    def calcular_area(self):
        return self.lados[0]*self.lados[1]