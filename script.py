import csv
from collections import defaultdict
import xml.etree.ElementTree as ET

caminho_csv = "perguntas.csv"

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
                    "difficulty": linha["dificultity"],
                    "category": linha["category"],
                    "questiontext": linha["questiontext"],
                    "answers": []
                }
            # toda a pergunta tem uma resposta e um fraction, que define quanto vale a resposta 
            perguntas[QuestionId]["answers"].append({ #regista a resposta da pergunta no dicionario "perguntas"
                "text": linha["answer"],
                "fraction": linha["fraction"]
            })

    return list(perguntas.values())