nomes_01 = "Alessandro, Maria, Pedro, Duda, Eduardo"
nomes_02 = ["Alessandro", "Maria", "Pedro", "Duda", "Eduardo"]
print(nomes_01)
print(nomes_02)
print(nomes_02[2])  #Para identificar como vetor e selecionar apenas 1 valor, cada valor precisa estar entre aspas
print(len(nomes_02)) # o comnado len serve para determinar a qtde de vetores
for i in range (len(nomes_02)):
    print(nomes_02[i])