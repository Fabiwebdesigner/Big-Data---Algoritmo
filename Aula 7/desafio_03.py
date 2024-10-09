#Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual 
#coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino) // cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos) // idade
#Faça um programa que determine e escreva:
#a) a maior e a menor idade dos habitantes, assim como a média das idades;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

# Coletando os dados dos habitantes
while True:
    print("\nInsira os dados do habitante (ou digite 'sair' para encerrar):")

    # Solicita sexo
    sexo = input("Sexo (masculino/feminino): ").lower()
    if sexo == 'sair':
        break

    # Solicita cor dos olhos
    olhos = input("Cor dos olhos (azuis/verdes/castanhos): ").lower()

    # Solicita cor dos cabelos
    cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ").lower()

    # Solicita idade
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Por favor, insira uma idade válida.")
        continue

    # Armazena as informações em uma lista de dicionários
    habitantes.append({'sexo': sexo,'olhos': olhos,'cabelos': cabelos,'idade': idade})

# Verifica se a lista de habitantes não está vazia
if habitantes:
    # Variáveis para armazenar a menor e maior idade
    menor_idade = habitantes[0]['idade']
    maior_idade = habitantes[0]['idade']

    for habitante in habitantes:
        idade = habitante['idade']
        total_idades += idade

        # Encontrar a menor e a maior idade
        if idade < menor_idade:
            menor_idade = idade
        if idade > maior_idade:
            maior_idade = idade

        # Condição b: Contar as mulheres com idade entre 18 e 35 anos
        if habitante['sexo'] == 'feminino' and 18 <= idade <= 35:
            feminino_18_35 += 1

        # Condição c: Contar pessoas com olhos verdes e cabelos louros
        if habitante['olhos'] == 'verdes' and habitante['cabelos'] == 'louros':
            olhos_verdes_cabelos_louros += 1

    # Calcula a média de idades
    media_idades = total_idades / len(habitantes)

    # Exibe os resultados
    print(f"\nA maior idade é: {maior_idade}")
    print(f"A menor idade é: {menor_idade}")
    print(f"A média das idades é: {media_idades:.2f}")
    print(f"\nQuantidade de mulheres entre 18 e 35 anos: {feminino_18_35}")
    print(f"\nQuantidade de pessoas com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")
else:
    print("Nenhum habitante foi registrado.")