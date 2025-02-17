import re
import os

with open("obras.csv", "r", encoding="utf-8") as f:
    conteudo_errado = f.readlines()

cabecalho = conteudo_errado[0]
conteudo_restante = "".join(conteudo_errado[1:])

obras_correto = re.sub(r'\n\s+', ' ', conteudo_restante)

if not os.path.exists("resultados.txt"):
    with open ("resultados.txt", "w", encoding="utf-8") as resultados:
        resultados.write("Ficheiro obras.csv criado:\n")

with open("obras_corretas.csv", "w", encoding="utf-8") as ficheiro2:
    ficheiro2.write(cabecalho)
    ficheiro2.write(obras_correto)

with open("obras_corretas.csv", "r", encoding="utf-8") as ficheiro2:
    dataset = ficheiro2.read()
    
padrao_compositor = r';\d\d\d\d;.*?;(.*?);'
compositores = []

for linha in dataset.split("\n"):
    linha = linha.strip()

    correspondencia = re.search(padrao_compositor,linha)

    if correspondencia:
        compositor = correspondencia.group(1).strip()
        if compositor not in compositores:
            compositores.append(compositor)

compositores = sorted(compositores)

with open("resultados.txt", "a", encoding="utf-8") as resultados:
    resultados.write("Lista ordenada de compositores: " + str(compositores) + "\n\n")

padrao_periodo = r';\d\d\d\d;(.*?);'
periodos = {}

for linha in dataset.split("\n"):
    linha = linha.strip()

    correspondencia2 = re.search(padrao_periodo,linha)

    if correspondencia2:
        periodo = correspondencia2.group(1).strip()
        if periodo:
            periodos[periodo] = periodos.get(periodo,0) + 1

with open("resultados.txt", "a", encoding="utf-8") as resultados:
    resultados.write("Quantidade de obras por período:\n")

    for periodo, quantidade in periodos.items():
        resultados.write(f"{periodo}: {quantidade}\n")

    resultados.write("\n")

padrao_dicionario = r'^(.+?);(.+?);\d{4};(.+?);'
dicionario = {}

for linha in dataset.split("\n"):
    linha = linha.strip()

    correspondencia3 = re.search(padrao_dicionario,linha)

    if correspondencia3:
        nome = correspondencia3.group(1).strip()
        periodo = correspondencia3.group(3).strip()

        dicionario[periodo] = dicionario.get(periodo, []) + [nome]

for periodo, obras in dicionario.items():
    obras.sort()

with open("resultados.txt", "a", encoding="utf-8") as resultados:
    resultados.write("Obras por período:\n")

    for periodo, obras in dicionario.items():
        resultados.write(f"{periodo}: {len(obras)} obras\n")

        for obra in obras:
            resultados.write(f" - {obra}\n")

    resultados.write("\n")



