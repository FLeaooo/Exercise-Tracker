from src.models.model_meso import *
from src.controlers.control_meso import *

file_csv_Meso = 'C:/FernandoLeao/Exercicios/meus/MesoCiclo.csv'


def criar_window_meso(academia_base, calistenia_base, file_csv_Meso):
    layout = [
        [sg.Text('Peso base de cada exercicio', font='_ 18', justification='center', expand_x=True,
                     relief=sg.RELIEF_RIDGE)],


        [sg.Frame('Exercicios para acompanhar evolucao', [
            [sg.Radio('Academia', "TipoExercicio", default=True, size=(10, 1), k='-R1_ACADEMIA-'),
             sg.Radio('Calistenia', "TipoExercicio", default=False, size=(10, 1), k='-R2_CALISTENIA-')],

            [sg.Text('Insira o exercicio:'),
             sg.Input(size=(40, 1), key='-IN_EXERC-')],

            [sg.Text('Peso (10 - 12 rep) ou Rep (peso corporal):'),
             sg.Input(size=(20, 1), key='-IN_PESO_REP-')],

            [sg.Button('Inserir', size=(40, 1), key='-BUT_INSERT-')],

        ], expand_x=True)],

        [sg.Frame('Tabela Academia', [
            [sg.Table(headings=academia_base[0], values=academia_base[1:], key='-TABLE_ACADEMIA-')],

            [sg.Button('Editar', expand_x=True, key='-BUT_EDIT_GYM-'),
             sg.Button('Substituir', expand_x=True, key='-BUT_SUB_GYM-'),
             sg.Button('Deletar', expand_x=True, key='-BUT_DEL_GYM-')],

        ]),
         sg.Frame('Tabela Calistenia', [

             [sg.Table(headings=calistenia_base[0], values=calistenia_base[1:], key='-TABLE_CALISTENIA-')],

             [sg.Button('Editar', expand_x=True, key='-BUT_EDIT_CAL-'),
              sg.Button('Substituir', expand_x=True, key='-BUT_SUB_CAL-'),
              sg.Button('Deletar', expand_x=True, key='-BUT_DEL_CAL-')],
         ])],

        [sg.Text('Camiho arq CSV: '), sg.Input(file_csv_Meso, size=(50,1), key='-IN_FILE_CSV-'),
         sg.Button('Escolher', key='-BUT_FILE-')],

        [sg.Button('Inserir dados MesoCiclo no Arquivo', key='-BUT_INSERT_DATA-'),
         sg.Button('Copiar dados do arquivo CSV', key='-BUT_COPY_DATA-')]

    ]


    window = sg.Window('Meso', layout, size=(700, 500))

    return window


def main():
    global file_csv_Meso

    academia_base = [['Exercicio', 'Kg (10-12Rep)']]
    calistenia_base = [['Exercicio', 'Reps (Calistenia)']]

    dic_gym_calist_base = {'Gym': academia_base, 'Calistenia': calistenia_base}

    window = criar_window_meso(academia_base, calistenia_base, file_csv_Meso)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        # Botao que adiciona o exercicio a lista e atualiza a tabela sem o peso
        if event == '-BUT_INSERT-':
            # funcao que retorna um dos dois ('Academia', 'Calistenia')
            calist_ou_gym = calistenia_ou_gym(values)

            # Atualiza a lista peso_base com o [exerc, 'x']
            exercicio_nopeso(values['-IN_EXERC-'], values['-IN_PESO_REP-'],calist_ou_gym, academia_base, calistenia_base)

            # Atualiza a tabela com a lista atualizada de peso_base
            atualiza_tabelas(window, academia_base, calistenia_base)

        if event == '-BUT_FILE-':
            # Abre nova janela e seleciona o arquivo
            file_csv_Meso = sg.popup_get_file('Choose your file', keep_on_top=True)
            # Troca o caminho do input
            window['-IN_FILE_CSV-'].update(file_csv_Meso)

        if event == '-BUT_INSERT_DATA-':
            dic_gym_calist_base = {'Gym': academia_base, 'Calistenia': calistenia_base}
            write_csv_Meso(dic_gym_calist_base, file_csv_Meso)

        if event == '-BUT_COPY_DATA-':
            academia_base, calistenia_base = read_csv_Meso(file_csv_Meso)
            print(calistenia_base)
            print(academia_base)
            atualiza_tabelas(window, academia_base, calistenia_base)

        ################### BOTOES EDITAR, SUB, DEL ############################
        if event == '-BUT_EDIT_GYM-':
            linha_editar = edit_linha(values, academia_base, 'gym')
            troca_in_dados(window, linha_editar, 'gym')

        if event == '-BUT_SUB_GYM-':
            subs_linha_dado_gym_cal(values, academia_base, 'gym')
            atualiza_tabelas(window, academia_base, calistenia_base)

        if event == '-BUT_DEL_GYM-':
            del academia_base[int(values['-TABLE_ACADEMIA-'][0]) + 1]
            atualiza_tabelas(window, academia_base, calistenia_base)

        # Botoes calistenia
        if event == '-BUT_EDIT_CAL-':
            linha_editar = edit_linha(values, calistenia_base, 'cal')
            troca_in_dados(window, linha_editar, 'cal')

        if event == '-BUT_SUB_CAL-':
            subs_linha_dado_gym_cal(values, calistenia_base, 'cal')
            atualiza_tabelas(window, academia_base, calistenia_base)

        if event == '-BUT_DEL_CAL-':
            del calistenia_base[int(values['-TABLE_CALISTENIA-'][0]) + 1]
            atualiza_tabelas(window, academia_base, calistenia_base)

    window.close()


if __name__ == '__main__':
    main()
