h=float(input("Informe a sua altura: "))
sexo= input("Informe m para Masculino e f para feminino: ")
if sexo =="m"or sexo=="M":
    m = (72.7 * h) - 58
    print(f"O seu peso ideal é {m: .2f}:")    
elif sexo=="f"or sexo=="F":
    f = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {f: .2f}:") 
else:
    print("Verifique o sexo informado")