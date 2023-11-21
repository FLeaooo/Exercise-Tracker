import PySimpleGUI as sg

from src.models.model_periodizacao import *

################ DADOS #################

path_dados_json = 'C:/FernandoLeao/Exercicios/meus/dadosMacro.json'

dados_json = ler_json(path_dados_json)


semanas = dados_json['Semanas']

micro_ciclo = dados_json['Micro_Ciclo']
meso_ciclo = dados_json['Meso_Ciclo']
dados_calistenia = dados_json['Dados_Calistenia']
dados_Gym = dados_json['Dados_Gym']
print(dados_Gym)
print(dados_calistenia)


def criar_lista_tabela_gym(dados, exercicio, semanas):
    lista_exercicios = [['Semana', 'Periodo', 'Exercicio', 'Peso']]
    for linha in dados:
        if linha[1] == exercicio:
            lista_exercicios.append(linha[:])


    for indice, linha in enumerate(lista_exercicios[1:]):
        if indice <= int(semanas[0]):
            linha.insert(1, 'Base')
        elif indice <= int(semanas[0]) + int(semanas[1]):
            linha.insert(1, 'Forca')
        elif indice <= int(semanas[0]) + int(semanas[1]) + int(semanas[1]):
            linha.insert(1, 'Shock')


    return lista_exercicios


def lista_nomes_exerc(dados):
    lista_exerc = []
    for linha in dados:
        if linha[0] == 0:
            lista_exerc.append(linha[1])

    return lista_exerc


lista_sup = criar_lista_tabela_gym(dados_Gym, 'Sup Inc Maq', semanas)
lista_nomes_ex = lista_nomes_exerc(dados_Gym)
nome_exerc = ''


layout = [
    [sg.Text('Exercicios para ver evolucao:'), sg.Combo(lista_nomes_ex), sg.Button('Confirmar')],
    [sg.Table(values=lista_sup[1:], headings=lista_sup[0], expand_x=True)]
        ]

window = sg.Window('Periodizacao', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()
