# TPC5 (Máquina de Estados)  

**Data:** 10 de março de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

![Foto do Aluno](image/yigaru4j.png)

# Explicação
O presente programa em python simula uma **máquina de vending**. A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço. No momento em que o programa correr é possível interagir com a máquina de algumas formas: **listar** os seus produtos, introduzir **moedas** para obter os seus itens, verificar o **saldo** e **sair** da máquina devolvendo o saldo que sobra. Como função extra recomendada no enunciado deste TPC5, também é possível **adicionar** produtos na máquina, quer já existentes quer novos. O stock encontra-se inicialmente armazenado num ficheiro JSON de nome "stock.json" que é carregado em memória quando o programa arranca. Quando o programa termina, o stock é gravado no mesmo ficheiro, mantendo assim o estado da aplicação entre interações

# Implementação
Foram criados tokens para cada operação possível mencionado anteriormente. Cada token tem associado uma expressão regular permitindo identificar corretamente as entradas do utilizador.

A máquina irá inicialmente demonstrar os comandos possíveis de forma a guiar o utilizador. A seguir estão explicados as suas funções:

- **LISTAR**: Informa todos os produtos em stock na máquina de vendas incluindo a informação de cada produto
- **SELECIONAR**: Permite o utilizador escolher o produto desejado mencionando o seu id que é único. Caso o saldo seja insuficiente a máquina informará e exibirá o preço do produto selecionado mais o saldo disponível.
- **MOEDA** : Adicionar saldo á máquina introduzindo moedas do tipo e(euros) e c(cêntimos). O argumento se for composto por mais moedas deve ser separado por ` ,` e sempre finalizador por um `.`
- **SALDO**: Exibe o saldo atual.
- **SAIR**: Sair da máquina e receber o devido troco.
- **ADICIONAR**: Incluir produtos existentes ou novos na máquina de vending. Recebe como argumento o nome do produto em causa e a sua quantidade. Se o produto for novo o sistema irá reconhecer,perguntará o seu preço e o seu identificador será +1 em relação ao produto com id superior.

## Ficheiro JSON
[Ficheiro JSON](stock.json)