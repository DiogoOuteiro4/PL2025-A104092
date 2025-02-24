# TPC3 (Conversor de MarkDown para HTML)  

**Data:** 24 de fevereiro de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

![Foto do Aluno](image/yigaru4j.png)

## Resumo  
Este projeto implementa um programa em Python capaz de converter MarkDown para HTML. No enunciado desta semana foram apresentados alguns exemplos como: Cabeçalhos, texto bold, texto itálico, lista numerada, link e imagem. A base da resolução foi utilizar expressões regulares associadas ás estruturas de cada um . Decidi criar um ficheiro MarkDown denominado `input.md` lido para o programa que posteriormente escreve em formato html a solução no ficheiro `output.html`.

No que toca á implementação em si, foi utilizado o método "sub" da biblioteca re, que recebe uma expressão regular e faz a troca presente no segundo argumento. Apenas na listas numeradas é que foi preciso fazer a substituição duas vezes. Primeiro, faço com que entre em cada linha entre o nome das linhas fique "li" e depois isolo a expressão toda e acrescente o "ol".

---

## Resultados 
[Ficheiro html](output.html)


