 TPC1 (Somador On/Off)  

**Data:** 08 de fevereiro de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

## Resumo  
Este projeto implementa um programa em Python para somar números em um texto fornecido via entrada padrão. As regras principais do programa são:  

1. Sempre que a string "Off" (em qualquer combinação de maiúsculas e minúsculas) é encontrada, a funcionalidade de soma é desativada.  
2. Quando a string "On" (em qualquer combinação de maiúsculas e minúsculas) é encontrada, a funcionalidade de soma é reativada.  
3. Sempre que o caractere `=` é encontrado, o resultado da soma acumulada até o momento é exibido.  

O código lê sequencialmente caracteres de um texto fornecido pela entrada padrão (stdin) para somar sequências de dígitos encontradas. A variável `calculadora_ativada` identifica se o comportamento está ligado conforme são detetadas strings "On" ou "Off". Caso seja detetado um On, o `numero_atual` é atualizado e a variável `numero_em_construcao` passa a True o que indica que o programa está a montar um número válido. Se o programa estiver numa fase de construção de número e a seguir deteta algo que não seja um dígito, a `soma_total` acumula o valor da soma , o numero_atual volta a 0 e numero_em_construcao volta a False. O TPC1 pode ser resolvido com expressões regulares, porém o objetivo era resolver o problema sem esse recurso. 

 
---

## Testes  

### Entrada de Teste:  
```
123On456=
Off789On10=
20Off30On50=
On25=
100Off1000On5=
```

### Saída Esperada:
```
A Soma atual é : 579
A Soma atual é : 589
A Soma atual é : 659
A Soma atual é : 684
A Soma atual é : 689
```

O teste apresentado em cima foi um exemplo utilizado para testar o funcionamento do programa. Após isto chega-se á conclusão que foi possível lidar corretamente com números, controlar estados "On" e "Off", e apresentar os resultados quando solicitado. O programa foi testado com textos de variados tamanhos e mesmo assim confirmou-se a sua execução correta.
