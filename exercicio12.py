status_conta = True
saldo = float(input("insira o saldo do client:\n"))
if saldo < 0:
    print("procure um acordo para a dívida")
    status_conta = True
elif saldo == 0:
    print("conta desativada")
    status_conta = False
else:
    print("conta ativa")
    status_conta = True