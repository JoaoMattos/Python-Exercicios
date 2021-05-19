a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
op = input("Digite a operação: ")
if op == '*+':
    print(a*b+a)
elif op == "+-":
    print(a+b-a)
elif op == '+':
    print(a+b)
elif op == '-':
    print(a-b)