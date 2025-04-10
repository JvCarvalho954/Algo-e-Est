tabuada = []
valor = int(input("Insira um valor inteiro: \n"))
for i in range(1,11):
    tabuada.append(valor*i)
    print(f"{valor} * {i} = {tabuada[i-1]}")