import csv


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
