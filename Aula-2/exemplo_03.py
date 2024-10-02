# Valor prestação em atraso
prestacao=float(input("Informe o valor da prestação R$ "))
taxa = float(input("Informe o valor da taxa de juros mensal:"))
tempo=int(input("Informe o tempo de atraso:"))
valor_final = prestacao+(prestacao*(taxa/100)*tempo)
print(f"O valor de atraso será de R$ {valor_final: .2f}")