# <- isso é um comentário
# # print("Mensagem") Ctrl + ;
# idade = 2
# altura = 0.5
# peso = 5.95
# nome = "francisco"
# print(idade,"\n", altura, peso, nome)
nome = input("insira seu nome: \n") # Python considera todo input como String
idade = int(input("insira sua idade: \n")) # por isso nesse caso, usamos o comando int() que transforma a String em int
peso = float(input("insira seu peso: \n")) # mesma coisa com float, float é capaz de guardar numeros reais
print(f"{nome}, {idade} anos {peso} kg") 
# o comando f"" é para formatar um testo, ele permite outros comandos de formatação