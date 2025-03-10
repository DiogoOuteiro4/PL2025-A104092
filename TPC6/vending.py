import re
import ply.lex as lex
import json

tokens = ['SELECIONAR','LISTAR','MOEDA','SALDO','SAIR','ADICIONAR']

def t_LISTAR(t):
    r'LISTAR'
    print("""maq:
---------------------------------------------------
|  cod  |       nome        | qtd |  preço (€)  |
---------------------------------------------------""")
    for produto in t.lexer.data['stock']:
        print(f"| {str(produto['id']).ljust(5)} | {produto['nome'].ljust(18)} | {str(produto['quantidade']).rjust(3)} | {str(produto['preco']).rjust(8)} |")

    print("---------------------------------------------------")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\d+'
    produto_id = int(t.value.split()[1])
    length = len(t.lexer.data['stock'])
    if (produto_id < 0 or produto_id > length):
        print(f"Produto {produto_id} inexistente")
    for elem in t.lexer.data['stock']:
        if elem['id'] == produto_id:
            if elem['quantidade'] > 0:
                if elem['preco']*100 <= t.lexer.saldo:
                    elem['quantidade'] -= 1
                    t.lexer.saldo = int(t.lexer.saldo - elem['preco'] * 100)
                    print(f"maq: Pode retirar o produto dispensado {elem['nome']}")
                    calcula_saldo(t)
                    with open("stock.json","w",encoding="utf-8") as file:
                        json.dump(t.lexer.data,file,indent=2, ensure_ascii=False)
                else:
                    print("Saldo Insuficiente para satisfazer o seu pedido")
                    calcula_saldo(t)
                    print(f"Pedido: {elem['preco']}")
            else:
                print(f"Produto esgotado:{elem['nome']}")
                break
    return t
        
                    

def t_MOEDA(t):
    r'MOEDA\s+(\d+[ec](,\s*\d+[ec])*\s*\.)'
    padrao = r'(\d+)(e|c)'
    correspondencia = re.findall(padrao,t.value)
    for valor,tipo in correspondencia:
        valor = int(valor)
        if tipo == 'e':
            t.lexer.saldo += valor * 100
        else:
            t.lexer.saldo += valor

    euros = t.lexer.saldo // 100
    centimos = t.lexer.saldo % 100

    if centimos == 0:
        print(f"maq: Saldo = {euros}e")
    else:
        print(f"maq: Saldo = {euros}e{centimos:02d}")

    return t



def t_SALDO(t):
    r'SALDO'
    euros = t.lexer.saldo // 100
    centimos = t.lexer.saldo % 100

    if centimos == 0:
        print(f"maq: Saldo disponível = {euros}e")
    else:
        print(f"maq: Saldo disponível = {euros}e{centimos:02d}")
    return t

def calcula_saldo(t):
    euros = int(t.lexer.saldo // 100)
    centimos = int (t.lexer.saldo % 100)

    if centimos == 0:
        print(f"maq: Saldo disponível = {euros}e")
    else:
        print(f"maq: Saldo disponível = {euros}e{centimos:02d}")
    return t



def t_SAIR(t):
    r'SAIR'
    euros = t.lexer.saldo // 100
    centimos = t.lexer.saldo % 100

    if centimos == 0:
        print(f"maq: Troco = {euros}e")
    else:
        print(f"maq: Troco  = {euros}e{centimos:02d}")
        
    print("Até á próxima!")
    t.lexer.flag = 1
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s\w+\s\d+'
    nome_produto  = t.value.split()[1]
    quantidade = int(t.value.split()[2])
    encontrado = 0
    for produto in t.lexer.data['stock']:
        if produto['nome'] == nome_produto:
            encontrado = 1
            produto['quantidade']+=quantidade
            with open("stock.json","w",encoding="utf-8") as file:
                json.dump(t.lexer.data,file,indent=2, ensure_ascii=False)
            print(f"Produto reposto com sucesso: {nome_produto}")
    if encontrado == 0:
        print(f"A registar novo produto: {nome_produto}")
        id_produto = len(t.lexer.data['stock']) + 1
        preco = float(input("Insira o preço do novo produto: "))
        with open("stock.json","w",encoding="utf-8") as file:
            t.lexer.data['stock'].append({'id': id_produto, 'nome': nome_produto, 'quantidade': quantidade, 'preco': preco})
            json.dump(t.lexer.data,file,indent=2, ensure_ascii=False)
        print(f"Produto novo inserido na máquina!")
    return t





def t_error(t):
    t.lexer.skip(1)

def main():
    lexer = lex.lex()
    with open("stock.json","r",encoding ="utf-8") as file:
        data = json.load(file)
    
    lexer.data = data
    lexer.saldo = 0
    lexer.flag = 0

    mensagem_Inicial = """
    Stock carregado, Estado atualizado,
    Bom dia! Estou disponível para atender o seu pedido
    Comandos:
    - LISTAR
    - MOEDA <quantia>e <quantia>c
    - SALDO
    - ADICIONAR <produto> <quantia>
    - SELECIONAR <id produto>
    - SAIR
    """

    print(mensagem_Inicial)


    while (lexer.flag == 0):
        input_maquine =input(">>") 
        lexer.input(input_maquine)
        token = lexer.token()
        if not token:
            print("Operação Inválida")

if __name__ == "__main__":
    main()
