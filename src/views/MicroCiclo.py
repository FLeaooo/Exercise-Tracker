from src.controlers.control_micro import *
from src.models.model_micro import *


def criar_janela_microciclo():
    layout = [
        [sg.Text('Criar MicroCiclo (Treino Semana)', font='_ 18', justification='center', expand_x=True,
                 relief=sg.RELIEF_RIDGE)],

        [sg.OptionMenu(values=dias_da_semana, key='-OPTION_DIA_SEMANA-'),
         sg.Combo(values=lista_todos_musculos, key='-COMBO_MUSCULOS-'),
         sg.Button('Adicionar Musculo', key='-ADD_MUSC-')],

        [sg.Button('Adicionar Treino', key='-ADD_TREINO-'),
         sg.Button('Substituir treino', key='-SUB_TREINO-'),
         sg.Button('Editar treino', key='-EDIT_TREINO-'),
         sg.Button('Deletar treino', key='-DEL_TREINO-')],

        [sg.MLine(texto_atualizado_treino, no_scrollbar=True, size=(70, 2), key='-MLINE-')],

        [sg.Table(headings=dados_treino_micro[0], values=dados_treino_micro[1:], key='-TABLE_TREINOS-', expand_x=True)],

        [sg.Text('Caminho do arquivo CSV'), sg.Input(path_micro,
                                                     key='-INPUT_FILE_PATH-', size=(50, 1)),
         sg.Button('Escolher', expand_x=True, key='-TROCAR_PATH_CSV-')],

        [sg.Button('Inserir dados MicroCiclo no Arquivo', key='-INSERIR_DADOS-'),
         sg.Button('Copiar dados do arquivo CSV', key='-COPIAR_DADOS-')]

    ]

    window = sg.Window('Criar Treino/MicroCiclo', layout, size=(600, 500))

    return window


def main():
    global dados_treino_micro, path_micro, texto_atualizado_treino

    window = criar_janela_microciclo()

    linha_treino = []
    lista_musculo = []

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        dia_semana = values['-OPTION_DIA_SEMANA-']
        path_micro = values['-INPUT_FILE_PATH-']


        # Botao que adiciona na lista o musculo selecionado
        if event == '-ADD_MUSC-':
            lista_musculo.append(values['-COMBO_MUSCULOS-'])

        # Botao que cria lista de treino com os dados e adiciona a lista de dados
        if event == '-ADD_TREINO-':
            add_treino_dados(lista_musculo, values, dados_treino_micro)
            atualiza_tabela(dados_treino_micro, window)


        # Abri uma janela para escolher novo caminho
        if event == '-TROCAR_PATH_CSV-':
            trocar_caminho(window)

        # Botao que inseri os dados no arquivo csv
        if event == '-INSERIR_DADOS-':
            inserir_dados_csv_json(dados_treino_micro, path_micro)

        # Botao que copia os dados para a janela do arquivo csv
        if event == '-COPIAR_DADOS-':
            dados_treino_micro = copiar_dados_arq_csv(path_micro)
            atualiza_tabela(dados_treino_micro, window)

        # Botao que pega a linha selecionada e edita ela
        if event == '-EDIT_TREINO-':
            dia_semana = editar_linha(window, values, dados_treino_micro, lista_musculo)
            texto_atualizado_treino = texto_treino_mline(dia=dia_semana, treino_tx=lista_musculo)
            window['-MLINE-'].update(texto_atualizado_treino)

        # Botao substituir treino, apaga o selecionado e inseri o novo ali (editar)
        if event == '-SUB_TREINO-':
            substituir_linha(values, dados_treino_micro, lista_musculo)
            atualiza_tabela(dados_treino_micro, window)

        if event == '-DEL_TREINO-':
            deletar_linha(values, dados_treino_micro)
            atualiza_tabela(dados_treino_micro, window)

        # Atualiza a linha na janela com o texto
        texto_atualizado_treino = texto_treino_mline(dia=dia_semana, treino_tx=lista_musculo)
        window['-MLINE-'].update(texto_atualizado_treino)

    window.close()


if __name__ == '__main__':
    main()