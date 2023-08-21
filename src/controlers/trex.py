from datetime import datetime


# Funcao que retorna a data de hoje em string
def data_hoje():
    hoje = datetime.now()
    data_hj = hoje.strftime("%d/%m/%Y")
    return data_hj


# Funcao que retorna a string para o cabecalho do aplicativo
def str_cabecalho_hj(data_str):
    str_dia_semana_hj = str_data_dia_treino(data_str)

    # Cria uma string para ter de cabeçalho no programa
    cabecalho = f'{data_str} - {str_dia_semana_hj}'

    return cabecalho


# Retorna em string o dia da semana (segunda, terca....)
def str_data_dia_treino(data_str):
    # Transformando minha data em um datetime
    data_datatime = datetime.strptime(data_str, "%d/%m/%Y")

    # Recebe dia da semana em numero
    dia_semana = data_datatime.weekday()

    # Lista com os dias da semana para eu ter a string
    dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
                      "Sexta-feira", "Sábado", "Domingo"]

    # Pega a string do dia da semana com base na lista 1 = Terça
    str_dia_semana = dias_da_semana[dia_semana]

    return str_dia_semana







