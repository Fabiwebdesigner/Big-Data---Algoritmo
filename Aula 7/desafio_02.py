#O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final
#informe a menor, a maior e a média das temperaturas.

# Inicializando uma lista para armazenar as temperaturas
temperaturas = []

# Solicitando ao usuário para inserir as temperaturas (digite 'sair' para encerrar)
while True:
    temp = input("Digite a temperatura (ou 'sair' para encerrar): ")
    if temp.lower() == 'sair':
        break
    try:
        temperaturas.append(float(temp))
    except ValueError:
        print("Por favor, insira um valor válido.")

# Verificando se a lista não está vazia
if temperaturas:
    menor = min(temperaturas)
    maior = max(temperaturas)
    media = sum(temperaturas) / len(temperaturas)

    print(f"\nMenor temperatura: {menor}°C")
    print(f"Maior temperatura: {maior}°C")
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("Nenhuma temperatura foi inserida.")