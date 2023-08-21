import matplotlib.pyplot as plt
import datetime

# Sua lista de dados
dados = [['Data', 'Exercicio', 'Peso', 'Repeticoes'],
         ['05/06/2023', 'Sup Inc Maq', '20', '11'],
         ['29/06/2023', 'Sup Inc Maq', '20', '4'],
         ['04/07/2023', 'Sup Inc Maq', '20', '10'],
         ['10/07/2023', 'Sup Inc Maq', '25', '8'],
         ['10/07/2023', 'Sup Inc Maq', '30', '3'],
         ['13/07/2023', 'Sup Inc Maq', '30', '5'],
         ['29/07/2023', 'Sup Inc Maq', '30', '9'],
         ['01/08/2023', 'Sup Inc Maq', '35', '7'],
         ['08/08/2023', 'Sup Inc Maq', '35', '7']]


# Lista dos pesos e das repeticoes
pesos = [int(row[2]) for row in dados[1:]]
datas = [row[0] for row in dados[1:]]

# Transformar minhas datas em numero da semana
numero_semana_list = []
for data in datas:
    data_objeto = datetime.datetime.strptime(data, '%d/%m/%Y')
    num_semana = data_objeto.isocalendar()[1]
    numero_semana_list.append(num_semana)

# Grafico de dispersao
plt.figure(figsize=(10,6))  # tamanho da figura

# adiciona pontos ao grafioc
plt.bar(numero_semana_list, pesos, color='blue', label='Dados')

# rotulo aos eixos
plt.xlabel('Semana')
plt.ylabel('Peso')

# Titulo ao grafico
plt.title('Relacao entre Peso e Repeticoes')

plt.xticks(numero_semana_list)
plt.grid(axis='y')

# Legenda
plt.legend()

plt.show()