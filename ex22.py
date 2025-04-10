palavras = []
for i in range(0,6):
    palavras.append(input("Insira uma palavra! \n"))

contPalavra = 0
for i in range(0, len(palavras)):
    if len(palavras[i]) > 5:
        contPalavra+= 1
print(f"Tem {contPalavra} palavras com mais de 5 caracteres!")