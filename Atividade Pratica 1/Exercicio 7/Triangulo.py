from FormaGeometrica import FormaGeometrica

class Triangulo(FormaGeometrica):
    def __init__(self):
        print("Você está instânciando um triângulo. Digite os 3 lados \n")
        super().__init__(3)
        super().le_lados()

    def calcular_perimetro(self):
        soma = 0
        for lado in self.lados:
            soma = soma + lado
        
        return soma
    
    def calcular_area(self):
        s = (self.lados[0] + self.lados[1] + self.lados[2])/2
        return (s*(s-self.lados[0])*(s-self.lados[1])*(s-self.lados[2]))**0.5
        
    def triangulo_retangulo(self):
        lados_ordenados = sorted(self.lados)
        if lados_ordenados[0]**2 + lados_ordenados[1]**2 == lados_ordenados[2]**2:
            return True
        else:
            return False