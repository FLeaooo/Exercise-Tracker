import PySimpleGUI as sg

layout = [
    [sg.Text('Texto à esquerda'), sg.Column(layout=[[sg.VSeperator()]], element_justification='center'), sg.Text('Texto à direita')]
]

window = sg.Window('Exemplo de Linha Vertical', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()