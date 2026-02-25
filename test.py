import csv 
import requests





print(r"""
 __  __                 _ _       ____        
|  \/  | ___   ___   __| | | ___ |  _ \ _   _ 
| |\/| |/ _ \ / _ \ / _` | |/ _ \| |_) | | | |
| |  | | (_) | (_) | (_| | |  __/|  __/| |_| |
|_|  |_|\___/ \___/ \__,_|_|\___||_|    \__, |
                                        |___/ 


""")
input("Começar a preencher as perguntas a partir do perguntas.csv? [Sim->enter] ")

url = input("Entre a url onde se encontra o formulario: (ex:https://httpbin.org/post) ").strip()

if url == "":
    url = "https://httpbin.org/post"
else:
    print(f"url escolhida: {url} , enviando as requests")
    
with open("perguntas.csv", newline="") as ficheiro: 
    leitor = csv.reader(ficheiro, delimiter=";")
    next(leitor) #! Para a leitura dar skip ao cabeçalho 
    for linha in ficheiro: 
        linha = linha.strip()          # tira \n
        campos = linha.split(";")      # separa pelos ;
        print(campos)                  # ['dado1', 'dado2', 'dado3', ...]
        dados = {
            "nome" : campos[0], 
            "email" : campos[1],
            "idade" : campos[2], 
            "telefone": campos[3]
        }
        resp = requests.post(url, data= dados)
        print(resp.status_code)
        print(resp.json()) 


# dados = {
#     "nome" : campos[0], 
#     "email" : campos[1],
#     "idade" : campos[2], 
#     "telefone": campos[3]
# }

# resp = requests.post(url, data= dados)

# print(resp.status_code)
# print(resp.json()) 