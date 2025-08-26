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