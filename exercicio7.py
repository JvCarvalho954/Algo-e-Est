num1 = float(input("Insira o primeiro valor numérico"))
num2 = float(input("insira o segundo valor numérico"))
simb = input("insira um simbolo de operação (+, -, *, /)")
resul = 0

if simb == "+":
    resul = num1 + num2
if simb == "-":
    resul = num1-num2
if simb == "*":
    resul = num1*num2
if simb == "/":
    resul = num1/num2
print("resultado:", resul)