dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                  'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

lista_todos_musculos = ['Peito', 'Costas', 'Ombros', 'Bíceps', 'Tríceps',
                        'Antebraço','Pernas', 'Abdômen', 'Cardio', 'Yoga']

# Lista que tera os dados do treino, primeira linha é o cabecalho
dados_treino_micro = [['Dia', 'Treino']]


# Funcao que cria uma string para inserir no multiline com o dia do treino, o treino, exercicios...
def texto_treino_mline(dia='x', treino_tx='x'):
    texto = f'Dia: {dia}\n' \
            f'Treino: {treino_tx}'

    return texto


# Funcao que recebe string do mline e retorna dia, treino e exercicios
def dados_mline(mline):
    """
    Dia: Terça-feira
    Treino: ['Peito', 'Tríceps', 'Ombros']
    Exercicios: ['Sup Inc Maq', 'Triceps Frances Halter', 'Desenvolvimento Ombro']
    """
    # Transformando minha string em uma lista de linhas
    linhas = mline.split('\n')
    print(linhas)
    # ['Dia: Terça-feira', "Treino: ['Peito', 'Tríceps', 'Ombros']", "Exercicios: ['Sup Inc Maq', 'Triceps Frances Halter', 'Desenvolvimento Ombro']"]
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


