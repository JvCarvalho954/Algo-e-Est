notas = []
soma = 0
for i in range(0, 5):
    notas.append(int(input(f"Insira {i+1}° nota: \n")))
    soma += notas[i]

media = soma/len(notas)
# print(f"Média : {soma/len(notas)}")
print(f"Média : {media}")