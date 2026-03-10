import csv
from collections import defaultdict
import xml.etree.ElementTree as ET

caminho_csv = "perguntas.csv"
caminho_output_xml = "quiz.xml"

print(r"""
 __  __                 _ _       ____        
|  \/  | ___   ___   __| | | ___ |  _ \ _   _ 
| |\/| |/ _ \ / _ \ / _` | |/ _ \| |_) | | | |
| |  | | (_) | (_) | (_| | |  __/|  __/| |_| |
|_|  |_|\___/ \___/ \__,_|_|\___||_|    \__, |
                                        |___/ 


""")
def ler_csv(caminho_csv):
    perguntas = {}

    #perguntas é um dicionário, ou seja vai ter esta estrutura :
#     perguntas = {
#     "Q1": {
#         "type": "multichoice",
#         "questiontext": "...",
#         "answers": []
#     }
# }

    with open(caminho_csv, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';') # ? define o delimitador como ;

        for linha in reader: #? percorre cada linha do csv 
            QuestionId = linha["id"] # guarda o id da pergunta definido no inicio de cada linha 

            if QuestionId not in perguntas: # caso o id da pergunta ainda não foi registado
                #(ou seja a pergunta é outra) começa o registo de uma nova pergunta
                perguntas[QuestionId] = {
                    "type": linha["type"],
                    "difficulty": linha["difficulty"],
                    "category": linha["category"],
                    "questiontext": linha["questiontext"],
                    "answers": []
                }
            # toda a pergunta tem uma resposta e um fraction, que define quanto vale a resposta 
            perguntas[QuestionId]["answers"].append({ #regista a resposta da pergunta no dicionario "perguntas"
                "text": linha["answer"],
                "fraction": linha["fraction"]
            })
        print(perguntas)
    return list(perguntas.values())

ler_csv(caminho_csv)


def criar_xml(caminho_output_xml):
    
    root = ET.Element("quiz")

    
