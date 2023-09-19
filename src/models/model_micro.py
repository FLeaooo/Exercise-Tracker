from src.controlers.control_micro import texto_treino_mline
import json
import csv

dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                  'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

lista_todos_musculos = ['Upper Body', 'Peito', 'Costas', 'Ombros', 'Bíceps', 'Tríceps',
                        'Antebraço','Pernas', 'Abdômen', 'Cardio', 'Yoga']

# Cria a variavel do texto da multiline
texto_atualizado_treino = texto_treino_mline()
dados_treino_micro = [['Dia', 'Treino']]

path_micro = 'C:\FernandoLeao\Exercicios\meus\MicroCiclo.csv'


########## USANDO JSON MICROCICLO  ##################
def inserir_dados_csv_json(dados, caminho):
    with open(caminho, 'w', newline='') as arquivo_csv:
        csvwriter = csv.writer(arquivo_csv)
        for row in dados:
            csvwriter.writerow([row[0], json.dumps(row[1])])


# Funcao que copia os dados do arquivo csv e retorna a lista dos dados
def copiar_dados_arq_csv(caminho):
    with open(caminho, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        data = []
        for row in csvreader:
            dia = row[0]
            treino = json.loads(row[1])
            data.append([dia, treino])

    return data


def add_treino_dados(lista_musculo, values, dados):
    # Adiciona o dia e a lista de musculos
    linha_treino = [values['-OPTION_DIA_SEMANA-'], lista_musculo[:]]

    # Adiciona a lista treino a lista de dados
    dados.append(linha_treino[:])

    # Limpa os dados da lista musculo
    lista_musculo.clear()


def deletar_linha(values, dados):
    # Recebe a posicao que ira editar dos dados na tabela
    pos_editar = int(values['-TABLE_TREINOS-'][0]) + 1

    # Deleta a linha que ira substituir
    del dados[pos_editar]


def substituir_linha(values, dados, lista_musculo):
    linha_treino = [values['-OPTION_DIA_SEMANA-'], lista_musculo[:]]

    deletar_linha(values, dados)

    # Funcao que pega a string MLINE e retorna os dados
    dia_mline, l_treino_mline = dados_mline(values['-MLINE-'])

    # Adiciona os dados na lista treino
    linha_treino.append(dia_mline)
    linha_treino.append(l_treino_mline[:])

    pos_editar = int(values['-TABLE_TREINOS-'][0]) + 1
    # Inseri o treino na posicao que o treino antigo estava e atualiza a tabela
    dados.insert(pos_editar, linha_treino[:])

    linha_treino.clear()
    lista_musculo.clear()


# Funcao que recebe string do mline e retorna dia, treino
def dados_mline(mline):
    """
    Dia: Terça-feira
    Treino: ['Peito', 'Tríceps', 'Ombros']
    """
    # Transformando minha string em uma lista de linhas
    linhas = mline.split('\n')

    # ['Dia: Terça-feira', "Treino: ['Peito', 'Tríceps', 'Ombros']"]

    dia = ''
    treino = []

    # Percorre cada linha em linhas
    for linha in linhas:
        # .starswith (se começar com)
        if linha.startswith('Dia:'):
            # Replace remove a palavra
            dia = linha.replace('Dia: ', '')
        elif linha.startswith('Treino:'):
            treino = eval(linha.replace('Treino: ', ''))

    return dia, treino