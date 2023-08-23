

"""
- 28/08/2023: A data da segunda feira da primeira semana de treino, o mesociclo 1 (base)
- 12: Duracao em semanas, vou dividir em 3 mesociclos, (base, forca, shock), cada mesociclo ira ter 4 semanas,
- [Supino, Agachamento...]: Lista de exercicio que irei usar para acompanhar minha evolução
- [Supino, 40]: Peso base para cada exercicio na faixa de 10 - 12 rep
- [Costas, 16]: Volume de series semanais bases para cada musculo
- [segunda, peito, supino, flexao...]: Divisao do treino semanal (segunda, terça...) Com cada musculo e os exercicios

----- Agora aqui seria a minha evolução em si de cada semana, se eu começo dia 28/08 segunda, esta é a minha Semana 1 (S1), e eu dividiria em 3, (base (S1 a S4), forca (S5 a S8) shock (S9 a S12)) pois cada uma dessas fases tem uma media de repeticao e volume semanal diferente entao ficaria assim----

- [[Exercicio, S1, S2, S3, S4,], [Supino, 30, 32, 32, 35]...] :  Esta seria os dados do mesociclo de base com todos os exercicios que eu usarei para acompanhar a minha evolução

--------------- Funcoes que tenho que fazer -----------

data inicio
semanas
lista_exercicios_acompanhar
peso_base
volume_semanal_base
divisao treino (sem exercicios)

base :
[exercicio, s1,s2,s3,s4]
forca:

shock:

"""


def dic_dados_macro(data_inicio, total_semanas, exercicios, peso_base_exercicios, musc_vol_seman_base,
                    divisao_treino, base, forca, shock):
    dados_macro = dict()

    dados_macro['data_inicio'] = data_inicio
    dados_macro['total_semanas'] = total_semanas
    dados_macro['exercicios'] = exercicios
    dados_macro['peso_base'] = peso_base_exercicios
    dados_macro['volume_semanal_base'] = musc_vol_seman_base
    dados_macro['divisao_treino'] = divisao_treino
    dados_macro['base'] = base
    dados_macro['forca'] = forca
    dados_macro['shock'] = shock

    return dados_macro



