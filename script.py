import csv
from collections import defaultdict
import xml.etree.ElementTree as ET

caminho_csv = "perguntas.csv"
caminho_output_xml = "quiz.xml"

print("Welcome to ... ")
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
    # o csv é plano, sem hierarquia, mas o xml precisa de ter organização para isso esta função lê as perguntas
    # do .csv e passa para um dicionario, ou seja vai ter esta estrutura :
#     perguntas = {
#     "Q1": {
#         "type": "multichoice",
#         "questiontext": "...",
#         "answers": []
#     }
# }
    
    with open(caminho_csv, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';') #  define o delimitador como ;

        for linha in reader: #percorre cada linha do csv 
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
            # toda a resposta tem o texto da resposta e um fraction, que define quanto vale a resposta 
            perguntas[QuestionId]["answers"].append({ #regista a resposta da pergunta no dicionario "perguntas"
                "text": linha["answer"],
                "fraction": linha["fraction"]
            })
        print("\n", perguntas)
    return list(perguntas.values())


def criar_xml(perguntas, caminho_output_xml):
    # esta função vai ler as perguntas guardadas no dicinário e vai passando uma a uma para xml 

    total_perguntas = len(perguntas)  # len() devolve o número de elementos numa lista
    print("TOTAL DE PERGUNTAS:", total_perguntas)

    # ET.Element() cria o elemento raiz do XML — escreve o <quiz>
    root = ET.Element("quiz")

    def adicionarpergunta(p): 

        #<name><text> → nome interno da pergunta (não é o enunciado)
        # <questiontext> → o enunciado real mostrado ao utilizador
        
        # SubElement em vez de Element porque <question> é child de <quiz>
        # type=p["type"] gera o atributo type="multichoice" ou type="truefalse"
        # sem este atributo o Moodle não saberia como interpretar a pergunta
        question = ET.SubElement(root, "question", type=p["type"])
        # ? TODO: IMPLEMENTAR SHUFFLE ENTRE ORDEM DAS PERGUNTAS

        # Gera: <name><text>...</text></name>
        name = ET.SubElement(question, "name")
        ET.SubElement(name, "text").text = p["questiontext"][:50] # [:50] é um slice — extrai os primeiros 50 caracteres da string
        
        # format="html" é exigido pelo Moodle para interpretar corretamente
        # o conteúdo como HTML (permitindo <code>, <b>, etc. no enunciado)
        questiontext = ET.SubElement(question, "questiontext", format="html")
        text_element = ET.SubElement(questiontext, "text")
        text_element.text = p["questiontext"]  # .text define o conteúdo dentro da tag XML

        #diz ao moodle para dar shuffle entre as opções de uma pergunta
        ET.SubElement(question, "shuffleanswers").text = "true"

        # Itera sobre a lista de respostas de cada pergunta
        for ans in p["answers"]:
            # str() converte o valor numérico de "fraction" em string,
            # porque os atributos XML têm de ser sempre strings
            answer = ET.SubElement(question, "answer", fraction=str(ans["fraction"]))

            answer_text = ET.SubElement(answer, "text")
            answer_text.text = ans["text"]

    for p in perguntas:
        adicionarpergunta(p)

    # ET.ElementTree() envolve o elemento raiz numa estrutura que pode ser escrita em ficheiro
    tree = ET.ElementTree(root)

    # .write() grava o XML no disco
    # xml_declaration=True adiciona <?xml version='1.0' encoding='utf-8'?> no início
    tree.write(caminho_output_xml, encoding="utf-8", xml_declaration=True)

    # f"..." é uma f-string, serve para podermos por variáveis dentro de strings com {}
    print(f"XML criado em: {caminho_output_xml}")



perguntas = ler_csv(caminho_csv)    
criar_xml(perguntas, caminho_output_xml)