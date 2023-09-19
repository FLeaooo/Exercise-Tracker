import copy
import csv
import json

from src.models.model_micro import *
from src.models.model_meso import *
from src.views.MesoCiclo import file_csv_Meso


path_macro = r'C:\FernandoLeao\Exercicios\teste_macro2.json'
path_macro_ler = r'C:\FernandoLeao\Exercicios\teste_macroo.json'

lis_cal = [['Exercicio', 'Reps (Calistenia)'], ['Barra Fixa', '4'], ['Paralela', '3'], ['Flexao', '10']]
lista_gym = [['Exercicio', 'Kg (10-12Rep)'], ['Sup Inc Maq', '30'], ['Meio Terra', '15'], ['Agachamento', '20']]


# Gera uma lista para acompanhar os exercicios da calistenia
def gerar_dados_acompanhar_macro_calistenia(lista_semanas, exerc_cal):

    # Deleta a primeira linha da lista que é [exercicio, rep] parra adicionar outra com a pos (0 semana)
    del exerc_cal[0]
    lis_calistenia = [['Semana', 'Exercicio', 'Reps']]

    # Saber o total de semanas
    total_semanas = sum(int(x) for x in lista_semanas)

    # Loop que vai de 0 ate 13
    for i in range(total_semanas + 1):
        # Loop que passa nos exercicios da lista (barra fix, paralela...)
        for exerc in exerc_cal:
            aux_treino = exerc[:]
            aux_treino.insert(0, i)

            if i != 0:
                aux_treino[2] = 'x'

            lis_calistenia.append(aux_treino[:])
            # Adiciona na lista a semana e o exercicio e as rep
            # [0, 'Barra Fixa', '4'], [1, 'Barra Fixa', 'x']....

    return lis_calistenia


# Gera um dicionario para acompanhar exercicios da academia (Referencia: [] Base: [] Forca: [] Shock: [])
def gerar_dados_acompanhar_macro_gym(lista_semanas, exerc_gym):
    # Fazendo receber quantidade de semanas
    base, forca, shock = lista_semanas[0], lista_semanas[1], lista_semanas[2]

    # Recebe ate qual semana é Ex: (4,8,12)
    ate_base = int(base)
    ate_forca = int(forca) + int(base)
    ate_shock = int(shock) + ate_forca

    # Deleta a primeira linha que é o cabecalho sem as semanas
    del exerc_gym[0]

    # Nova lista para armazenar os dados de referencia dos exercicios
    referencia = []

    # Percorre a lista inserindo os valores do exercicio mais a semana 0
    # [['0', 'Sup Inc Maq', '30'], ['0', 'Meio Terra', '15'], ['0', 'Agachamento', '20']]
    for linha in exerc_gym:
        linha.insert(0, 0)
        referencia.append(linha)


    # Cria o dicionario que sera retornado
    dic_academia = {'Referencia': referencia, 'Base': [], 'Forca': [], 'Shock': []}

    # Cria funcao que gera a lista de treino da semana sem o peso
    def gera_lista(start, stop, referencia):
        dados_base = []
        # Loop que vai da semana que começa ate parar
        for semana in range(start, stop + 1):
            # Copia a lista de referenci
            aux_referencia_copy = copy.deepcopy(referencia)

            # Loop que passa por cada exercicio da lista
            for treino_aux in aux_referencia_copy:
                # Inseri a semana e o x no peso
                treino_aux[0] = semana
                treino_aux[2] = 'x'
                # Adiciona a lista de dados
                dados_base.append(treino_aux[:])
                # ['1', 'Sup Inc Maq', 'x'], ['1', 'Meio Terra', 'x'], ['1', 'Agachamento', 'x'].....

        return dados_base

    # Cria lista de cada fase da periodização
    data_base = gera_lista(1, ate_base, referencia)
    data_forca = gera_lista(ate_base, ate_forca, referencia)
    data_shock = gera_lista(ate_forca, ate_shock, referencia)

    # Inseri no dicionario
    dic_academia['Base'] = data_base
    dic_academia['Forca'] = data_forca
    dic_academia['Shock'] = data_shock

    return dic_academia



"""
{
    Informacoes: ""
    Data_inicio: ""
    Semanas: [3,3,3]
    MicroCiclo: [treino]
    MesoCiclo: [[gym],[calistenia]]
    dados_calistenia: [[]]
    dados_gym: {
        referencia: []
        base : []
        forca: []
        shock: []
        }
}
"""
def criar_dados_macro(str_info, data_inicio, lista_semanas, path_micro_ciclo, path_meso_ciclo):

    micro_ciclo = copiar_dados_arq_csv(path_micro_ciclo)

    academia_base, calistenia_base = read_csv_Meso(path_meso_ciclo)
    meso_ciclo = [academia_base, calistenia_base]

    dados_macro = {
        'Informacoes': str_info,
        'Data_Inicio': data_inicio,
        'Semanas': lista_semanas,
        'Micro_Ciclo': micro_ciclo,
        'Meso_Ciclo': meso_ciclo,
        'Dados_Calistenia': gerar_dados_acompanhar_macro_calistenia(lista_semanas, meso_ciclo[0]),
        'Dados_Gym': gerar_dados_acompanhar_macro_gym(lista_semanas, meso_ciclo[1])
    }

    return dados_macro


def inserir_CSV_dados_macro(dados_macro):
    with open(path_macro, 'w') as arquivo:
        json.dump(dados_macro, arquivo, ensure_ascii=False)



def ler_CSV_dados_macro():

    with open(path_macro_ler, 'r') as arquivo_ler:
        dados_macro_lido = json.load(arquivo_ler)

    return dados_macro_lido


def write_json_dados(dados, caminho):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo)






