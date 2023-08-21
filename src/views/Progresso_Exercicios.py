import PySimpleGUI as sg
import csv
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.controlers.trex import *
from src.models.Dados_Exercise import *

# Caminho para o meu arquivo csv
pasta = 'C:\FernandoLeao\Exercicios'
nome_arquivo = 'meus_exercicio.csv'
caminho_completo = os.path.join(pasta, nome_arquivo)


# Recebe a data de hoje em string
data_hoje_str = data_hoje()
cabecalho_hj = str_cabecalho_hj(data_hoje_str)


cabecalho_tabela = ['Data', 'Peso', 'Repeticoes']
cabecalho_dados = ['Data', 'Exercicio', 'Peso', 'Repeticoes']

################################################################
dados_treinos = ler_arquivo_csv(caminho_completo)
list_todos_exerc = lista_exercicios(dados_treinos)

if len(dados_treinos) == 0:
    dados_treinos.append(cabecalho_dados)



# str_cabecalho_hj(treino_semana, data_hoje),
layout = [
    [sg.Text(f'Hoje: {cabecalho_hj}', size=(48, 1), justification='center',
             relief=sg.RELIEF_RIDGE, font=("Helvetica", 18))],

    [sg.Text('Caminho do arquivo CSV'), sg.Input(caminho_completo, key='-INPUT_FILE_PATH-'),
     sg.Button('Trocar', expand_x=True, key='-TROCAR_PATH_CSV-')],

    [sg.Input(data_hoje_str, key='-IN_DATA-', size=(10, 1)),
     sg.CalendarButton('Calendario', format='%d/%m/%Y', close_when_date_chosen=True),
     sg.Button('Dia seguinte', key='-DIA_SEGUINTE-')],

    [sg.Input(key='-INPUT_NOVO_EXERC-', size=(20,1)), sg.Button('Criar novo exercicio', key='-NOVO_EXERCICIO-')],

    [sg.Combo(values=list_todos_exerc, key='-COMBO_EXERC-', size=(20,1)),
     sg.Text('Peso: '), sg.Input(size=(10,1), key='-IN_PESO-'), sg.Text('Repeticoes: '),
     sg.Input(size=(10,1), key='-IN_REP-'), sg.Button('Adicionar treino', key='-BUT_ADD_TREINO-')],

    [sg.Button('Tabela exercicio selecionado', key='-BUT_EXERC_TABLE-'),
     sg.Button('Tabela todos os exercicios', key='-BUT_EXERC_ALL-'),
     sg.Button('Adicionar dados ao arquivo', key='-ADD_DADOS_CSV-'),
     sg.Button('Grafico Exercicio', key='-GRAPH-')],

    [sg.Table(values=dados_treinos[1:], headings=dados_treinos[0], key='-TABLE_TREINOS-',
              enable_events=True, expand_x=True)]

]

window = sg.Window('Exercise-Tracker', layout)


def gerar_grafico(list_semana, list_peso, exerc):
    # Grafico de dispersao
    plt.figure(figsize=(10, 6))  # tamanho da figura

    # Funcao que retorna lista de inteiro e a logica para os ticks
    list_peso_int, list_y_ticks = list_pesoint_ticks(list_peso)

    # Plota o grafico com x = semana e y = pesos
    plt.bar(list_semana, list_peso_int, color='blue')

    # Descrição em cada eixo
    plt.xlabel('Semanas')
    plt.ylabel('Peso')

    # Ticks de cada eixo
    plt.xticks(list_semana)
    plt.yticks(list_y_ticks)

    # Linha vertical dos ticks de y
    plt.grid(axis='y')

    # Titulo em cima do grafico
    plt.title(f'Relação peso em cada semana no {exerc}')

    # Mostrar o grafico
    plt.show()



while True:
    event, values = window.read()

    # Se fechar a janela sai do loop e acaba o programa
    if event == sg.WIN_CLOSED:
        break

    # Abri uma janela para escolher novo caminho
    if event == '-TROCAR_PATH_CSV-':
        # Abre nova janela e seleciona o arquivo e troca o caminho do input
        folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
        sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
        window['-INPUT_FILE_PATH-'].update(folder_or_file)

    # Adiciona o novo exercicio a lista e atualiza o combo da janela com base na nova lista
    if event == '-NOVO_EXERCICIO-':
        novo_exerc = values['-INPUT_NOVO_EXERC-']
        list_todos_exerc.append(novo_exerc)
        window['-COMBO_EXERC-'].update(values=list_todos_exerc)

    # Botao que faz a tabela mostrar dados de apenas um exercicio
    if event == '-BUT_EXERC_TABLE-':
        # Lista de dados de apenas um exercicio
        info_do_exerc = dados_um_exercicio(dados_treinos, values['-COMBO_EXERC-'])
        # Atualiza a tabela com os dados dessa lista
        window['-TABLE_TREINOS-'].update(values=info_do_exerc[1:])
        print(info_do_exerc)


    # Botao que atualiza a tabela para mostrar todos exercicios que adicionou
    if event == '-BUT_EXERC_ALL-':
        window['-TABLE_TREINOS-'].update(values=dados_treinos[1:])


    # Botao que pega cria a lista com o exercicio/ treino, adiciona aos dados e atualiza a janela
    if event == '-BUT_ADD_TREINO-':
        # Cria a lista do treino com base nos valores da janela
        novo_treino_lista = [values['-IN_DATA-'], values['-COMBO_EXERC-'], values['-IN_PESO-'], values['-IN_REP-']]
        # Adicionando o novo treino a lista de dados
        dados_treinos.append(novo_treino_lista)
        # dados_um_exercicio retorna lista de informacoes do exercicio especifico que eu adicionei
        info_do_exerc = dados_um_exercicio(dados_treinos, values['-COMBO_EXERC-'])
        # Atualiza a tabela da janela
        window['-TABLE_TREINOS-'].update(values=info_do_exerc[1:])

    # Logica botao para avançar um dia
    if event == '-DIA_SEGUINTE-':
        # Recebe a data que esta escrita no input
        data_treino_in = values['-IN_DATA-']
        # Transforma em datetime
        data_treino_datetime = datetime.strptime(data_treino_in, '%d/%m/%Y')
        # Adiciona um dia neste datetima
        data_treino_datetime += timedelta(days=1)
        # Volta a data para string
        data_treino_str = data_treino_datetime.strftime("%d/%m/%Y")
        # Atualiza a janela
        window['-IN_DATA-'].update(data_treino_str)

    # Botao que chama funcao para escrever dados no arquivo csv
    if event == '-ADD_DADOS_CSV-':
        dados_treinos = organiza_dados_data(dados_treinos)
        inserir_dados_arq_csv(dados_treinos, caminho_completo)

    # Botao que chama funcao para plotar grafico
    if event == '-GRAPH-':
        # Variavel que recebe qual o exercicio que esta selecionado
        exerc_select = values['-COMBO_EXERC-']
        # Lista com as infos deste exericio especifico
        info_do_exerc = dados_um_exercicio(dados_treinos, exerc_select)
        # Variavel que recebe a lista das semans e dos pesoss
        list_semana, list_peso = listas_semana_e_peso(info_do_exerc)
        # Funcao que gera e plota o grafico
        gerar_grafico(list_semana, list_peso, exerc_select)
        pass



window.close()