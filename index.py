#  <- isso é um comentário
#  # print("Mensagem") Ctrl + ;
#idade = 2
#altura = 0.5
#peso = 5.95
#nome = "francisco"
#print(idade,"\n", altura, peso, nome)
#  para declaração de variaveis no Python, é recomendado o uso do case Snake_case
# ----------------------------------
#nome = input("insira seu nome: ") # Python considera todo input como String
#idade = int(input("insira sua idade: ")) # por isso nesse caso,usamos int() que transforma a String em int
#peso = float(input("insira seu peso: ")) # mesma coisa com float(), float é capaz de guardar numeros reais
#print(f"{nome}, {idade} anos {peso} kg") 
#  o comando f"" é para formatar um testo, ele permite outros comandos de formatação
#  extra: o comando \n age como um "Enter" no meio de uma string, deve ser usado dentro de aspas ("")
# ----------------------------------
#pedaco_pizza = input("insira quantos pedaços de pizza comeu?")
#cliente = "John"
#print(type(pedaco_pizza))
#print(type(cliente))
#  função type() mostra o tipo de dado de uma variável
# ----------------------------------
#a = 8
#A = "haha"
#print(a)
#print(A)
#  Python é case sensitive, é muito importante manter as váriaveis com letras maiusculas e minusculas corretas
# ----------------------------------
#fruta1, fruta2, fruta3 = "maçã", "abacaxi", "banana"
#print(fruta1, fruta2, fruta3)
#  :O caramba, no Python é possivel a declaração de várias variáveis com vários valores em uma linha
#  Incrivel!
# ----------------------------------
#num1 = 5
#num2 = 10
#print(num1+num2)
#  '+' é capaz de somar váriaveis, e dentro de print também é possivel executar soma
#  Excelente!
#str3 = "a"
#str4 = "b"
#print(str3+str4)
#  Também é possivel a soma entre String!
#  Brilhante!
#  Mas apesar disso, não é possivel a soma entre números e letras!
# ----------------------------------
#nome = input("insira seu nome")
#print(f"Bem vindo {nome}")
#if nome == "hulk":
#  se o nome inserido pelo usuario for "hulk", então...
#   print("Bem vindo vigador mais forte!")
#else:
#  senão...
#   print("Acesso negado!")
#  Use a identação!!!
#  Em Python, ao inves de usarmos delimitadores ({}, () , ...), usamos a identação
#  use Tab ou ' ' (Espaço) como identação para demilitar escopos no código
#  meh :/ eu ainda prefiro delimitadores
# ----------------------------------
x = 5
if x>2 and x<10:
    print("O número está entre 2 e 10")
#  and é um operador relacional em inglês, o 'e'
#  que só retorna verdadeiro se ambas as condições forem verdadeiras
# Estupendo!
# ----------------------------------
if x<2 or x>4:
    print("O número está é menor que 2 ou maior que 4")
#  A operação relacional or corresponde ao "ou"
#  que significa que para retornar verdadeiro, apenas uma das duas condições devem ser verdadeiras
#  Magnifico!
# ----------------------------------
if not x>10:
    print("O número não é maior que 10")
#  not significa não e inverte o resultado de uma condição
#  ou seja, x é MENOR que 10, então seria FALSO, PORÉM a condição é INVERTIDA, resultando em VERDADEIRO
#  ou seja ele entraria no "if"
#  Maravilha!
# ----------------------------------
y = 8

if x>2 and (y>10 or not x == 5):
    print("A condição complexa foi atendida")
else:
    print("Codição não entendida")
#  é possivel usar vários operadores ao mesmo tempo
#  Uau!
#  Python segue a ordem de operadores lógicos: 1. not ; 2. and ; 3. or.