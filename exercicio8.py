login_certo = "Jv"
senha_certo = 12345

login = input("Insira o nome do usuário:\n")
senha = int(input("Insira a senha:\n"))
if login == login_certo:
    if senha == senha_certo:
        print("Bem vindo!")
else:
    print("Login ou senha incorretos")