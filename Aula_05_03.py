import pandas as pd

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n----Obtendo dados gerais sobre ocorrências ----')
print(df_ocorrencias.head())

# Criando o DataFrame Roubo de veículos por Município
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
print('\n----Obtendo dados sobre roubo de veículos ----')
print(df_roubo_veiculo.head())

# Criando o DataFrame Homicídio Doloso por ano 
df_ano_hommicidio_doloso = df_ocorrencias[['ano','hom_doloso']]
df_ano_hommicidio_doloso = df_ano_hommicidio_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
print('\n----Obtendo dados sobre Homicídios Doloso por ano ----')
print(df_ano_hommicidio_doloso.head())

# Criando o DataFrame Homicídio Doloso e culposo por delegacias 
df_cisp_dol_culp = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_cisp_dol_culp = df_cisp_dol_culp.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()

print('\n----Obtendo dados sobre Homicídios Doloso e culposo ----')
print(df_cisp_dol_culp.head())