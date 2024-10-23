import pandas as pd
# Importando a Base de Dados
endereco_dados = 'Base_Dados\Funcionarios.csv'

# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Exibindo os Dados do DataFrame 
print('---- DADOS DOS FUNCIONÁRIOS ----')
print(df_funcionarios.head())

#Realizando o cálculo da média salarial
media_sal = df_funcionarios['Salário'].mean(axis=0)
print(f"A média salarial é {media_sal:.2f} reais.")

#Realizando o cálculo da média das idades
media_idade = df_funcionarios['Idade'].mean(axis=0)
print(f"A média das idades é {media_idade:.0f} anos.")

#Realizando cálculo do maior e menor tempo de casa, e a diferença entre eles
maior_tempo = df_funcionarios['Tempo'].max(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
dif_tempo = maior_tempo - menor_tempo
print(f"O maior tempo de casa é {maior_tempo:.0f}. " )
print(f"O menor tempo de casa é {menor_tempo:.0f}.")
print(f"A diferença de tempo de casa é {dif_tempo:.0f}.")

# Cálculo da Média de tempo de casa
media_tempo = df_funcionarios['Tempo'].mean(axis=0)
print(f"A média do tempo de casa é {media_tempo:.0f} anos.")

# Cálculo funcionário mais novo e mais velho, bem como a diferença de idade entre eles
#Para ocultar a indexação (localização do dado)usa-se .to_string (index=False)
func_velho = df_funcionarios[df_funcionarios['Idade'] == [maior_idade]['Nome']
func_novo = df_funcionarios[df_funcionarios['Idade'] == [menor_idade]['Nome']
print(f"O funcionário com mais tempo de casa é {func_velho.values[0]} e o com menos tempo de casa é {func_novo.values[0]}")                                                                           

#Cálculo da quantidade de funcionários
qtd_func = df_funcionarios['Nome'].count
print(f"A empresa possui {qtd_func:.0f} funcionários")

#Cálculo funcionário maior salário
maior_sal = df_funcionarios['Salário'] == [maior_sal]['Nome']
print(f"O funcionário com maior salário é {maior_sal:.0f}") 

#Cálculo do funcionário com maior tempo de casa

