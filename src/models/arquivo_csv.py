import csv
import json
import os.path
from datetime import datetime, timedelta


# Le o arquivo csv e retorna os dados lidos
def ler_arquivo_csv(caminho):
    # Abrindo arquivo csv
    with open(caminho, 'r') as file:
        # Criando um objeto leitor de CSV
        reader = csv.reader(file)

        dados_csv_ler = []

        # Iterando sobre cada linha do arquivo CSV
        for row in reader:
            dados_csv_ler.append(row)

        # Retorna lista com os dados
        return dados_csv_ler


# Funcao que inseri os dados dos exercicios no arquivo
def inserir_dados_arq_csv(dados, caminho):
    with open(caminho, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(dados)


########## USANDO JSON MICROCICLO  ##################
def inserir_dados_csv_json(dados, caminho):
    with open(caminho, 'w', newline='') as arquivo_csv:
        csvwriter = csv.writer(arquivo_csv)
        for row in dados:
            csvwriter.writerow([row[0], json.dumps(row[1])])


# Funcao que copia os dados do arquivo csv e retorna a lista dos dados
def copiar_dados_arq_csv(caminho):
    with open(caminho, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        data = []
        for row in csvreader:
            dia = row[0]
            treino = json.loads(row[1])
            data.append([dia, treino])

    return data
