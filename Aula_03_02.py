# Roubo de automóveis: 100,90,80,120,110,90,70
# Furto de automóveis: 80,60,70,60,100,50,30
# Recuperação de automóveis: 70,50,90,80,100,70,50

import pandas as pd
roubos = pd.Series([100,90,80,120,110,90,70])
furtos = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])
total_roubos_furtos = roubos + furtos
taxa_recuperacao = recuperacao/total_roubos_furtos
# Resultados
print("Quantidade de roubos de automóveis + furto de automóveis diária:")
print(total_roubos_furtos)

print("\nTaxa de recuperação de automóveis diária (em porcentagem):")
for dia, taxa in enumerate(taxa_recuperacao, start=1):
    print(f"Dia {dia}: {taxa * 100:.2f}%")