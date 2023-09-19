import PySimpleGUI as sg
from src.controlers.control_meso import *
import csv



lista_musculos = ['Costas','Perna', 'Peito',  'Ombros', 'Bíceps', 'Tríceps',
                  'Antebraço', 'Abdômen', 'Panturilha']




def subs_linha_dado_gym_cal(values, dados, gym_cal):
    aux_exer_valor = [values['-IN_EXERC-'], values['-IN_PESO_REP-']]

    if gym_cal == 'gym':
        dados[int(values['-TABLE_ACADEMIA-'][0]) + 1] = aux_exer_valor
    elif gym_cal == 'cal':
        dados[int(values['-TABLE_CALISTENIA-'][0]) + 1] = aux_exer_valor



def write_csv_Meso(dados, caminho):
    # Abre o arquivo em omodo escrita
    with open(caminho, 'w', newline='') as arquivo_csv:
        # Variavel csv para ler arquivo
        writer = csv.writer(arquivo_csv)

        # Percode o dicionario
        for key, item in dados.items():
            # Escreve a chave
            writer.writerow([key])

            # Pecorre a lista de exercicios escrevendo linha por linha
            for linha in item:
                # Escreve cada linha da lista
                writer.writerow(linha)


def read_csv_Meso(caminho):
    with open(caminho, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)

        aux_academia_base = []
        aux_calistenia_base = []
        dados = ''

        for linha in reader:
            if len(linha) == 1:
                dados = linha[0]
            elif dados == 'Gym':
                aux_academia_base.append(linha)
            elif dados == 'Calistenia':
                aux_calistenia_base.append(linha)

        return aux_academia_base[:], aux_calistenia_base[:]


# Funcao que cria e adiciona linha na lista peso base sem [exerc, 'x']
def exercicio_nopeso(exerc, valor, peso_rep, academia_base, calistenia_base):
    if peso_rep == 'Academia':
        aux_peso_exerc = [exerc, valor]
        academia_base.append(aux_peso_exerc[:])
    elif peso_rep == 'Calistenia':
        aux_rep_exerc = [exerc, valor]
        calistenia_base.append(aux_rep_exerc[:])


def calistenia_ou_gym(values):
    if values['-R1_ACADEMIA-']:
        return 'Academia'
    elif values['-R2_CALISTENIA-']:
        return 'Calistenia'


def atualiza_tabelas(window, academia_base, calistenia_base):
    window['-TABLE_ACADEMIA-'].update(values=academia_base[1:])
    window['-TABLE_CALISTENIA-'].update(values=calistenia_base[1:])


def edit_linha(values, dados, gym_cal):
    if gym_cal == 'gym':
        linha_editar = dados[int(values['-TABLE_ACADEMIA-'][0]) + 1]
    elif gym_cal == 'cal':
        linha_editar = dados[int(values['-TABLE_CALISTENIA-'][0]) + 1]

    return linha_editar


def troca_in_dados(window, linha, gym_cal):
    if gym_cal == 'gym':
        window['-R1_ACADEMIA-'].update(True)
    elif gym_cal == 'cal':
        window['-R2_CALISTENIA-'].update(True)

    window['-IN_EXERC-'].update(linha[0])
    window['-IN_PESO_REP-'].update(linha[1])

"""
# Funcao que retorna o indice da linha que eu quero e a linha
def indice_linha(exerc):
    for linha in academia_base:
        if exerc in linha:
            indice = academia_base.index(linha)
            # Retorna o indice da lista e a linha
            return indice, linha
"""

