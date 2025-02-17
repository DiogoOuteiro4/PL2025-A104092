# TPC2 (Análise de um dataset de obras musicais)  

**Data:** 17 de fevereiro de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

![Foto do Aluno](image/yigaru4j.png)

## Resumo  
Este projeto implementa um programa em Python capaz de analisar um ficheiro csv sobre obras musicais e num ficheiro denominado de `resultados.txt` imprime os resultados esperados de cada questão exigida no enunciado. Inicialmente, o ficheiro `obras.csv` não se encontrava bem formatada, pois uma obra possuia quebras de linha e espaços sucessivos. Para isso foi criada uma expressão regular que permite com que cada linha do ficheiro conte-se uma obra. O ficheiro correto corresponde ao `obras_corretas.csv`.


- **Questão 1:**  Nesta primeira alínea, o objetivo era ordenar todos os compositores por ordem alfabética. A solução passou por criar uma expressão regular que identifica-se o ano de criação, o período e o devido compositor. O programa percorre as linhas todas do ficheiro .csv correto e depois os compositores são armazenados numa lista caso não pertencem nesta de forma a evitar a ter os mesmos nomes. Depois o resultado é imprimido
- **Questão 2:** Na segunda questão, o objetivo era determinar o número de obras por períodos distintos. A estratégia acaba por ser muita semelhante ao da questão 1. Através de uma expressão regular, identifica-se o período e ao percorrer as linhas do ficheiro, incrementa-se o valor desse mesmo período caso exista ou define-se como 1 sendo a primeira vez que ocorre.
- **Questão 3:** Na terceira questão, o objetivo seria criar um dicionário com as obras associadas a um período. A partir de uma expressão regular identifica-se o nome da obra e o seu período sucessivamente. Armazeno o período no respetivo dicionário e depois e associo a obra em questão. Após ser tudo guardado no dicionário, percorro os períodos e ordeno as obras por ordem alfabética. 

---

## Resultados 
[Ficheiro .csv alterado](obras_corretas.csv)
[Ficheiro de resultados](resultados.txt)
[Ficheiro com código](dataset.py)