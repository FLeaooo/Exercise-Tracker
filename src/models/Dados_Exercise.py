import csv
import os.path
from datetime import datetime, timedelta
from ast import literal_eval

from src.models.arquivo_csv import *


cabecalho = ['Data', 'Exercicio', 'Peso', 'Repeticoes']


# Cria uma lista so dos exercicios percorrendo a lista de dados
def lista_exercicios(lista_dados):
    lista_exerc = []
    # Percorre a lista ignorando o cabecalho
    for linha in lista_dados[1:]:
        # Se na pos de exercicio nao estiver na lista de exercicios
        if linha[1] not in lista_exerc:
            # Adiciona o exercicio na lista
            lista_exerc.append(linha[1])

    # Retorna a lista de todos os exercicios
    return lista_exerc


# Cria uma lista com as informações de somente um exercicio
def dados_um_exercicio(dados_treino, exercicio):
    info_um_exerc = [dados_treino[0]]
    for linha in dados_treino[1:]:
        if linha[1] == exercicio:
            info_um_exerc.append(linha)

    return info_um_exerc


# Organiza os dados pela data
def organiza_dados_data(dados):
    def converter_data(data_str):
        return datetime.strptime(data_str, '%d/%m/%Y')

    # Ordena a lista de dados pela data
    dados_ordenados = sorted(dados[1:], key=lambda x: converter_data(x[0]))
    dados_ordenados.insert(0, cabecalho)

    return dados_ordenados


# retorna lista de semanas e lista de pesos
def listas_semana_e_peso(dados):
    lista_semana = []
    lista_peso = []

    primeiro_treino = dados[1]
    ultimo_treino = dados[-1]

    # Recebe a data str = '05/06/2023'
    primeira_data_str = primeiro_treino[0]
    ultima_data_str = ultimo_treino[0]


    # Transforma data str em datetime
    primeira_data_datetime = datetime.strptime(primeira_data_str, '%d/%m/%Y')
    ultima_data_datetime = datetime.strptime(ultima_data_str, '%d/%m/%Y')

    # Recebe a semana do ano desta data
    primeira_semana = primeira_data_datetime.isocalendar()[1]
    ultima_semana = ultima_data_datetime.isocalendar()[1]


    lista_semana_completa = []
    # Gero a lista de semanas, desde o primeiro dado ate a semana de hoje
    for semana in range(primeira_semana, ultima_semana+1):
        lista_semana_completa.append(semana)

    index = 0
    for linha in dados[1:]:

        # recebe a data string
        data_linha_str = linha[0]
        # Transforma em datetime
        data_linha_datetime = datetime.strptime(data_linha_str, '%d/%m/%Y')
        # Recebe a semana do ano desta data
        num_semana_linha = data_linha_datetime.isocalendar()[1]

        lista_semana.append(num_semana_linha)
        lista_peso.append(linha[2])



    for i, semana in enumerate(lista_semana_completa):
        if semana != lista_semana[i]:
            print(f'Semana {semana}')
            print(f'Peso {lista_peso[i-1]}')
            lista_semana.insert(i, semana)
            lista_peso.insert(i, lista_peso[i-1])

    print(lista_semana)
    print(lista_peso)

    print(len(lista_semana))
    print(len(lista_peso))
    print(len(lista_semana_completa))


    for j in range(len(lista_semana)):
        print(f'semana: {lista_semana[j]} peso {lista_peso[j]}')


    return lista_semana, lista_peso


# Retorna lista de peso em int e uma lista de ticks para o grafico
def list_pesoint_ticks(list_peso_str):

    list_peso_int = []
    # Transformando a lista de peso string em lista de inteiro
    for str_peso in list_peso_str:
        int_peso = int(str_peso)
        list_peso_int.append(int_peso)

    # Irei ter 3 opcoes de evolucao e ticks de peso (2 em 2, 5 em 5, 10 em 10)
    # Exemplo: Biceps scott(2e2) Supino(5e5) legpress(10e10)
    # Isto para ficar mais facil a vizualização
    ticks = 0
    peso_max = max(list_peso_int)
    if peso_max < 30:
        ticks = 2
    elif peso_max < 60:
        ticks = 5
    else:
        ticks = 10

    # Cria e adiciona valores na lista ticks, de 0 ate +10 pulando de (2,5,10) dependendo do exercicio
    list_ticks = []
    for j in range(0, peso_max+11, ticks):
        list_ticks.append(j)


    return list_peso_int, list_ticks

