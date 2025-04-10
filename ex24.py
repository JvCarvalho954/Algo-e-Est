numeros = []
maior = 0
numeros.append(int(input("Insira um valor inteiro: \n")))
menor = numeros[0]
for i in range(1,5):
    numeros.append(int(input("Insira um valor inteiro: \n")))
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print(f"Menor: {menor} | Maior: {maior}")