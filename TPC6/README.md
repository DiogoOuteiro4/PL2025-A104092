# TPC6 (Gramática Independente de Contexto)  

**Data:** 10 de março de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

![Foto do Aluno](image/yigaru4j.png)

# Resumo
Este TPC consiste na implementação de uma gramática independente de contexto para representar expressões aritméticas simples. A gramática é composta por símbolos terminais, não terminais, regras de produção e axioma.

### Exemplo:
```
5 + 3 * 2
2 * 7 - 5 * 3
```

# Resolução
```
T = {'+','*',num, '-'}
S = Exp
N = {Exp,Exp2,Sinal,Sinal2}

P->{
    Exp -> Exp2 Sinal
    Sinal -> '+' Exp
            | '-' Exp
            | empty

    Exp2 -> num Sinal2
    Sinal2 -> '*' Exp2
            | empty
}
```




