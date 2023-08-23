import PySimpleGUI as sg

from src.controlers.criar_micro import *
from src.models.Dados_Exercise import *

# Cria a variavel do texto da multiline
texto_atualizado_treino = texto_treino_mline()


def criar_janela_microciclo():
    layout = [
        [sg.Text('Criar MicroCiclo (Treino Semana)', font='_ 18', justification='center', expand_x=True,
                 relief=sg.RELIEF_RIDGE)],

        [sg.OptionMenu(values=dias_da_semana, key='-OPTION_DIA_SEMANA-'),
         sg.Combo(values=lista_todos_musculos, key='-COMBO_MUSCULOS-'),
         sg.Button('Adicionar Musculo', key='-ADD_MUSC-')],

        [sg.Text('Não é necessario inserir todos os exercicios que ira fazer no treino.\n'
                 'Apenas os principais que voce ira usar para acompanhar a sua evolução de força.')],


        [sg.Button('Adicionar Treino', key='-ADD_TREINO-'),
         sg.Button('Substituir treino', key='-SUB_TREINO-'),
         sg.Button('Editar treino', key='-EDIT_TREINO-'),
         sg.Button('Deletar treino', key='-DEL_TREINO-')],

        [sg.MLine(texto_atualizado_treino, no_scrollbar=True, size=(70, 2), key='-MLINE-')],


        [sg.Table(headings=dados_treino_micro[0], values=dados_treino_micro[1:], key='-TABLE_TREINOS-', expand_x=True)],

        [sg.Text('Caminho do arquivo CSV'), sg.Input('C:/FernandoLeao/Exercicios/dados_treino_macro.csv',
                                                     key='-INPUT_FILE_PATH-', size=(50,1)),
         sg.Button('Escolher', expand_x=True, key='-TROCAR_PATH_CSV-')],

        [sg.Button('Inserir dados MicroCiclo no Arquivo', key='-INSERIR_DADOS-'),
         sg.Button('Copiar dados do arquivo CSV', key='-COPIAR_DADOS-')]

    ]

    window = sg.Window('Criar Treino/MicroCiclo', layout, size=(600, 500))

    return window


dia_semana = ''


def main():
    global dados_treino_micro
    window = criar_janela_microciclo()

    linha_treino = []
    lista_musculo = []


    while True:
        event, values = window.read()
        dia_semana = values['-OPTION_DIA_SEMANA-']
        folder_or_file = values['-INPUT_FILE_PATH-']

        if event == sg.WIN_CLOSED:
            break

        # Botao que adiciona na lista o musculo selecionado
        if event == '-ADD_MUSC-':
            lista_musculo.append(values['-COMBO_MUSCULOS-'])


        # Botao que cria lista de treino com os dados e adiciona a lista de dados
        if event == '-ADD_TREINO-':

            # Adiciona o dia a lista treino
            linha_treino.append(values['-OPTION_DIA_SEMANA-'])
            # Adiciona a lista dos musculos a treinar na lista treino
            linha_treino.append(lista_musculo[:])

            # Adiciona a lista treino a lista de dados
            dados_treino_micro.append(linha_treino[:])

            # Limpa os dados da lista treino,texto,musculo,exercicios
            linha_treino.clear()
            lista_musculo.clear()

            # Atualiza a tabela
            window['-TABLE_TREINOS-'].update(values=dados_treino_micro[1:])

        # Abri uma janela para escolher novo caminho
        if event == '-TROCAR_PATH_CSV-':
            # Abre nova janela e seleciona o arquivo e troca o caminho do input
            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            window['-INPUT_FILE_PATH-'].update(folder_or_file)
            print(folder_or_file)

        # Botao que inseri os dados no arquivo csv
        if event == '-INSERIR_DADOS-':
            inserir_dados_csv_json(dados_treino_micro, folder_or_file)

        # Botao que copia os dados para a janela do arquivo csv
        if event == '-COPIAR_DADOS-':
            dados_treino_micro = copiar_dados_arq_csv(folder_or_file)
            window['-TABLE_TREINOS-'].update(values=dados_treino_micro[1:])

        # Botao que pega a linha selecionada e edita ela
        if event == '-EDIT_TREINO-':
            # Recebe a linha que selecionou na tabela
            linha_editar_dados = dados_treino_micro[int(values['-TABLE_TREINOS-'][0]) + 1]
            # Atualiza o dia da semana de option com base na linha selecionada
            window['-OPTION_DIA_SEMANA-'].update(linha_editar_dados[0])

            # Recebe o dia, musculos, exercicios
            dia_semana = linha_editar_dados[0]
            lista_musculo = linha_editar_dados[1]

            # Cria a string da linhha que vai editar e adiciona na multiline
            texto_editar = texto_treino_mline(linha_editar_dados[0], lista_musculo)
            window['-MLINE-'].update(texto_editar)


        # Botao substituir treino, apaga o selecionado e inseri o novo ali (editar)
        if event == '-SUB_TREINO-':
            # Recebe a posicao que ira editar dos dados na tabela
            pos_editar = int(values['-TABLE_TREINOS-'][0]) + 1
            # Deleta a linha que ira substituir
            del dados_treino_micro[pos_editar]

            # Funcao que pega a string MLINE e retorna os dados
            dia_mline, l_treino_mline = dados_mline(values['-MLINE-'])

            # Adiciona os dados na lista treino
            linha_treino.append(dia_mline)
            linha_treino.append(l_treino_mline[:])

            # Inseri o treino na posicao que o treino antigo estava e atualiza a tabela
            dados_treino_micro.insert(pos_editar, linha_treino[:])

            linha_treino.clear()
            lista_musculo.clear()

            window['-TABLE_TREINOS-'].update(values=dados_treino_micro[1:])

        if event == '-DEL_TREINO-':
            # Recebe a posicao que ira deletar
            pos_editar = int(values['-TABLE_TREINOS-'][0]) + 1
            # Deleta a linha
            del dados_treino_micro[pos_editar]
            # Atualiza a tabela agora com ela deletada
            window['-TABLE_TREINOS-'].update(values=dados_treino_micro[1:])


        # Atualiza a linha na janela com o texto
        texto_atualizado_treino = texto_treino_mline(dia=dia_semana, treino_tx=lista_musculo)
        window['-MLINE-'].update(texto_atualizado_treino)

    window.close()


if __name__ == '__main__':
    main()

