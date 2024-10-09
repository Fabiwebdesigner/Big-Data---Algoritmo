#Criar 2 vetores, um com nomes e outro com senhas
usuarios = ["pedro", "maria", "duda", "dirceu", "elvis"]
senhas = ["123", "345", "567", "@@@$$", "8910"]
usuarios = input("Informe o nome de acesso ao sistema: ")
for i in range (len(usuarios)):
    if ususarios [i] == usuario:
        senha = input ("Informe a senha de acesso:")
        if senhas [i] == senha:
            resp = "Acesso Liberado"
        else:
            resp = "Senha não confere"
        break
    else:
        resp = "Usuário não encontrado"
print (resp)