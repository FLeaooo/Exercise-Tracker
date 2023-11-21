import json

def ler_json(caminho):
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
