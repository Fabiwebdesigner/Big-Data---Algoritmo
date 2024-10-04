try:
    idade=int(input("Informe sua idade"))
    tempo_trab = int(input("Informe quantos anos trabalhou"))
except ValueError:
     print("Verifique os dados informados")
else:
    if idade>=65:
        print("Apto a aposentadoria")
    elif tempo_trab>=30:
        print("Apto a aposentadoria")
    elif idade >= 60 and tempo_trab>=25:
        print("Apto a aposentadoria")
    else:
        print("Inapto a Aposentadoria")