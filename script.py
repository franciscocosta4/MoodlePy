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
perguntas = {}
def ler_csv(caminho_csv):
    

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
        print("\n", perguntas)
    return list(perguntas.values())


def criar_xml(perguntas, caminho_output_xml):
    total_perguntas = len(perguntas)
    print( "TOTAL DE PERGUNTAS:", total_perguntas)
    
    root = ET.Element("quiz")
    def adicionarpergunta(p): 
        
        question = ET.SubElement(root, "question", type =p["type"])
        
        #name
        name = ET.SubElement(question, "name")
        ET.SubElement(name,"text").text = p["questiontext"][:50]

        questiontext= ET.SubElement(question, "questiontext" ,format = "html")
        text_element = ET.SubElement(questiontext, "text")
        text_element.text = p["questiontext"]

        ET.SubElement(question, "shuffleanswers").text = "true"
        
        # <answer>
        for ans in p["answers"]:
            answer = ET.SubElement(question, "answer", fraction=str(ans["fraction"]))
            
            answer_text = ET.SubElement(answer, "text")
            answer_text.text = ans["text"]  # sem CDATA

    for p in perguntas:
        adicionarpergunta(p)
    
    tree = ET.ElementTree(root)
    tree.write(caminho_output_xml, encoding="utf-8", xml_declaration=True)
    print(f"XML criado em: {caminho_output_xml}")


perguntas = ler_csv(caminho_csv)    
criar_xml(perguntas, caminho_output_xml)
    


    
