print(("-"*10),("CALCULADORA"),("-"*10))
print("\n")
s = True    
while s == True:
    print("Selecione o tipo de operação desejada:")
    print("\n")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

    conj_valid = (1,2,3,4)
    
    tip = int(input("Selecione a operaçao desejada: "))
    if tip not in conj_valid:
        v = input("Valor não válido, ainda deseja realizar uma operação? S/N")
        if v == "S":
            continue
        elif v == "N":
            break

    num = float(input("Digite o primeiro: "))
    num2 = float(input("Digite o segundo numero: "))

    if tip == 1:
        res = num + num2
        print(f"Resultado de {int(num)} + {int(num2)} = {int(res)}")
    elif tip == 2:
        res = num - num2
        print(f"Resultado de {int(num)} - {int(num2)} = {int(res)}")
    elif tip == 3:
        res = num * num2
        print(f"Resultado de {int(num)} x {int(num2)} = {int(res)}")
    elif tip == 4:
        res = num / num2
        print(f"Resultado de {num} / {num2} = {res}")

    v = input("Deseja realizar outro calculo? S/N: ")
    if v == "N":
        print("Obigado!")
        break
