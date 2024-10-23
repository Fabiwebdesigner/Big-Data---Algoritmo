import pandas as pd

# Dados fornecidos
vendas_maria = pd.Series([800, 700, 1000, 900, 1200, 600, 600], index=["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"])
vendas_joao = pd.Series([900, 500, 1100, 1000, 900, 500, 700], index=["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"])
vendas_manuel = pd.Series([700, 600, 900, 1200, 900, 700, 400], index=["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"])

# Função para calcular os dados de interesse
def calcular_dados_vendas(vendas):
    media_vendas = vendas.mean()
    maior_venda = vendas.max()
    menor_venda = vendas.min()
    return round(media_vendas, 2), maior_venda, menor_venda

# Calculando para cada vendedor/a
vendedores = {'Maria': vendas_maria, 'João': vendas_joao, 'Manuel': vendas_manuel}

for vendedor, vendas in vendedores.items():
    media, maior, menor = calcular_dados_vendas(vendas)
    print(f"Vendedor/a: {vendedor}")
    print(f"Média de vendas: {media:.2f}")
    print(f"Maior valor vendido: {maior}")
    print(f"Menor valor vendido: {menor}")
    print("-" * 30)
