#Programa Média com aprovação ou reprovação
nome=input("Informe o nome do estudante: ")
n1=float(input("Informe a primeira nota de 0 a 100: "))
n2=float(input("Informe a segunda nota de 0 a 100: "))
media=(n1+n2)/2
print(media)
if media >=70:
    print("Parabéns, você foi aprovado")
elif media >=30 and media <70:
    print("Você está em recuparação")
elif media <30:
    print("Infelizmente você não foi aprovado")

