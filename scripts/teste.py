import csv
import json

data = [['Dia', 'Treino', 'Exercicio'],
        ['Segunda-feira', ['Pernas', 'Abdômen'], ['Agachamento']],
        ['Terça-feira', ['Peito', 'Tríceps', 'Ombros'], ['Sup Inc Maq', 'Paralela', 'Desenvolvimento Maq']],
        ['Quarta-feira', ['Costas', 'Bíceps'], ['Pullet Frente Neutra', 'Meio Terra', 'Biceps Rosca Scoot W']],
        ['Quinta-feira', ['Pernas', 'Ombros'], ['Agachamento', 'Desenvolvimento']],
        ['Sexta-feira', ['Bíceps', 'Tríceps', 'Antebraço'], ['Biceps Rosca', 'Frances Halter', 'Antebraco Polia']]]

with open('C:/FernandoLeao/Exercicios/dados_treino_macro.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow([row[0], json.dumps(row[1]), json.dumps(row[2])])



with open('C:/FernandoLeao/Exercicios/dados_treino_macro.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    data = []
    for row in csvreader:
        dia = row[0]
        treino = json.loads(row[1])
        exercicio = json.loads(row[2])
        data.append([dia, treino, exercicio])

    print(data)
