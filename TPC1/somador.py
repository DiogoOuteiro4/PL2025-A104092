import sys

def main():
    calculadora_ativada = True
    soma_total = 0
    numero_atual = 0
    numero_em_construcao = False

    for linha in sys.stdin:
        i = 0
        while i < len(linha):
            char = linha[i]

            if linha[i:i + 3].lower() == "off":
                if numero_em_construcao:
                    soma_total += numero_atual
                    numero_atual = 0
                    numero_em_construcao = False

                calculadora_ativada = False
                i += 3
                continue

            elif linha[i:i + 2].lower() == "on":
                if calculadora_ativada and numero_em_construcao:
                    soma_total += numero_atual
                    numero_atual = 0
                    numero_em_construcao = False
                calculadora_ativada = True
                i += 2
                continue

            if char.isdigit() and calculadora_ativada:
                numero_em_construcao = True
                numero_atual = numero_atual * 10 + int(char)
            else:
                if numero_em_construcao:
                    soma_total += numero_atual
                    numero_atual = 0
                    numero_em_construcao = False

            if char == "=":
                if numero_em_construcao:
                    soma_total += numero_atual
                    numero_atual = 0
                    numero_em_construcao = False
                print(f"A Soma atual é : {soma_total}")

            i += 1

if __name__ == "__main__":
    main()