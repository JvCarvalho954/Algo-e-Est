compra = float(input("insira o valor da compra: \n"))
if compra >= 100:
    desconto = compra*0.9
    print("O valor da compra com desconto: ", desconto)
else:
    print("O valor da compra sem desconto: ", compra)