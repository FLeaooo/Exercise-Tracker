import PySimpleGUI as sg

lista_musculos = ['Peito', 'Costas', 'Ombros', 'Bíceps', 'Tríceps',
                  'Antebraço','Quadriceps', 'Posterior','Abdômen', 'Panturilha']

volume_base = [['Musculo', 'Volume']]

peso_base = [['Exercicio', 'Peso (10-12Rep)']]

lista_exercicios_acompanhar = []


layout = [
    [sg.Text('Receber o volume base semanal e o peso base de cada exercicio')],

    [sg.Frame('Volume de base series semana', [
        [sg.Combo(values=lista_musculos, size=(30, 1)), sg.Input(size=(6, 1)), sg.Button('Inserir', expand_x=True)],
        [sg.Table(headings=volume_base[0], values=volume_base[1:], expand_x=True)]
    ], expand_x=True)],

    [sg.Frame('Exercicios para acompanhar evolucao', [
        [sg.Input(size=(40,1)), sg.Button('Inserir', expand_x=True)]
    ], expand_x=True )],

    [sg.Frame('Peso base, para os exercicios', [
        [sg.Combo(values=lista_exercicios_acompanhar, size=(30, 1)), sg.Input(size=(6, 1)),
         sg.Button('Inserir', expand_x=True)],
        [sg.Table(headings=peso_base[0], values=peso_base[1:], expand_x=True)],

    ], expand_x=True)],
]

window = sg.Window('Meso', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()
