#Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.

n1=float (input("Informe o valor recebido por hora trabalhada: "))
n2= float (input("Qual a quantidade de horas trabalhadas no mês? "))
sal_bruto = n1*n2
print(f"O valor do salário bruto é: {sal_bruto:.2f}")
Desc_IRRF = sal_bruto * 0.08
print(f"O valor do desconto do IRRF é: {Desc_IRRF:.2f}")
Desc_INSS = sal_bruto * 0.11
print(f"O valor do desconto do INSS é: {Desc_INSS:.2f}")
Desc_Sind = sal_bruto * 0.05
print(f"O valor do desconto do sindicato é: {Desc_Sind:.2f}")
sal_liq = sal_bruto - (Desc_IRRF + Desc_INSS + Desc_Sind)
print(f"O valor do salário líquido é: {sal_liq:.2f}")


