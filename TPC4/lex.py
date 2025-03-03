import ply.lex as lex
import sys

tokens = ('SELECT','WHERE','VAR','LIMIT','DOT','LBRACE','RBRACE','LANGTAG','A','IDENTIFIER','STRING','NUMBER','COMMENT')

t_SELECT = r'select'
t_WHERE = r'where'
t_VAR = r'\?\w+'
t_LIMIT = r'LIMIT'
t_DOT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LANGTAG = r'@[a-zA-Z]+'
t_A = r'a'

def t_STRING(t):
    r'\".*\"'
    t.value = t.value.strip('"')
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+:[a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

def main(file):
    with open(file,"r") as f:
        data = f.read()
        lexer = lex.lex()
        lexer.input(data)
        for token in lexer:
            print(token)

if __name__ == '__main__':
    main(sys.argv[1])


