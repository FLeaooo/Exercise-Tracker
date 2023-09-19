import PySimpleGUI as sg


# Funcao que cria uma string para inserir no multiline com o dia do treino, o treino, exercicios...
def texto_treino_mline(dia='x', treino_tx='x'):
    texto = f'Dia: {dia}\n' \
            f'Treino: {treino_tx}'

    return texto


def trocar_caminho(window):
    global path_micro
    # Abre nova janela e seleciona o arquivo e troca o caminho do input
    path_micro = sg.popup_get_file('Choose your file', keep_on_top=True)
    window['-INPUT_FILE_PATH-'].update(path_micro)


def atualiza_tabela(dados, window):
    # Atualiza a tabela
    window['-TABLE_TREINOS-'].update(values=dados[1:])


def editar_linha(window, values, dados, lista_musculo):
    # Recebe a linha que selecionou na tabela
    linha_editar_dados = dados[int(values['-TABLE_TREINOS-'][0]) + 1]

    # Atualiza o dia da semana de option com base na linha selecionada
    window['-OPTION_DIA_SEMANA-'].update(linha_editar_dados[0])

    # Recebe o musculos
    lista_musculo.clear()
    lista_musculo.extend(linha_editar_dados[1])

    return linha_editar_dados[0]
