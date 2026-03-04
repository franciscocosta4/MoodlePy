import csv 
import requests 
import xml.etree.ElementTree as ET

XML_OUTPUT = "quiz.xml"

tree = ET.parse("template.xml")
root = tree.getroot()

with open("perguntas.csv", newline="") as ficheiro: 
    leitor = csv.reader(ficheiro, delimiter=";")
    next(leitor) #! Para a leitura dar skip ao cabeçalho 
    for linha in ficheiro: 
        linha = linha.strip()          # tira \n
        campos = linha.split(";")      # separa pelos ;
        print(campos)                  # ['dado1', 'dado2', 'dado3', ...]
        dados = {
            "id" : campos[0], 
            "tipo" : campos[1],
            "dificuldade" : campos[2], 
            "categoria": campos[3],
            "pergunta": campos[4],
            "opcao": campos[5],
            "correta": campos[6]
        }

# Mapeamento entre dados e XML
mapeamento = {
    "nome": "nomeCompleto",
    "idade": "anos"
}


# Preencher campos
for caminho, valor in dados.items():
    elemento = root.find(caminho)
    if elemento is not None:
        elemento.text = valor

# Guardar novo XML
tree.write(XML_OUTPUT, encoding="utf-8", xml_declaration=True)