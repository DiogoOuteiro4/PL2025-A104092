# TPC4 (Analisador Léxico)  

**Data:** 03 de março de 2025  

**Autor:**  
- **Nome:** Diogo Miguel Sousa Outeiro  
- **Número:** A104092  

![Foto do Aluno](image/yigaru4j.png)

## Resumo  
Este projeto implementa um programa em Python capaz de separar um texto em tokens baseado na linguagem SQL. Os resultados são escritos no terminal com a informação relativa a cada token, fornrcendo o seu tipo, o token encontrado, a linha em que se encontra e ainda a sua posição (índice no texto). Optei por ter o texto fornecido no enunciado do TPC4 num ficheiro em paralelo chamado `query.txt`. A implementação passou por recorrer ao `ply.lex`, mas também era possível fazer o TPC4 sem esta ferramenta como foi abordado na aula teórica.

## Implentação 
No início foi definida uma variável tokens que possui todos os tipos de tokens que o analisador léxico deveria reconhecer no ficheiro.Depois de ver o texto em causa, considerei que os tokens encontrados podem ser do tipo `SELECT`,`WHERE`,`LIMIT` que correspondem literalmente á palavra, `LBRACE`, `RBRACE`, `DOT` que seriam a chaveta da esquerda, da direita e ao ponto presente nos finais das linhas 4,5,6 e 7 do ficheiro, respetivamente.Para além disso, considerei tokens de `VAR` que equivale a strings que começem por `?`, `IDENTIFIER` caso estejam entre `:`, `STRING` quando estiver entre aspas, `NUMBER` para inteiros e `COMMENT` para comentários que acaba por ser algo que comece por `#`. No exemplo fornecido encontra-se um a isolado e eu considerei como token `A`.

O passo seguinte foi criar variáveis do tipo t_ que irão determinar como cada token irá ser reconhecido. Em certos casos apenas se criou uma expressão regular para tokens simples. No caso da String extrae-se as aspas e no Number converte-se de string para int. A variável t_ignore define os caracteres que o analisador deve ignorar.Neste caso, as tabulações e espaços são ignorados.Definiu-se ainda uma função para determinar os comentários mas que acaba por ser também ignorada.

A função t_newline(t) é uma função especial que lida com novas linhas, incrementando o número da linha do analisador léxico.

A função t_error(t) é chamada quando um caracter estranho é encontrado. Imprime uma mensagem de erro e avança para o caracter seguinte.

---

## Testes  

### Entrada de Teste:  
```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

### Saída Esperada:
```
LexToken(SELECT,'select',3,33)
LexToken(VAR,'?nome',3,40)
LexToken(VAR,'?desc',3,46)
LexToken(WHERE,'where',3,52)
LexToken(LBRACE,'{',3,58)
LexToken(VAR,'?s',4,60)
LexToken(A,'a',4,63)
LexToken(IDENTIFIER,'dbo:MusicalArtist',4,65)
LexToken(DOT,'.',4,82)
LexToken(VAR,'?s',5,84)
LexToken(IDENTIFIER,'foaf:name',5,87)
LexToken(STRING,'Chuck Berry',5,97)
LexToken(LANGTAG,'@en',5,110)
LexToken(DOT,'.',5,114)
LexToken(VAR,'?w',6,116)
LexToken(IDENTIFIER,'dbo:artist',6,119)
LexToken(VAR,'?s',6,130)
LexToken(DOT,'.',6,132)
LexToken(VAR,'?w',7,134)
LexToken(IDENTIFIER,'foaf:name',7,137)
LexToken(VAR,'?nome',7,147)
LexToken(DOT,'.',7,152)
LexToken(VAR,'?w',8,154)
LexToken(IDENTIFIER,'dbo:abstract',8,157)
LexToken(VAR,'?desc',8,170)
LexToken(RBRACE,'}',9,176)
LexToken(LIMIT,'LIMIT',9,178)
LexToken(NUMBER,1000,9,184)
```
Com base no output fornecido acima, chegou-se á conclusão que o analisador conseguiu dividir o texto corretamente com base nos tokens definidos ignorando também aquilo que foram as funções criadas. Este TPC4 permitiu aplicar os conhecimentos abordados na aula teórica da quarta semana e ainda explorar aquilo que o ply.lex oferece enquanto ferramenta.

