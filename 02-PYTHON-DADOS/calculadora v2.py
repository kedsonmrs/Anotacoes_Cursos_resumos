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

    nums = ((float(input("Digite o primeiro numero: "))),(float(input("Digite o segundo numero: "))))
    
    if tip == 1:
        res = 0
        for i in nums:
            res += i
        print(f"Resultado de {int(nums[0])} + {int(nums[1])} = {int(res)}")
    elif tip == 2:
        res = nums[0] - nums[1]
        print(f"Resultado de {int(nums[0])} - {int(nums[1])} = {int(res)}")
    elif tip == 3:
        res = nums[0] * nums [1]
        print(f"Resultado de {int(nums[0])} x {int(nums[1])} = {int(res)}")
    elif tip == 4:
        res = nums[0] * nums[1]
        print(f"Resultado de {nums[0]} / {nums[1]} = {res}")

    v = input("Deseja realizar outro calculo? S/N: ")
    if v == "N":
        print("Obigado!")
        break
