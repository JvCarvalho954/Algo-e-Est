numeros = []
par = []
impar = []
for i in range(0,10):
    numeros.append(int(input("Insira um valor inteiro: \n")))
    if numeros[i]%2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])

print(f"Numeros pares: {par} \n Numeros impares: {impar}")