# criando login email
emailCorreto = str.lower(input("crie um Email:\n"))
# criando login senha
senha = input("crie uma senha:\n")
if len(senha) < 8:
    print("senha muito pequena, minimo 8 caracteres")
else:
    senhaCorreto = senha
    # efetuando login
    email = str.lower(input("insira seu email:\n"))
    senha = input("insira sua senha:\n")
    if email == emailCorreto:
        if senha == senhaCorreto:
            print("Bem vindo!")
    else:
        print("email ou senha incorretos")