import PySimpleGUI as sg

caminho_micro_csv = ''
caminho_meso_csv = ''

lista_musculos = ['Peito', 'Costas', 'Ombros', 'Bíceps', 'Tríceps',
                  'Antebraço','Quadriceps', 'Posterior','Abdômen', 'Panturilha']

volume_base = [['Musculo', 'Volume']]

peso_base = [['Exercicio', 'Peso (10-12Rep)']]

lista_exercicios_acompanhar = []

meso_base = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]
meso_forca = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]
meso_shock = [['Exercicio', 'S1', 'S2', 'S3', 'S4']]

layout = [


    [sg.Frame('MicroCiclo, treino Semanal',[
        [sg.Text('Para criar planejamento de treino (MacroCiclo) é necessario ter o treino semanal (MicroCiclo):')],
        [sg.Button('Abrir arquivo MicroCiclo',expand_x=True), sg.Button('Criar treino e arquivo MicroCiclo',expand_x=True)],
        [sg.Text('Caminho CSV (treino semanal):'), sg.Input(caminho_micro_csv, size=(40,1))],
        [sg.Button('Editar/Ver treino')]
    ])],

    [sg.Frame('MesoCiclo, planejamento mes a mes', [
        [sg.Text('Para criar planejamento de treino (MacroCiclo) é necessario ter o planejamento de cada mes (MesoCiclo):')],
        [sg.Button('Abrir arquivo MesoCiclo', expand_x=True),
         sg.Button('Criar arquivo MesoCiclo', expand_x=True)],
        [sg.Text('Caminho CSV (treino semanal):'), sg.Input(caminho_meso_csv, size=(40,1))],
        [sg.Button('Editar/Ver planejamento')]
    ])],

    [sg.Frame('Informações para o MacroCiclo', [
        [sg.Text('Data de inico, primeira semana, segunda:'), sg.Input(size=(20,1), key='-IN_DATA_INICIO-'),
         sg.CalendarButton('Calendario', target='-IN_DATA_INICIO-', format='%d/%m/%Y')],
        [sg.Text('Semanas Mesociclo Base:  '), sg.Input('4', size=(3,1), key='-IN_BASE-')],
        [sg.Text('Semanas Mesociclo Forca: '), sg.Input('4', size=(3,1), key='-IN_FORCA-')],
        [sg.Text('Semanas Mesociclo Shock:'), sg.Input('4', size=(3,1), key='-IN_SHOCK-')],
        [sg.Button('Confirmar', key='-INFO_MACRO-')]
    ], expand_x=True)],


    [sg.Frame('Acompanhamento semanal',[
        [sg.Table(headings=meso_base[0], values=meso_base[1:]), sg.Table(headings=meso_forca[0], values=meso_forca[1:]),
         sg.Table(headings=meso_shock[0], values=meso_shock[1:])]
    ])],

    [sg.Frame('Divisao e datas', [
        [sg.Input(size=(20,1)), sg.Button('Selecione data de inicio')],


    ])],
]

window = sg.Window('Meso', layout, size=(700,900))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-INFO_MACRO-':
        pass

window.close()
