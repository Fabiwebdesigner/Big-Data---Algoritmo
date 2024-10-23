import pandas as pd
# Importando a Base de Dados
endereco_dados = 'Base_Dados\Financeira.csv'
# Criando o DataFrame 
df_financeira = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
# Exibindo os Dados do DataFrame 
print('---- DADOS FINANCEIROS ----')
print(df_financeira.head())