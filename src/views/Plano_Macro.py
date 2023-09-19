import PySimpleGUI as sg
import subprocess

from src.models.model_macro import *



lista_musculos = ['Peito', 'Costas', 'Ombros', 'Bíceps', 'Tríceps',
                  'Antebraço','Quadriceps', 'Posterior','Abdômen', 'Panturilha']

volume_base = [['Musculo', 'Volume']]

peso_base = [['Exercicio', 'Peso (10-12Rep)']]

lista_exercicios_acompanhar = []

meso_base = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]
meso_forca = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]
meso_shock = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]

caminho_micro_csv = 'C:/FernandoLeao/Exercicios/meus/MicroCiclo.csv'
caminho_meso_csv = 'C:/FernandoLeao/Exercicios/meus/MesoCiclo.csv'
caminho_pasta = 'C:/FernandoLeao/Exercicios/meus/'
nome_json = 'dadosMacro.json'



def executar_arquivo(arq):
    if arq == 'Micro':
        subprocess.call(['python', 'MicroCiclo.py'])
    elif arq == 'Meso':
        subprocess.call(['python', 'MesoCiclo.py'])


layout = [
    [sg.Frame('Informações para o MacroCiclo', [
        [sg.Text('Informacoes (opcional):\nEx: Nome, peso, cardio... '), sg.MLine(size=(40,2), key='-MLINE_INFO-')],

        [sg.Text('Data de inico - 1° semana - Segunda-Feira:'), sg.Input(size=(20, 1), key='-IN_DATA_INICIO-'),
         sg.CalendarButton('Calendario', target='-IN_DATA_INICIO-', format='%d/%m/%Y')],

        [sg.Text('Semanas Base:  '), sg.Input('4', size=(3, 1), key='-IN_BASE-'),
         sg.Text('Semanas Forca: '), sg.Input('4', size=(3, 1), key='-IN_FORCA-'),
         sg.Text('Semanas Shock:'), sg.Input('4', size=(3, 1), key='-IN_SHOCK-')],


    ], expand_x=True)],

    [sg.Frame('MicroCiclo, treino Semanal',[
        [sg.Text('Para criar planejamento de treino (MacroCiclo) é necessario ter o treino semanal (MicroCiclo):')],

        [sg.Button('Abrir arquivo MicroCiclo',expand_x=True, key='-BUT_ABRIR_ARQ_MICRO-'),
         sg.Button('Criar treino e arquivo MicroCiclo',expand_x=True, key='-BUT_CRIAR_MICRO-')],

        [sg.Text('Caminho CSV (treino semanal):'),
         sg.Input(caminho_micro_csv, size=(50,1), key='-IN_PATH_MICRO-')],

    ])],

    [sg.Frame('MesoCiclo, planejamento mes a mes', [
        [sg.Text('Para criar planejamento de treino (MacroCiclo) é necessario ter o planejamento de cada mes (MesoCiclo):')],
        [sg.Button('Abrir arquivo MesoCiclo', expand_x=True, key='-BUT_ABRIR_ARQ_MESO-'),
         sg.Button('Criar arquivo MesoCiclo', expand_x=True, key='-BUT_CRIAR_MESO-')],
        [sg.Text('Caminho CSV (Exercicios Acompanhar (Meso)):'),
         sg.Input(caminho_meso_csv, size=(40,1), key='-IN_PATH_MESO-', expand_x=True)],
    ])],

    [sg.Frame('Criar dados Macro Ciclo', [
        [sg.Button('Caminho Para Pasta do JSON', expand_x=True, key='-BUT_PATH_FILE-')],
        [sg.Text('Caminho JSON (Periodização (Macro)):'), sg.Input(caminho_pasta, size=(40,1), key='-IN_PATH_MACRO-')],
        [sg.Button('Confirmar', key='-BUT_CRIAR_MACRO-', size=(20,2)),
         sg.Text('Nome do arquivo:'), sg.Input(nome_json, size=(20,1), key='-IN_NAME_JSON-')
         ],
        [sg.Text('Dados:')],
        [sg.MLine(size=(60,20), key='-ML_DADOS-')]

    ])]

]

window = sg.Window('Meso', layout, size=(700,900))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUT_CRIAR_MACRO-':
        infos = values['-MLINE_INFO-']
        data_inicio = values['-IN_DATA_INICIO-']
        lista_semanas = [values['-IN_BASE-'], values['-IN_FORCA-'], values['-IN_SHOCK-']]
        path_micro = values['-IN_PATH_MICRO-']
        path_meso = values['-IN_PATH_MESO-']
        path_macro = values['-IN_PATH_MACRO-']

        dados_macro = criar_dados_macro(infos, data_inicio, lista_semanas, path_micro, path_meso)

        caminho_json = caminho_pasta + nome_json
        print(caminho_json)
        write_json_dados(dados_macro, caminho_json)

        window['-ML_DADOS-'].update(dados_macro)


    if event == '-BUT_PATH_FILE-':
        path_folder = sg.popup_get_folder('Choose your file', keep_on_top=True)
        window['-IN_PATH_MACRO-'].update(path_folder)


    if event == '-BUT_ABRIR_ARQ_MICRO-':
        caminho_micro_csv = sg.popup_get_file('Choose your file', keep_on_top=True)
        window['-IN_PATH_MICRO-'].update(caminho_micro_csv)

    if event == '-BUT_ABRIR_ARQ_MESO-':
        caminho_meso_csv = sg.popup_get_file('Choose your file', keep_on_top=True)
        window['-IN_PATH_MESO-'].update(caminho_meso_csv)

    if event == '-BUT_CRIAR_MICRO-':
        executar_arquivo('Micro')

    if event == '-BUT_CRIAR_MESO-':
        executar_arquivo('Meso')



window.close()
