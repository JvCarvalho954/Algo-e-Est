valores = []
for i in range(0,4):
    valores.append(int(input("Insira um valor inteiro: \n")))
multip = int(input("Insira um valor inteiro para multiplicar: \n"))
for i in range(0,4):
    valores[i] = valores[i]*multip
print(valores)