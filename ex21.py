numeros = []

for i in range(0, 10):
    numeros.append(int(input(f"Insira o {i+1}° número: \n")))

# print(len(numeros))

for i in range(0,10):
    print(f"--{numeros[i]}--")

soma = 0
for i in range(0,10):
    soma += numeros[i]
print(soma)