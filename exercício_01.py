# Faça um programa para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), 
# o desconto e o total a pagar (total a pagar = total -desconto), sabendo que:
#Se quantidade <= 5 o desconto será de 2%. // Se quantidade > 5 e quantidade <=10 o desconto será de 3%. // Se quantidade > 10 o desconto será de 5%.

try:
    nome=input("Informe o nome do produto que você adquiriu: ")
    Qtde = int(input("Informe a quantidade adquirida: "))
    Valor = float(input ("Informe o valor unitário do produto"))
except ValueError:
    print("Verifique os valores informados")
else:
    Total = Qtde*Valor
    print(f"O valor total sem desconto é: {Total:.2f}")
    if Qtde <=5:
        Total = Valor*0.98
    elif Qtde>5 and Qtde<=10:
        Total = Valor*0.97
    else:
        Total = Valor*0.95
print(f"O valor total com desconto é R$ {Total:.2f}")