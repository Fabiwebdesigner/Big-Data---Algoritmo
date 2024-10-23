# População Vacinada: 30000000, 25000000, 10000000, 5000000
# População Total: 213317639, 214477744, 215574303, 216687971
# O total e a média de pessoas vacinadas no período.
# O total e a média da população do Brasil.
# A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a 
# de vacinados pela quantidade da população.
# quantidade de vacinados pela quantidade da população.

import pandas as pd
# Dados fornecidos
dados = {
    'Ano': [2021, 2022, 2023, 2024],
    'Populacao_Vacinada': [30000000, 25000000, 10000000, 5000000],
    'Populacao_Total': [213317639, 214477744, 215574303, 216687971]
}
df = pd.DataFrame(dados)
# Cálculos
total_vacinados = df['Populacao_Vacinada'].sum()
media_vacinados = df['Populacao_Vacinada'].mean()

total_populacao = df['Populacao_Total'].sum()
media_populacao = df['Populacao_Total'].mean()

# Calcular taxa de vacinação anual
df['Taxa_Vacinacao'] = df['Populacao_Vacinada'] / df['Populacao_Total']

# Resultados
print(f"Total de pessoas vacinadas: {total_vacinados}")
print(f"Média de pessoas vacinadas: {media_vacinados:.2f}")
print(f"Total da população do Brasil: {total_populacao}")
print(f"Média da população do Brasil: {media_populacao:.2f}")
print("\nTaxa de vacinação anual (em porcentagem):")
for ano, taxa in zip(df['Ano'], df['Taxa_Vacinacao']):
    print(f"Ano {ano}: {taxa * 100:.2f}%")
