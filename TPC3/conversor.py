import re

def conversor(texto):
    # Cabeçalhos
    texto = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto, flags=re.MULTILINE)

    # Bold (negrito)
    texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)

    # Itálico
    texto = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto)

    # Lista numerada
    texto = re.sub(r"^\d+\.\s*(.*)", r"<li>\1</li>", texto, flags=re.MULTILINE)
    texto = re.sub(r"(\n<li>.+?</li>)+",r'\n<ol>\g<0>\n<ol>',texto)

    # Imagem
    texto = re.sub(r"!\[(.*?)\]\((.*?)\)", r'Como se vê na imagem seguinte: <img src="\2" alt="\1"/>', texto)

    # Link
    texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)

    return texto

def main():
    input_file = "input.md"  
    output_file = "output.html"  

    with open(input_file, "r", encoding="utf-8") as file:
        md_content = file.read()
        html_content = conversor(md_content)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

if __name__ == "__main__":
    main()



        

        
    