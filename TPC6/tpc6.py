import ply.lex as lex


#Analisador léxico
tokens = ("NUM","PLUS","MINUS","TIMES")


def t_NUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_PLUS = r"\+"

t_MINUS = r"\-"

t_TIMES = r"\*"

t_ignore =" /t"

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()
prox_simb = None
#Analisador sintático
def rec_exp():
    global prox_simb
    valor = rec_exp2()
    while prox_simb and prox_simb.type in ("PLUS", "MINUS"):
        operador = prox_simb.type
        prox_simb = lexer.token()
        if operador == "PLUS":
            valor += rec_exp2()
        else:
            valor -= rec_exp2()
    return valor

def match(tipo):
    global prox_simb
    if prox_simb and prox_simb.type == tipo:
        valor = prox_simb.value
        prox_simb = lexer.token()
        return valor
    else:
        raise SyntaxError(f"Erro de sintaxe: esperado {tipo}, encontrado {prox_simb}")


def rec_exp2():
    global prox_simb
    valor = match("NUM")
    while prox_simb and prox_simb.type == "TIMES":
        prox_simb = lexer.token()
        valor *= match("NUM")
    return valor

def rec_parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_exp()

while True:
    try:
        expr = input("Digite uma expressão matemática: ")
        if not expr:
            break
        resultado = rec_parser(expr)
        print ("Resultado:", resultado)
    except (EOFError, SyntaxError) as e:
        print(e)
        break