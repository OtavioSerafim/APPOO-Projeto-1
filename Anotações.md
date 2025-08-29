# Especificação do diagrama UML

Para as classes:

- **Nome:** em *PascalCase*
- **Atributos públicos:** colocar um `+` anterior ao nome do atributo/método
- **Atributos privados:** colocar um `-` anterior ao nome do atributo/método
- **Modelo para atributos:**  
    `visibilidade (+/-) nomeAtributo : tipo (str, bool, int) = valor default`
- **Tabela:** repartir o meio da tabela mesmo que a classe não tenha atributos/métodos
- **Modelo para métodos:**  
    `visibilidade nomeMétodo(listaArgumentos de preferência no modelo nomeArgumento:tipoArgumento): tipoRetorno`
- **Conexão entre tabelas:** Quando for herança, usa-se seta, quando uma classe tem acesso a outra, usa-se linha.

# Especificações para Classe

- **Construtor:** O construtor é feito por meio do método:

    ```python
    def __init__(self, atributo: tipo):
        self.atributo = atributo
    ```

- **Ao instânciar:** O código fica:

    ```python
    objeto1 = Classe(atributo1, atributo2, ... ,atributoN)
    ```

- **Métodos:** Ao instânciar métodos é necessário o uso do self:
    ```python
    class ClasseExemplo:
        def __init__(self, atributoExemplo1: str, atributoExemplo2: str):
            self.atributoExemplo1 = atributoExemplo1
            self.atributoExemplo2 = atributoexemplo2

        def metodoExemplo(self):
            print("Exemplo")

    objetoExemplo = ClasseExemplo("Teste","Teste2")
    
    objetoExemplo.metodoExemplo()
    ```

